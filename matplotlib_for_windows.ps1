# Create a virtual environment for managing dependencies
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install numpy matplotlib

# Run code for matplotlib
python main.py $args