import time
import cv2

#Start the camera
video = cv2.VideoCapture(0) #(x) is the priority camera, ex. primary(0), secondary(1), etc

# check, frame = video.read() #read() captures the images
# print(check)  #returns True if action done, else False
# print(frame)  #returns arrays with pixel colors

#video capture outside loop as it only starts the camera
while True:
	#read methods inside loop as they are used to capture images
	time.sleep(1) #sleep the camera, mentioning before read methods gives camera time to load
	#this also means that we are creating 1 frame per second
	#load speed of given code snippet is slow
	
	check, frame = video.read()
	cv2.imshow("My video", frame)
	
	key = cv2.waitKey(1)
	
	if key == ord('q'):
		break
		
video.release()