import subprocess
import datetime


now = datetime.datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

command_fast = f"gst-launch-1.0 -v v4l2src device=/dev/video0 ! videoconvert ! videoscale ! video/x-raw,width=1280,height=720,framerate=30/1 ! \
    x264enc tune=zerolatency bitrate=16000000 speed-preset=superfast ! h264parse ! rtph264pay pt=96 ! udpsink port=5000 host=192.168.0.5"

process = subprocess.Popen(command_fast.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("rpi_stream started at: ", formatted_time)

output, error = process.communicate()
print(f"stdout: {output.decode('utf-8')}")
print(f"stderr: {error.decode('utf-8')}")

if process.returncode == 0:
    print("Pipeline completed")
else:
    print(f"Error: {process.returncode}")