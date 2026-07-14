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

def signal_handler(sig, frame):
    print('\nStopping receiver...')
    if process.poll() is None:
        process.terminate()
        process.wait()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print(f"Listening for stream on port: {STREAM_PORT}")
print(f"Receiver started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Прием видео через gst-launch с udpsrc и вывод на экран
cmd = f"gst-launch-1.0 udpsrc port={STREAM_PORT} caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96' ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink sync=false"

process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

try:
    output, error = process.communicate()
except KeyboardInterrupt:
    process.terminate()
    print("\nReceiver stopped")