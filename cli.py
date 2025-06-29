#!/usr/bin/env python3
"""
CLI interface for the Fake Data Generator
"""

import click
import json
from tabulate import tabulate
from fake_data_generator import FakeDataGenerator

@click.group()
@click.option('--locale', default='en_US', help='Locale for data generation (e.g., en_US, en_GB, de_DE)')
@click.pass_context
def cli(ctx, locale):
    """Offline Fake Data Generator CLI"""
    ctx.ensure_object(dict)
    ctx.obj['generator'] = FakeDataGenerator(locale=locale)

@cli.command()
@click.option('--save', is_flag=True, help='Save the generated persona')
@click.option('--seed', help='Seed for reproducible generation')
@click.option('--format', 'output_format', default='table', 
              type=click.Choice(['table', 'json', 'yaml']), 
              help='Output format')
def generate(save, seed, output_format):
    """Generate a new fake persona"""
    generator = click.get_current_context().obj['generator']
    
    if seed:
        persona = generator.create_seeded_persona(seed)
    else:
        persona = generator.generate_persona()
    
    if save:
        persona_id = generator.save_persona(persona)
        click.echo(f"Persona saved with ID: {persona_id}")
    
    if output_format == 'json':
        click.echo(json.dumps(persona, indent=2, default=str))
    elif output_format == 'yaml':
        click.echo(generator.export_persona(persona.get('id', 'temp'), 'yaml'))
    else:
        # Table format
        display_persona_table(persona)

@cli.command()
def list():
    """List all saved personas"""
    generator = click.get_current_context().obj['generator']
    personas = generator.list_personas()
    
    if not personas:
        click.echo("No saved personas found.")
        return
    
    headers = ['ID', 'Name', 'Email', 'Created']
    table_data = [[p['id'][:8] + '...', p['name'], p['email'], p['created_at'][:10]] 
                  for p in personas]
    
    click.echo(tabulate(table_data, headers=headers, tablefmt='grid'))

@cli.command()
@click.argument('persona_id')
@click.option('--format', 'output_format', default='table', 
              type=click.Choice(['table', 'json', 'yaml', 'csv', 'qr']), 
              help='Output format')
def show(persona_id, output_format):
    """Show a specific persona"""
    generator = click.get_current_context().obj['generator']
    persona = generator.load_persona(persona_id)
    
    if not persona:
        click.echo(f"Persona with ID {persona_id} not found.")
        return
    
    if output_format in ['json', 'yaml', 'csv', 'qr']:
        output = generator.export_persona(persona_id, output_format)
        click.echo(output)
    else:
        display_persona_table(persona)

@cli.command()
@click.argument('persona_id')
def regenerate(persona_id):
    """Regenerate a persona using the same seed"""
    generator = click.get_current_context().obj['generator']
    persona = generator.regenerate_persona(persona_id)
    
    if not persona:
        click.echo(f"Persona with ID {persona_id} not found.")
        return
    
    click.echo(f"Regenerated persona: {persona['name']}")
    display_persona_table(persona)

@cli.command()
@click.argument('persona_id')
@click.confirmation_option(prompt='Are you sure you want to delete this persona?')
def delete(persona_id):
    """Delete a persona"""
    generator = click.get_current_context().obj['generator']
    success = generator.delete_persona(persona_id)
    
    if success:
        click.echo(f"Persona {persona_id} deleted successfully.")
    else:
        click.echo(f"Persona with ID {persona_id} not found.")

@cli.command()
@click.argument('seed_string')
@click.option('--save', is_flag=True, help='Save the generated persona')
def seed(seed_string, save):
    """Generate a persona from a seed string (deterministic)"""
    generator = click.get_current_context().obj['generator']
    persona = generator.create_seeded_persona(seed_string)
    
    if save:
        persona_id = generator.save_persona(persona)
        click.echo(f"Persona saved with ID: {persona_id}")
    
    click.echo(f"Generated from seed: '{seed_string}'")
    display_persona_table(persona)

def display_persona_table(persona):
    """Display persona in a nice table format"""
    data = [
        ['Name', persona['name']],
        ['Email', persona['email']],
        ['Phone', persona['phone']],
        ['Address', persona['address']['full_address']],
        ['Job', persona['job']],
        ['SSN', persona['ssn']],
        ['Credit Card', f"{persona['credit_card']['number']} ({persona['credit_card']['provider']})"],
        ['Website', persona['website']],
        ['Age', persona['age']],
        ['Blood Group', persona['blood_group']],
    ]
    
    click.echo(tabulate(data, headers=['Field', 'Value'], tablefmt='grid'))

if __name__ == '__main__':
    cli() 