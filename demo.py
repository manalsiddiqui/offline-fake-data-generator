#!/usr/bin/env python3
"""
Comprehensive Demo of the Offline Fake Data Generator
"""

import json
import time
from fake_data_generator import FakeDataGenerator

def print_section(title):
    print(f"\n{'='*50}")
    print(f"🎭 {title}")
    print('='*50)

def demo_basic_generation():
    print_section("Basic Data Generation")
    
    generator = FakeDataGenerator()
    
    # Generate a basic persona
    persona = generator.generate_persona()
    
    print(f"Generated Person: {persona['name']}")
    print(f"Email: {persona['email']}")
    print(f"Phone: {persona['phone']}")
    print(f"Address: {persona['address']['full_address']}")
    print(f"Job: {persona['job']}")
    print(f"Age: {persona['age']}")
    print(f"SSN: {persona['ssn']}")
    print(f"Credit Card: {persona['credit_card']['number']} ({persona['credit_card']['provider']})")
    print(f"Website: {persona['website']}")
    print(f"Blood Type: {persona['blood_group']}")
    
    return persona

def demo_seeded_generation():
    print_section("Deterministic/Seeded Generation")
    
    generator = FakeDataGenerator()
    
    # Generate the same person multiple times with the same seed
    seed = "my-test-user-2024"
    
    print(f"Using seed: '{seed}'")
    print("\nGeneration 1:")
    persona1 = generator.create_seeded_persona(seed)
    print(f"Name: {persona1['name']}")
    print(f"Email: {persona1['email']}")
    
    print("\nGeneration 2 (same seed):")
    persona2 = generator.create_seeded_persona(seed)
    print(f"Name: {persona2['name']}")
    print(f"Email: {persona2['email']}")
    
    print(f"\n✅ Reproducible: {persona1['name'] == persona2['name']}")
    
    return persona1

def demo_persistence():
    print_section("Data Persistence & Management")
    
    generator = FakeDataGenerator()
    
    # Save some personas
    print("Saving personas...")
    
    personas = []
    for i in range(3):
        persona = generator.generate_persona()
        persona_id = generator.save_persona(persona)
        personas.append((persona_id, persona['name'], persona['email']))
        print(f"  Saved: {persona['name']} (ID: {persona_id[:8]}...)")
    
    # List all personas
    print(f"\nAll saved personas:")
    all_personas = generator.list_personas()
    for p in all_personas:
        print(f"  • {p['name']} ({p['email']}) - {p['created_at'][:10]}")
    
    # Load a specific persona
    if personas:
        test_id, test_name, test_email = personas[0]
        print(f"\nLoading persona: {test_name}")
        loaded_persona = generator.load_persona(test_id)
        print(f"  Loaded: {loaded_persona['name']} - {loaded_persona['email']}")
        
        # Regenerate the same persona
        print(f"\nRegenerating persona: {test_name}")
        regenerated = generator.regenerate_persona(test_id)
        if regenerated:
            print(f"  Regenerated: {regenerated['name']} - {regenerated['email']}")
    
    return len(all_personas)

def demo_export_formats():
    print_section("Export Formats")
    
    generator = FakeDataGenerator()
    persona = generator.generate_persona()
    persona_id = generator.save_persona(persona)
    
    print(f"Exporting persona: {persona['name']}")
    
    # JSON Export
    print("\n1. JSON Export (first 200 chars):")
    json_export = generator.export_persona(persona_id, 'json')
    print(json_export[:200] + "...")
    
    # YAML Export
    print("\n2. YAML Export (first 200 chars):")
    yaml_export = generator.export_persona(persona_id, 'yaml')
    print(yaml_export[:200] + "...")
    
    # CSV Export
    print("\n3. CSV Export (first 200 chars):")
    csv_export = generator.export_persona(persona_id, 'csv')
    print(csv_export[:200] + "...")

def demo_locales():
    print_section("International Locales")
    
    locales = [
        ('en_US', 'United States'),
        ('en_GB', 'United Kingdom'),
        ('de_DE', 'Germany'),
        ('fr_FR', 'France'),
        ('es_ES', 'Spain')
    ]
    
    for locale_code, locale_name in locales:
        try:
            generator = FakeDataGenerator(locale=locale_code)
            persona = generator.generate_persona()
            print(f"\n{locale_name} ({locale_code}):")
            print(f"  Name: {persona['name']}")
            print(f"  Address: {persona['address']['city']}, {persona['address']['country']}")
        except Exception as e:
            print(f"\n{locale_name} ({locale_code}): ❌ Not available")

def demo_form_data():
    print_section("Form Auto-Fill Data")
    
    generator = FakeDataGenerator()
    persona = generator.generate_persona()
    
    # Simulate form data extraction
    form_data = {
        'firstName': persona['first_name'],
        'lastName': persona['last_name'],
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
    
    print("Form-ready data:")
    for field, value in form_data.items():
        print(f"  {field}: {value}")

def main():
    print("🎭 OFFLINE FAKE DATA GENERATOR - COMPREHENSIVE DEMO")
    print("=" * 60)
    print("This tool generates realistic fake personal data for testing,")
    print("development, and privacy protection - completely offline!")
    
    # Run all demos
    demo_basic_generation()
    demo_seeded_generation()
    count = demo_persistence()
    demo_export_formats()
    demo_locales()
    demo_form_data()
    
    # Final summary
    print_section("Demo Complete!")
    print(f"✅ Generated multiple fake personas")
    print(f"✅ Demonstrated seeded/reproducible generation")
    print(f"✅ Saved and managed {count} personas")
    print(f"✅ Showed export capabilities (JSON, YAML, CSV)")
    print(f"✅ Tested international locales")
    print(f"✅ Demonstrated form auto-fill data")
    
    print(f"\n🚀 Next Steps:")
    print(f"• CLI: python cli.py generate --save")
    print(f"• Web: python run.py web (visit http://localhost:5000)")
    print(f"• Extension: Visit http://localhost:5000/extension")
    print(f"• Help: python run.py help")
    
    print(f"\n🔒 Privacy: All data generated and stored locally!")
    print(f"🎯 Use Cases: Testing, development, privacy protection")

if __name__ == "__main__":
    main() 