# Virtual Environments in Python (venv)
# A virtual environment carries your entire Python installation
# into a folder at the chosen path.
# When you activate a virtual environment, that environment's
# Python installation will be used.
# venv is the module we will use to
# create virtual environments.
# You can name your virtual environment as you wish,
# but the most common names are:
# venv env .venv .env
#
# How to create virtual environments
# Open your project folder in the terminal
# and type:
# python -m venv venv
#
# Activating and deactivating the virtual environment
# Windows: .\venv\Scripts\activate
# Linux and Mac: source venv/bin/activate
# Deactivate: deactivate
#
# pip - installing packages and libraries
# Install latest version:
# pip install package_name
# Install specific version
# (there are other methods as well not mentioned here)
# pip install package_name==0.0.0
# Uninstall a package
# pip uninstall package_name
# Freeze (list installed packages)
# pip freeze
#
# Creating and using a requirements.txt
# pip freeze > requirements.txt
# Installing everything from requirements.txt
# pip install -r requirements.txt
