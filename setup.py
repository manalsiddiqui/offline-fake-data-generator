#!/usr/bin/env python3
"""
Setup script for Offline Fake Data Generator
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

# Read requirements
def read_requirements():
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='offline-fake-data-generator',
    version='1.0.0',
    author='Offline Fake Data Generator Contributors',
    author_email='',
    description='A comprehensive tool for generating realistic fake personal information offline',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/YOUR_USERNAME/offline-fake-data-generator',
    
    # Package discovery
    packages=find_packages(),
    py_modules=[
        'fake_data_generator',
        'cli',
        'web_server',
        'run',
        'demo'
    ],
    
    # Include additional files
    include_package_data=True,
    package_data={
        '': ['templates/*.html', 'requirements.txt', 'README.md', 'LICENSE']
    },
    
    # Dependencies
    install_requires=read_requirements(),
    
    # Python version requirement
    python_requires='>=3.7',
    
    # Entry points for command-line scripts
    entry_points={
        'console_scripts': [
            'fake-data-gen=run:main',
            'fake-data-cli=cli:cli',
        ],
    },
    
    # Classification
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Testing',
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Environment :: Web Environment',
    ],
    
    # Keywords for PyPI
    keywords=[
        'fake-data', 'privacy', 'testing', 'generator', 'offline', 
        'personas', 'forms', 'browser', 'cli', 'web', 'security'
    ],
    
    # Project URLs
    project_urls={
        'Bug Reports': 'https://github.com/YOUR_USERNAME/offline-fake-data-generator/issues',
        'Source': 'https://github.com/YOUR_USERNAME/offline-fake-data-generator',
        'Documentation': 'https://github.com/YOUR_USERNAME/offline-fake-data-generator/wiki',
        'Changelog': 'https://github.com/YOUR_USERNAME/offline-fake-data-generator/blob/main/CHANGELOG.md',
    },
    
    # License
    license='MIT',
    
    # Additional metadata
    zip_safe=False,
) 