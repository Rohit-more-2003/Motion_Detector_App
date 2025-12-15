import time
from copyreg import constructor

import cv2

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None # Initial frame to compare with other frames
while True:
	check, frame = video.read()
	
	# Change the colored frame to grayscale
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Apply the blur as we don't need much precision.
	gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
	
	#cv2.imshow("My video", gray_frame_gau)
	if first_frame is None:
		first_frame = gray_frame_gau
		
	# Difference between current and first frame
	delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
	#cv2.imshow("My video", delta_frame)
	#print(delta_frame)
	
	# Make the frame black and white sensitive
	# Apply threshold for the pixel change
	thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
	# Apply dilation to the threshold_frame
	dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
	cv2.imshow("My video", dil_frame)
	
	# Check contours around white area
	# That is check for contours where there is fake object but still shows whites in dil_frame
	contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	for contour in contours:
		# Check fake object in frame
		if cv2.contourArea(contour) < 5000:
			continue
			
		# Get x,y coordinates of right upper of rectangle
		# and also width and height of rectangle
		x, y, w, h = cv2.boundingRect(contour)
		
		# Apply the rectangle to specified(here original) frame
		# Specify (coordinates of right upper point), (width and height), (border color of rectangle)
		#
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
		
	cv2.imshow("Video", frame)
	# As shadows changes while moving so more rectangle were shown than necessary
	key = cv2.waitKey(1)
	
	if key == ord('q'):
		break
		
video.release()