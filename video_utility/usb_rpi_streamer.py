import os
import signal
import subprocess
import sys
import time

import yaml

config_path = os.path.join(os.environ["HOME"], "rtc_robotics", "config", "robot_params.yaml")
with open(config_path, "r") as file:
    config = yaml.safe_load(file)

STREAM_PORT = config["configuration"]["STREAM_PORT"]
STREAM_TARGET = config["configuration"]["STREAM_TARGET"]

cmd = (
    "gst-launch-1.0 -e -v "
    "v4l2src device=/dev/video0 ! videoconvert ! videoscale ! "
    "video/x-raw,width=640,height=480,framerate=30/1 ! "
    "x264enc tune=zerolatency bitrate=2000 speed-preset=superfast ! "
    "h264parse ! rtph264pay pt=96 ! "
    f"udpsink port={STREAM_PORT} host={STREAM_TARGET} sync=false"
)

process = None


def signal_handler(sig, frame):
    print("\nStopping stream...")
    if process is not None and process.poll() is None:
        process.terminate()
        process.wait()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

print(f"videostream port: {STREAM_PORT}")
print(f"videostream target: {STREAM_TARGET}")
print(f"rpi_stream started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print(cmd)

process = subprocess.Popen(cmd, shell=True)
returncode = process.wait()
print(f"gst exit code: {returncode}")
if returncode != 0:
    sys.exit(returncode)
