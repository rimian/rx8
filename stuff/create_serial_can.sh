#!/bin/bash

DEVICE="/dev/ttyACM0"

# https://github.com/latonita/arduino-canbus-monitor
sudo slcan_attach -f -s4 -o $DEVICE
sudo slcand -S 115200 $DEVICE can0
sudo ifconfig can0 up
