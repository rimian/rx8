#!/bin/bash

LOG_FILE="/home/pi/rx8/boot.log"

cd /home/pi/rx8 >> "$LOG_FILE" 2>&1 &
source /home/pi/.venv/rx8/bin/activate >> "$LOG_FILE" 2>&1
/home/pi/.venv/rx8/bin/python3 main.py >> "$LOG_FILE" 2>&1 &
