import picamera
import time
from datetime import datetime

camera = picamera.PiCamera()
continueCapture = True
start=datetime.datetime(2019, 11, 3,19,31)
end=datetime.datetime(2007, 11, 3,19,40)
timeStart = datetime.timestamp(start)
timeEnd = datetime.timestamp(end)

index=0

while continueCapture:
    now=datetime.now()
    index+=1
    print('video {} - {}', index, now)
    camera.start_recording('video{}.mp4'.format(index))
    time.sleep(30)
    camera.stop_recording()    
    timestamp = datetime.timestamp(now)
    if timestamp-timeStart > 0 and timeEnd-timestamp > 0:
        continueCapture = True
    
