#!/bin/bash

cp rpi_streamer.service /etc/systemd/system
cp robot_controller.service /etc/systemd/system

sudo systemctl daemon-reload

sudo systemctl enable rpi_streamer.service
sudo systemctl enable robot_controller.service

echo "___________________________________________________"
cat /etc/systemd/system/rpi_streamer.service
echo "___________________________________________________"
cat /etc/systemd/system/robot_controller.service 
echo "___________________________________________________"

echo "Сервис rpi_streamer.service успешно добавлен и включен."