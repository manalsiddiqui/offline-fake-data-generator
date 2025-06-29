#!/usr/bin/env python3
"""
Offline Fake Data Generator
A comprehensive tool for generating fake personal information offline
"""

import json
import os
import uuid
import datetime
from faker import Faker
from faker.providers import internet, phone_number, credit_card, automotive, company
import hashlib
import yaml
import qrcode
from io import BytesIO
import base64

class FakeDataGenerator:
    def __init__(self, locale='en_US', data_dir='fake_data'):
        self.fake = Faker(locale)
        self.data_dir = data_dir
        self.personas_file = os.path.join(data_dir, 'personas.json')
        self.ensure_data_dir()
        
        # Add additional providers
        self.fake.add_provider(internet)
        self.fake.add_provider(phone_number)
        self.fake.add_provider(credit_card)
        self.fake.add_provider(automotive)
        self.fake.add_provider(company)
        
    def ensure_data_dir(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            
    def generate_persona(self, seed=None, persona_id=None):
        """Generate a complete fake persona"""
        if seed:
            Faker.seed(seed)
            
        if not persona_id:
            persona_id = str(uuid.uuid4())
            
        # Generate profile
        profile = self.fake.profile()
        
        # Enhanced persona data
        persona = {
            'id': persona_id,
            'created_at': datetime.datetime.now().isoformat(),
            'seed': seed,
            
            # Basic info
            'name': profile['name'],
            'first_name': profile['name'].split()[0],
            'last_name': profile['name'].split()[-1],
            'username': profile['username'],
            'sex': profile['sex'],
            'birthdate': profile['birthdate'].isoformat(),
            'age': (datetime.date.today() - profile['birthdate']).days // 365,
            
            # Contact info
            'email': profile['mail'],
            'phone': self.fake.phone_number(),
            'mobile': self.fake.phone_number(),
            
            # Address
            'address': {
                'street': self.fake.street_address(),
                'city': self.fake.city(),
                'state': self.fake.state(),
                'state_abbr': self.fake.state_abbr(),
                'zipcode': self.fake.zipcode(),
                'country': self.fake.country(),
                'country_code': self.fake.country_code(),
                'full_address': profile['address']
            },
            
            # Professional info
            'job': profile['company'] + ' - ' + profile['job'],
            'company': profile['company'],
            'job_title': profile['job'],
            'ssn': profile['ssn'],
            
            # Online presence
            'website': self.fake.url(),
            'social_media': {
                'twitter': f"@{self.fake.user_name()}",
                'linkedin': f"linkedin.com/in/{self.fake.user_name()}",
                'facebook': f"facebook.com/{self.fake.user_name()}"
            },
            
            # Financial
            'credit_card': {
                'number': self.fake.credit_card_number(),
                'provider': self.fake.credit_card_provider(),
                'security_code': self.fake.credit_card_security_code(),
                'expire': self.fake.credit_card_expire()
            },
            
            # Additional details
            'blood_group': self.fake.random_element(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']),
            'height': f"{self.fake.random_int(150, 200)} cm",
            'weight': f"{self.fake.random_int(50, 120)} kg",
            'license_plate': self.fake.license_plate(),
            'mother_maiden_name': self.fake.last_name(),
            'favorite_color': self.fake.color_name(),
        }
        
        return persona
        
    def save_persona(self, persona):
        """Save persona to persistent storage"""
        personas = self.load_all_personas()
        personas[persona['id']] = persona
        
        with open(self.personas_file, 'w') as f:
            json.dump(personas, f, indent=2, default=str)
            
        return persona['id']
        
    def load_persona(self, persona_id):
        """Load a specific persona by ID"""
        personas = self.load_all_personas()
        return personas.get(persona_id)
        
    def load_all_personas(self):
        """Load all saved personas"""
        if not os.path.exists(self.personas_file):
            return {}
            
        try:
            with open(self.personas_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
            
    def list_personas(self):
        """List all saved personas with basic info"""
        personas = self.load_all_personas()
        return [{
            'id': p['id'],
            'name': p['name'],
            'email': p['email'],
            'created_at': p['created_at']
        } for p in personas.values()]
        
    def delete_persona(self, persona_id):
        """Delete a persona"""
        personas = self.load_all_personas()
        if persona_id in personas:
            del personas[persona_id]
            with open(self.personas_file, 'w') as f:
                json.dump(personas, f, indent=2, default=str)
            return True
        return False
        
    def regenerate_persona(self, persona_id):
        """Regenerate a persona using the same seed"""
        persona = self.load_persona(persona_id)
        if not persona:
            return None
            
        new_persona = self.generate_persona(
            seed=persona['seed'], 
            persona_id=persona_id
        )
        self.save_persona(new_persona)
        return new_persona
        
    def export_persona(self, persona_id, format='json'):
        """Export persona in various formats"""
        persona = self.load_persona(persona_id)
        if not persona:
            return None
            
        if format == 'json':
            return json.dumps(persona, indent=2, default=str)
        elif format == 'yaml':
            return yaml.dump(persona, default_flow_style=False)
        elif format == 'csv':
            # Flatten the persona for CSV
            flat_data = self._flatten_dict(persona)
            header = ','.join(flat_data.keys())
            values = ','.join(str(v) for v in flat_data.values())
            return f"{header}\n{values}"
        elif format == 'qr':
            # Generate QR code with basic info
            qr_data = f"Name: {persona['name']}\nEmail: {persona['email']}\nPhone: {persona['phone']}"
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
            
    def _flatten_dict(self, d, parent_key='', sep='_'):
        """Flatten nested dictionary for CSV export"""
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
        
    def create_seeded_persona(self, seed_string):
        """Create a persona with a deterministic seed based on a string"""
        seed = int(hashlib.md5(seed_string.encode()).hexdigest(), 16) % (2**32)
        persona = self.generate_persona(seed=seed)
        persona['seed_string'] = seed_string
        return persona

if __name__ == "__main__":
    # Example usage
    generator = FakeDataGenerator()
    
    # Generate a new persona
    persona = generator.generate_persona()
    persona_id = generator.save_persona(persona)
    
    print(f"Generated persona: {persona['name']}")
    print(f"Persona ID: {persona_id}")
    print(f"Email: {persona['email']}")
    print(f"Address: {persona['address']['full_address']}") 