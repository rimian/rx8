#!/bin/sh

python -m venv ~/.venv/rx8
source ~/.venv/rx8/bin/activate
pip install flask
git clone https://github.com/rimian/rx8.git .
