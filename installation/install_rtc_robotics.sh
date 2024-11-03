#!/bin/bash

sudo apt-get update -y
if [[ $? -ne 0 ]]; then
    echo "Error in apt update"
    exit 1
fi

sudo apt-get full-upgrade -y
if [[ $? -ne 0 ]]; then
    echo "Error in apt upgrade"
    exit 1
fi

sudo apt-get install python3-pip -y
if [[ $? -ne 0 ]]; then
    echo "Error in apt install python3-pip"
    exit 1
fi

sudo apt-get install python3-dev -y
if [[ $? -ne 0 ]]; then
    echo "Error in sudo apt-get install python-dev"
    exit 1
fi

sudo apt-get install libatlas-base-dev -y
if [[ $? -ne 0 ]]; then
    echo "Error in sudo apt-get install libatlas-base-dev"
    exit 1
fi

sudo apt install python3-venv -y
if [[ $? -ne 0 ]]; then
    echo "Error in sudo apt install python3-venv"
    exit 1
fi

sudo apt install gedit -y
if [[ $? -ne 0 ]]; then
    echo "Error in apt install gedit"
    exit 1
fi

sudo apt-get install gstreamer1.0* -y
if [[ $? -ne 0 ]]; then
    echo "Ошибка при установке gstreamer1.0*. Скрипт остановлен."
    exit 1
fi

sudo apt install libgstreamer1.0-0 -y
if [[ $? -ne 0 ]]; then
    echo "sudo apt install libgstreamer1.0-0"
    exit 1
fi

sudo apt install gstreamer1.0-tools -y
if [[ $? -ne 0 ]]; then
    echo "sudo apt install gstreamer1.0-tools"
    exit 1
fi


echo "Установка завершена успешно."