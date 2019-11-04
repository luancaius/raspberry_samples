import picamera
import time
from datetime import datetime

camera = picamera.PiCamera()
interval=30
continueCapture = True
start=datetime(2019, 11, 3,19,44)
end=datetime(2019, 11, 3,19,52)
timeStart = start.timestamp()
timeEnd = end.timestamp()

index=0

while continueCapture:
    now=datetime.now()
    index+=1
    print('video ',index,' - ', now)
    camera.start_recording('video{}.mp4'.format(index))
    time.sleep(interval)
    camera.stop_recording()    
    timestamp = now.timestamp()
    diffStart = timestamp-timeStart
    diffEnd = timeEnd-timestamp
    print(diffStart," | ", diffEnd)
    if diffStart > 0 and diffEnd > 0:
        continueCapture = True
    else:
        continueCapture = False
print('Program finished!')