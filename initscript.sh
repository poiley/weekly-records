#!/bin/bash

set -xe

[ -d ".git/" ] && echo "Searching for git repository." || (exit 1) # Check script is running within repository

echo "Git repository found!" # Success Message

[ -d "env/" ] && echo "Searching for Python3 virtual environemnt." || (python3 -m venv env) # Detect or create virual environment

source $(pwd)"/env/bin/activate" # Activate virtual environment

pip install -r requirements.txt # Install python pips

alias activate=". $(pwd)'/.env/bin/activate'"
