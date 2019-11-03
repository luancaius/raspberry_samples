import picamera
import time

camera = picamera.PiCamera()

camera.start_recording('example1.h264')
time.sleep(30)
camera.stop_recording()