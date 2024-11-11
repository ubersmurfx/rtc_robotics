#!/bin/bash


sudo apt install python3-venv -y
if [[ $? -ne 0 ]]; then
    echo "Error in sudo apt install python3-venv"
    exit 1
fi