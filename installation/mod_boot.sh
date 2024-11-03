#!/bin/bash

sudo sed -i 's/camera_auto_detect=1/camera_auto_detect=0/g' /boot/firmware/config.txt


if grep -q 'start_x=1' /boot/firmware/config.txt; then
    echo "Строка start_x=1 уже существует в файле."
else
    sudo sed -i '$a start_x=1' /boot/firmware/config.txt
fi

echo "Изменения в firmware.config.txt внесены успешно!"
