#!/bin/bash

source /home/pi/.venv/bin/activate >> dev/null 2>&1
$(which python3) -m rx8
