#!/bin/bash

cd /home/pi/rx8 2>&1 &
source /home/pi/.venv/rx8/bin/activate 2>&1 &
/home/pi/.venv/rx8/bin/python3 main.py 2>&1 &
