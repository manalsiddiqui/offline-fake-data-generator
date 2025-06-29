# 🎭 Offline Fake Data Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform Support](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/manalsiddiqui/offline-fake-data-generator)
[![Privacy First](https://img.shields.io/badge/privacy-first-green.svg)](https://github.com/manalsiddiqui/offline-fake-data-generator)

A comprehensive tool for generating realistic fake personal information offline. Perfect for testing, development, and privacy-conscious browsing.

> **🔒 Privacy-First Design**: All data generation happens locally. No network requests, no telemetry, no data collection.

## ✨ Features

- **Offline Generation**: Works completely offline with no external dependencies
- **Persistent Storage**: Save and reload fake personas
- **Deterministic Seeds**: Generate the same fake data using string seeds
- **Multiple Interfaces**: CLI, Web UI, and browser extension popup
- **Rich Data Types**: Names, addresses, phones, emails, SSNs, credit cards, and more
- **Export Options**: JSON, YAML, CSV, and QR code formats
- **Browser Integration**: Auto-fill forms with fake data
- **Privacy-First**: All data stays on your device

## 🚀 Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate Data via CLI**
   ```bash
   python cli.py generate --save
   ```

3. **Start Web Interface**
   ```bash
   python web_server.py
   ```
   Then visit `http://localhost:5000`

4. **Browser Extension**
   Visit `http://localhost:5000/extension` for form auto-fill popup

## 📱 Usage Examples

### Command Line Interface

```bash
# Generate a new persona
python cli.py generate

# Generate with seed for reproducible data
python cli.py seed "my-test-user" --save

# List all saved personas
python cli.py list

# Show specific persona
python cli.py show <persona-id>

# Export persona as JSON/YAML/CSV
python cli.py show <persona-id> --format json
```

### Web Interface

1. Start the server: `python web_server.py`
2. Open `http://localhost:5000`
3. Click "Generate New Persona" or use seeds
4. Enable auto-save or manually save personas
5. View saved personas in the "Saved Personas" tab

### Browser Integration

1. Start the server
2. Visit `http://localhost:5000/extension`
3. Generate or select fake data
4. Click on any field to copy to clipboard
5. Paste into web forms manually

### API Endpoints

- `POST /api/generate` - Generate new persona
- `GET /api/personas` - List all personas
- `GET /api/personas/<id>` - Get specific persona
- `DELETE /api/personas/<id>` - Delete persona
- `POST /api/personas/<id>/regenerate` - Regenerate persona
- `POST /api/fill-form` - Get form fill data

## 🛠️ Python API

```python
from fake_data_generator import FakeDataGenerator

# Create generator
generator = FakeDataGenerator(locale='en_US')

# Generate persona
persona = generator.generate_persona()

# Generate with seed
persona = generator.create_seeded_persona("my-seed")

# Save persona
persona_id = generator.save_persona(persona)

# Load persona
saved_persona = generator.load_persona(persona_id)

# Export persona
json_data = generator.export_persona(persona_id, 'json')
```

## 📊 Generated Data Types

- **Personal**: Name, age, gender, birthdate, blood type
- **Contact**: Email, phone, mobile, website
- **Address**: Street, city, state, ZIP, country
- **Professional**: Job title, company, SSN
- **Financial**: Credit card number, expiry, CVV, provider
- **Online**: Username, social media profiles
- **Physical**: Height, weight, favorite color
- **Family**: Mother's maiden name
- **Vehicle**: License plate number

## 🔧 Configuration

### Locales
Support for multiple locales (en_US, en_GB, de_DE, fr_FR, etc.):
```bash
python cli.py --locale de_DE generate
```

### Data Directory
Custom data storage location:
```python
generator = FakeDataGenerator(data_dir='my_fake_data')
```

## 🗂️ File Structure

```
├── fake_data_generator.py  # Core generator class
├── cli.py                  # Command line interface
├── web_server.py          # Flask web server
├── templates/
│   ├── index.html         # Main web interface
│   └── extension.html     # Browser extension popup
├── fake_data/             # Generated data storage
│   └── personas.json      # Saved personas
└── requirements.txt       # Python dependencies
```

## 🔒 Privacy & Security

- **No Network Requests**: All data generated locally
- **No External APIs**: Uses local Faker library
- **Local Storage Only**: Data saved to your device
- **No Telemetry**: No usage tracking or data collection
- **Open Source**: Full source code available for review

## 🌟 Use Cases

- **Web Development**: Test forms and user interfaces
- **Privacy Protection**: Avoid giving real data to websites
- **QA Testing**: Generate test data for applications
- **Demonstrations**: Create realistic demos without real data
- **Education**: Teaching about data privacy and security

## 🤝 Contributing

This tool is designed to help people maintain privacy online. Contributions are welcome and encouraged!

### Quick Contributing Guide
1. **Fork** the repository on GitHub
2. **Clone** your fork: `git clone https://github.com/manalsiddiqui/offline-fake-data-generator.git`
3. **Set up** development environment: `./setup.sh`
4. **Create** a feature branch: `git checkout -b feature/amazing-feature`
5. **Make** your changes and test them
6. **Commit** with conventional format: `git commit -m "feat: add amazing feature"`
7. **Push** to your fork: `git push origin feature/amazing-feature`
8. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### 🎯 Areas Needing Help
- Real browser extensions (Chrome/Firefox)
- Additional international locales
- UI/UX improvements
- Documentation and tutorials
- Testing and bug reports

## 🌟 Support the Project

If this tool helps you maintain privacy online:
- ⭐ **Star** the repository on GitHub
- 🐛 **Report bugs** and suggest features
- 📝 **Contribute code** or documentation  
- 📢 **Share** with others who value privacy

## ⚖️ Legal Notice

This tool is for legitimate testing and privacy purposes only. Use responsibly and in accordance with applicable laws and website terms of service.

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Faker](https://faker.readthedocs.io/) for realistic data generation
- Inspired by the need for better online privacy tools
- Thanks to all contributors who help make the internet more privacy-friendly

---

**🛡️ Stay private, stay safe! Help others do the same by contributing to this project.** 