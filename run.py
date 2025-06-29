#!/usr/bin/env python3
"""
Simple launcher script for the Fake Data Generator
"""

import sys
import subprocess
import os
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import faker, flask, click, yaml, qrcode, tabulate
        return True
    except ImportError as e:
        print(f"Missing dependencies: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    if not check_dependencies():
        return 1
    
    if len(sys.argv) < 2:
        print("🎭 Offline Fake Data Generator")
        print()
        print("Usage:")
        print("  python run.py web        # Start web server")
        print("  python run.py cli        # Open CLI interface")
        print("  python run.py generate   # Quick generate")
        print("  python run.py help       # Show help")
        return 0
    
    command = sys.argv[1].lower()
    
    if command == 'web':
        try:
            from web_server import app, find_free_port
            port = find_free_port()
            if port:
                print(f"🌐 Starting web server on http://localhost:{port}")
                print("Press Ctrl+C to stop")
                app.run(debug=False, host='localhost', port=port)
            else:
                print("❌ Could not find a free port between 5000-5100")
                print("Try closing other applications or restart your computer")
        except KeyboardInterrupt:
            print("\n👋 Server stopped")
    
    elif command == 'cli':
        # Launch interactive CLI
        from cli import cli
        sys.argv = ['cli.py'] + sys.argv[2:]  # Pass remaining args to CLI
        cli()
    
    elif command == 'generate':
        # Quick generate and display
        from fake_data_generator import FakeDataGenerator
        generator = FakeDataGenerator()
        persona = generator.generate_persona()
        
        print(f"🎭 Generated Persona:")
        print(f"Name: {persona['name']}")
        print(f"Email: {persona['email']}")
        print(f"Phone: {persona['phone']}")
        print(f"Address: {persona['address']['full_address']}")
        print(f"Job: {persona['job']}")
        print(f"SSN: {persona['ssn']}")
        print(f"Credit Card: {persona['credit_card']['number']} ({persona['credit_card']['provider']})")
        
        save = input("\n💾 Save this persona? (y/N): ").lower().startswith('y')
        if save:
            persona_id = generator.save_persona(persona)
            print(f"✅ Saved with ID: {persona_id}")
    
    elif command == 'help':
        print("🎭 Offline Fake Data Generator - Help")
        print()
        print("Web Interface:")
        print("  python run.py web")
        print("  Then visit http://localhost:5000")
        print()
        print("Command Line:")
        print("  python run.py cli generate --save")
        print("  python run.py cli list")
        print("  python run.py cli seed 'my-test-data'")
        print()
        print("Browser Extension:")
        print("  Start web server, then visit http://localhost:5000/extension")
        print()
        print("Features:")
        print("  • Generate realistic fake personal data")
        print("  • Save and reload personas")
        print("  • Deterministic generation with seeds")
        print("  • Export to JSON, YAML, CSV, QR code")
        print("  • Browser form auto-fill")
        print("  • Complete offline operation")
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Run 'python run.py help' for usage information")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main()) 