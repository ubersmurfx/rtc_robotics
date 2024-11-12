# Rover and Student robotic systems
Ссылка на актуальный репозиторий проекта: [rtc_robotics](https://github.com/ubersmurfx/rtc_robotics/)

# Содержание
1. Работа с пультом (Ubuntu 22.04)
2. Управление роботом
3. Работа с РТК (Ровер)

# Настройка пульта
Пульт - управляющий компьютер или ноутбук с предустановленной ОС Ubuntu 22.04.
- Ubuntu 22.04 - операционная система [Download ubuntu](https://releases.ubuntu.com/22.04/)
- RealVNC - удаленный рабочий стол [Download RealVNC](https://www.realvnc.com/en/)
- VS Code - универсальное IDE [Download VS Code](https://code.visualstudio.com)
Для настройки соединения по ssh-протоколу (пульт и робот находятся в одной сети, т.е. подключены
к роутеру) необходимо ввести следующую команду:
```
ssh  <имя робота>@<ip address>
```
Для запуска python-скрипта необходимо создать виртуальное окружение и установить необходимые зависимости с помощью pip:
```
sudo apt-get update -y
sudo apt-get update -y
sudo apt-get install python3-pip -y
sudo apt-get install python3-dev -y
sudo apt-get install libatlas-base-dev -y
sudo apt-get install gstreamer1.0* -y
sudo apt install libgstreamer1.0-0 -y
sudo apt install gstreamer1.0-tools -y
sudo apt install python3-venv -y
cd ~
python3 -m venv venv_rtc_rover
```
Клонируем удаленный репозиторий на пульт:
```
git clone -b rev_2.0_B https://github.com/ubersmurfx/rtc_robotics.git
```
Устанавливаем необходимые зависимости для работы:
```
source ~/venv_rtc_rover/bin/activate
cd rtc_robotics/
pip install pyyaml
pip install numpy
pip install pynput
```
Для удобства команду source можно добавить в bashrc.
Каждый робот имеет свой IP адрес в локальной сети роутера, поэтому на пульте необходимо задать эти параметры:
- IP адрес робота, который необходимо настроить находится в файле rtc_robotics/config/pult_params.yaml 
(HOST - здесь указываем IP адрес робота)
- Путь к конфигурационному файлу пульта rtc_robotics/pult_ws/onpult.py
```
with open('/home/{USERNAME}/rtc_robotics/config/pult_params.yaml', 'r')
```
- Путь к конфигурационному файлу пульта rtc_robotics/video_utility/rpi_reciever.py
```
with open('/home//{USERNAME}/rtc_robotics/config/robot_params.yaml', 'r')
```
# Управление роботом
Подключите пульт к WIFI-роутеру.
Для приема видеопотока с робота:
```
cd ~
source ~/venv_rtc_rover/bin/activate
cd rtc_robotics/video_utility
python3 rpi_reciever.py
```
Для управления роботом:
```
cd ~
source ~/venv_rtc_rover/bin/activate
cd rtc_robotics/pult_ws
python3 onpult.py
## Управление движением роботом:
- w – движение вперед;
- s – двжиение назад;
- a – танковый поворот налево;
- d – танковый поворот направо;
- q – поворот налево;
- e – поворот направо;
- r - нулевое положение;
- t - колеса ромбом.
## Управлением камерой:
- 1 – поднять камеру;
- 2 – опустить камеру.
## Управление скоростью моторов:
- z – замедлиться;
- x – ускориться.
## Управление манипулятором:
- u, h – управление первым звеном манипулятора;
- i, j – управление вторым звеном манипулятора;
- o, k – управление третьим звеном манупулятора;
- p, l - управление четвертым манупулятора;
- g, y – управление схватом. 
## Управление фарой:
- v, b – включить и выключить фару.
```
# Работа с РТК (Ровер)
- Необходимое ПО на роботе запускается автоматически при подключении к роутеру (с совпадающим номером).
- В случае ошибок, потери связи и иных обстоятельств робот перезапускается автоматически в течении 10-15 секунд.
- К роботу можно подключаться после того как появился логотип ЦНИИ РТК на дисплее.

# Особенности работы
Важно отметить, что испольняемый файл *onpult.py* (на пульте) должен запускаться только после включения робота. 
В другом случае соединение не будет установлено.
