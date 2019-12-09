import picamera
import time
from datetime import datetime
import cv2 
import picamera.array

time.sleep(0.1)

interval=30
continueCapture = True
start=datetime(2019, 12, 8,21,40)
end=datetime(2019, 12, 8,21,45)
timeStart = start.timestamp()
timeEnd = end.timestamp()

index=0

prevImage = None
with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:

        while continueCapture:
            now=datetime.now()
            timestamp = now.timestamp()
            diffStart = timestamp-timeStart
            diffEnd = timeEnd-timestamp
            
            if diffStart > 0:
                index+=1
                camera.capture(stream, 'bgr', use_video_port=True)
                # stream.array now contains the image data in BGR order
                # cv2.imshow('frame', stream.array)

                cv2.imwrite('{}.png'.format(now), stream.array)
                # reset the stream before the next capture
                stream.seek(0)
                stream.truncate()

            
            if diffEnd > 0:
                continueCapture = True
            else:
                continueCapture = False
print('Program finished!')
