# Contributing to Offline Fake Data Generator

Thank you for your interest in contributing to the Offline Fake Data Generator! This project aims to help people maintain privacy online while providing developers with realistic test data.

## 🚀 Quick Start for Contributors

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/offline-fake-data-generator.git
   cd offline-fake-data-generator
   ```
3. **Set up the development environment**:
   ```bash
   ./setup.sh
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 How to Contribute

### 🐛 Bug Reports
- Use the GitHub issue tracker
- Include steps to reproduce the bug
- Mention your operating system and Python version
- Provide error messages if any

### ✨ Feature Requests
- Check existing issues first to avoid duplicates
- Clearly describe the use case and expected behavior
- Consider privacy implications of any new features

### 🔧 Code Contributions
- Follow PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed
- Ensure all existing tests pass

## 🏗️ Development Setup

### Prerequisites
- Python 3.7 or higher
- Virtual environment support

### Setup Steps
```bash
# Clone and enter directory
git clone <your-fork-url>
cd offline-fake-data-generator

# Run setup script
./setup.sh

# Activate virtual environment
source venv/bin/activate

# Test installation
python demo.py
```

## 🧪 Testing

### Running Tests
```bash
# Activate virtual environment
source venv/bin/activate

# Run comprehensive demo
python demo.py

# Test CLI functionality
python cli.py generate --save
python cli.py list

# Test web server (in separate terminal)
python run.py web
# Visit http://localhost:5000
```

### Manual Testing Checklist
- [ ] CLI generates and saves personas
- [ ] Seeded generation is reproducible
- [ ] Web interface loads and functions
- [ ] Browser extension popup works
- [ ] Export formats (JSON, YAML, CSV) work
- [ ] Data persistence across sessions

## 📦 Project Structure

```
├── fake_data_generator.py  # Core generation engine
├── cli.py                  # Command line interface
├── web_server.py          # Flask web server
├── run.py                 # Main launcher script
├── demo.py                # Comprehensive demo
├── templates/             # Web interface templates
├── fake_data/             # Data storage directory
├── requirements.txt       # Python dependencies
├── setup.sh              # Setup script
└── README.md             # Main documentation
```

## 🎯 Contribution Areas

### High Priority
- **Browser Extension**: Real browser extension (Chrome/Firefox)
- **Additional Locales**: Support for more countries/languages
- **Form Detection**: Automatic form field detection and filling
- **Data Quality**: More realistic data generation
- **Performance**: Optimize generation speed

### Medium Priority
- **UI/UX Improvements**: Better web interface design
- **Export Formats**: Additional export options (XML, SQLite)
- **Import Features**: Import existing personas
- **Batch Operations**: Generate multiple personas at once
- **Security Hardening**: Additional privacy protections

### Documentation
- **Tutorials**: Step-by-step guides for common use cases
- **API Documentation**: Detailed API reference
- **Video Demos**: Screen recordings of usage
- **Translations**: README in other languages

## 📋 Code Style Guidelines

### Python Code
- Follow PEP 8
- Use type hints where appropriate
- Add docstrings to all functions and classes
- Keep functions focused and small
- Use meaningful variable names

### Web Frontend
- Use semantic HTML
- Mobile-responsive design
- Accessible interfaces (ARIA labels, etc.)
- Progressive enhancement

### Commit Messages
Use conventional commit format:
```
feat: add new locale support for German
fix: resolve port conflict in web server
docs: update installation instructions
test: add tests for seeded generation
```

## 🔒 Privacy & Security Considerations

This project prioritizes user privacy. When contributing:

- **No Network Calls**: Ensure all data generation remains offline
- **Local Storage Only**: Data should never leave the user's device
- **No Telemetry**: No usage tracking or analytics
- **Minimal Dependencies**: Avoid unnecessary external libraries
- **Security Review**: Consider security implications of changes

## 🤝 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different opinions and approaches
- Remember this project serves privacy-conscious users

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Wiki**: For additional documentation

## 🏷️ Release Process

1. Update version in relevant files
2. Update CHANGELOG.md
3. Create pull request to main branch
4. After merge, create GitHub release with tag
5. Update documentation if needed

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- GitHub releases
- Project documentation

Thank you for helping make the internet a more privacy-friendly place! 🛡️ 