#!/bin/bash

# First create a python virtual environment
python3 -m venv ./env

# Enable the environment
source env/bin/activate

# Install the required python dependencies for the application
python3 -m pip install -r requirements.txt

# Exit the virtual environment
deactivate