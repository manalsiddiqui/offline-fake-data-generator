#!/usr/bin/env python3
"""
Installation script for the Offline Fake Data Generator
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher required")
        print(f"   Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} detected")
    return True

def install_dependencies():
    """Install required Python packages"""
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing Python dependencies"
    )

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    directories = ['fake_data', 'templates']
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"   Created: {directory}")
    
    print("✅ Directories created")
    return True

def test_installation():
    """Test if installation works"""
    print("🧪 Testing installation...")
    try:
        from fake_data_generator import FakeDataGenerator
        generator = FakeDataGenerator()
        persona = generator.generate_persona()
        print(f"✅ Test successful - Generated: {persona['name']}")
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    print("🎭 Offline Fake Data Generator - Installation")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Create directories
    if not create_directories():
        return 1
    
    # Install dependencies
    if not install_dependencies():
        print("\n💡 Try upgrading pip: python -m pip install --upgrade pip")
        return 1
    
    # Test installation
    if not test_installation():
        return 1
    
    print("\n🎉 Installation completed successfully!")
    print("\n🚀 Quick start:")
    print("   python run.py web        # Start web interface")
    print("   python run.py generate   # Generate fake data")
    print("   python run.py help       # Show help")
    print("\n🌐 Web interface will be available at: http://localhost:5000")
    print("🎯 Browser extension popup at: http://localhost:5000/extension")
    
    return 0

if __name__ == '__main__':
    sys.exit(main()) 