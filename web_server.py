#!/usr/bin/env python3
"""
Web server for browser integration and web interface
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from fake_data_generator import FakeDataGenerator

app = Flask(__name__)
generator = FakeDataGenerator()

@app.route('/')
def index():
    """Main web interface"""
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def api_generate():
    """API endpoint to generate new persona"""
    data = request.get_json() or {}
    seed = data.get('seed')
    save = data.get('save', False)
    
    if seed:
        persona = generator.create_seeded_persona(seed)
    else:
        persona = generator.generate_persona()
    
    if save:
        persona_id = generator.save_persona(persona)
        persona['saved_id'] = persona_id
    
    return jsonify(persona)

@app.route('/api/personas', methods=['GET'])
def api_list_personas():
    """API endpoint to list all personas"""
    personas = generator.list_personas()
    return jsonify(personas)

@app.route('/api/personas/<persona_id>', methods=['GET'])
def api_get_persona(persona_id):
    """API endpoint to get specific persona"""
    persona = generator.load_persona(persona_id)
    if persona:
        return jsonify(persona)
    return jsonify({'error': 'Persona not found'}), 404

@app.route('/api/personas/<persona_id>', methods=['DELETE'])
def api_delete_persona(persona_id):
    """API endpoint to delete persona"""
    success = generator.delete_persona(persona_id)
    if success:
        return jsonify({'success': True})
    return jsonify({'error': 'Persona not found'}), 404

@app.route('/api/personas/<persona_id>/regenerate', methods=['POST'])
def api_regenerate_persona(persona_id):
    """API endpoint to regenerate persona"""
    persona = generator.regenerate_persona(persona_id)
    if persona:
        return jsonify(persona)
    return jsonify({'error': 'Persona not found'}), 404

@app.route('/api/fill-form', methods=['POST'])
def api_fill_form():
    """API endpoint for browser extension to get form fill data"""
    data = request.get_json() or {}
    persona_id = data.get('persona_id')
    
    if persona_id:
        persona = generator.load_persona(persona_id)
    else:
        persona = generator.generate_persona()
    
    if not persona:
        return jsonify({'error': 'Persona not found'}), 404
    
    # Return data in a format suitable for form filling
    form_data = {
        'firstName': persona['first_name'],
        'lastName': persona['last_name'],
        'name': persona['name'],
        'email': persona['email'],
        'phone': persona['phone'],
        'address': persona['address']['street'],
        'city': persona['address']['city'],
        'state': persona['address']['state'],
        'zip': persona['address']['zipcode'],
        'country': persona['address']['country'],
        'company': persona['company'],
        'jobTitle': persona['job_title'],
        'website': persona['website'],
        'creditCard': persona['credit_card']['number'],
        'ccExpiry': persona['credit_card']['expire'],
        'ccCvv': persona['credit_card']['security_code'],
    }
    
    return jsonify(form_data)

@app.route('/extension')
def extension_popup():
    """Browser extension popup interface"""
    return render_template('extension.html')

def find_free_port(start_port=5000, max_port=5100):
    """Find a free port starting from start_port"""
    import socket
    for port in range(start_port, max_port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    return None

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Find a free port
    port = find_free_port()
    if port:
        print(f"🌐 Starting web server on http://localhost:{port}")
        print("Press Ctrl+C to stop")
        app.run(debug=True, host='localhost', port=port)
    else:
        print("❌ Could not find a free port between 5000-5100")
        print("Please close other applications using these ports") 