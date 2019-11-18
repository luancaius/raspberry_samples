import argparse
import warnings
import datetime
import json
import time
import cv2

cap = cv2.VideoCapture('/samples/video10.h264')

motionCounter = 0
delta_thresh=5
blur_size=[21, 21]
min_motion_frames=8
camera_warmup_time=10
min_area=5000
while(cap.isOpened()):
	timestamp = datetime.datetime.now()
  	ret, frame = cap.read()

	# resize the frame, convert it to grayscale, and blur it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, blur_size, 0)

	# accumulate the weighted average between the current frame and
	# previous frames, then compute the difference between the current
	# frame and running average
	frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
	cv2.accumulateWeighted(gray, avg, 0.5)

	# threshold the delta image, dilate the thresholded image to fill
	# in holes, then find contours on thresholded image
	thresh = cv2.threshold(frameDelta, delta_thresh, 255,
		cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=2)
	im2 ,cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < min_area:
			continue

		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		save_ps	

	# check to see if the room is occupied
	if save_picture:
		cv2.imwrite("/frames/img{}.jpg".format(motionCounter), frame)
        
	# otherwise, the room is not occupied
	else:
		motionCounter = 0

	cv2.imshow("Security Feed", frame)
	key = cv2.waitKey(1) & 0xFF

	if debug_mode:
		cv2.imshow('Debug blurred gray frame', gray)
		cv2.imshow('Debug threshold frame', thresh)

	if key == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()