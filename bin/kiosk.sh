#!/bin/bash

LOG_FILE="/var/log/rx8/boot.log"

# Activate the virtual environment and run Python app
source /home/pi/.venv/bin/activate >> "$LOG_FILE" 2>&1
/home/pi/.venv/rx8/bin/python3 /home/pi/rx8/main.py >> "$LOG_FILE" 2>&1 &
sEv7-Hvfgssd@wp