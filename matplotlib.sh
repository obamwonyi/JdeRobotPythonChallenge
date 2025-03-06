#!/bin/bash
# Create a virtual environment for managing dependencies
python3 -m venv venv
# Sourcing the virtual environment
source venv/bin/activate
# Install dependencies
pip install numpy matplotlib
# Run code for matplotlib
python main.py matplotlib
