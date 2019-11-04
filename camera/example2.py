import picamera
import time
from datetime import datetime

camera = picamera.PiCamera()
interval=30
continueCapture = True
start=datetime(2019, 11, 3,19,44)
end=datetime(2019, 11, 3,20,10)
timeStart = start.timestamp()
timeEnd = end.timestamp()

index=0

while continueCapture:
    now=datetime.now()
    index+=1
    print('video ',index,' - ', now)
    camera.start_recording('videos/video{}.h264'.format(index))
    time.sleep(interval)
    camera.stop_recording()    
    timestamp = now.timestamp()
    diffStart = timestamp-timeStart
    diffEnd = timeEnd-timestamp
    
    if diffStart > 0 and diffEnd > 0:
        continueCapture = True
    else:
        continueCapture = False
print('Program finished!')
