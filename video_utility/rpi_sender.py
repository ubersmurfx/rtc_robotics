import subprocess
import signal
import sys
import yaml
import time
import os

# Загружаем конфиг если есть

config_path = os.path.join(os.environ['HOME'], 'rtc_robotics', 'config', 'robot_params.yaml')
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

STREAM_PORT = config['configuration']['STREAM_PORT']
STREAM_TARGET = config['configuration']['STREAM_TARGET']

def signal_handler(sig, frame):
    print('\nStopping stream...')
    if process.poll() is None:
        process.terminate()
        process.wait()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print(f"videostream port: {STREAM_PORT}")
print(f"videostream target: {STREAM_TARGET}")
print(f"rpi_stream started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Отправка видео через rpicam-vid с пайпом в gst-launch для RTP
cmd = f"rpicam-vid -t 0 --width 640 --height 480 --framerate 30 --codec h264 --inline -o - | gst-launch-1.0 fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host={STREAM_TARGET} port={STREAM_PORT} sync=false"

process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

try:
    output, error = process.communicate()
except KeyboardInterrupt:
    process.terminate()
    print("\nStream stopped")