import picamera
import time
from datetime import datetime
import cv2 
import picamera.array

time.sleep(0.1)

interval=30
continueCapture = True
start=datetime(2019, 12, 8,23,10)
end=datetime(2019, 12, 8,23,13)
timeStart = start.timestamp()
timeEnd = end.timestamp()

index=0
threshold=100

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
                currentImage=stream.array
                delta=calculateDelta(currentImage,prevImage)
                if delta > threshold:
                    cv2.imwrite('videos2/{}.png'.format(now), stream.array)
                prevImage = currentImage
                stream.seek(0)
                stream.truncate()

            
            if diffEnd > 0:
                continueCapture = True
            else:
                continueCapture = False
print('Program finished!')

def calculateDelta(currentImage, prevImage):
    if prevImage is None:
        return 0
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
    print(err)
    return 90