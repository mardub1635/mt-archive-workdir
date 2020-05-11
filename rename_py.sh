#!/bin/bash
sleep 1
xdotool key shift+F10
sleep 1
xdotool key Up Up Up Up Up Return
sleep 2
xdotool type ../rename_py_suite.sh
xdotool key Return
xdotool type code
xdotool key space
xdotool type .
xdotool key Return
sleep 3
xdotool key alt+Tab
sleep 2
xdotool key alt+F4

