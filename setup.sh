#!/bin/bash
# Setup script for Offline Fake Data Generator on macOS

echo "🎭 Offline Fake Data Generator - Setup"
echo "======================================"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found"
    echo "Install Python 3 with: brew install python"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Test installation
echo "🧪 Testing installation..."
python -c "
from fake_data_generator import FakeDataGenerator
generator = FakeDataGenerator()
persona = generator.generate_persona()
print(f'✅ Test successful - Generated: {persona[\"name\"]}')
"

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "🚀 To use the fake data generator:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Then run:"
echo "   python run.py web        # Start web server"
echo "   python run.py generate   # Quick generate"
echo "   python run.py help       # Show help"
echo ""
echo "🌐 Web interface: http://localhost:5000"
echo "🎯 Browser extension: http://localhost:5000/extension"
echo ""
echo "💡 To deactivate virtual environment later: deactivate" 