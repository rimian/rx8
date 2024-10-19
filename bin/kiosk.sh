#!/bin/bash

LOG_FILE="/var/log/rx8/boot.log"

# Activate the virtual environment and run Python app
source /home/pi/.venv/bin/activate >> "$LOG_FILE" 2>&1
$(which python3) /home/pi/rx8/main.py >> "$LOG_FILE" 2>&1 &
