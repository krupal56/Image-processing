#image

import cv2
import numpy as np

def nothing(x):
	pass


cv2.namedWindow('Tracking')
cv2.createTrackbar('LH','Tracking', 0, 255, nothing)
cv2.createTrackbar('LS','Tracking', 0, 255, nothing)
cv2.createTrackbar('LV','Tracking', 0, 255, nothing)
cv2.createTrackbar('UH','Tracking', 255, 255, nothing)
cv2.createTrackbar('US','Tracking', 255, 255, nothing)
cv2.createTrackbar('UV','Tracking', 255, 255, nothing)

while True:
	image =cv2.imread('smarties.png',1)

	hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

	l_h = cv2.getTrackbarPos('LH','Tracking')
	l_s = cv2.getTrackbarPos('LS','Tracking')
	l_v = cv2.getTrackbarPos('LV','Tracking')
	u_h = cv2.getTrackbarPos('UH','Tracking')
	u_s = cv2.getTrackbarPos('US','Tracking')
	u_v = cv2.getTrackbarPos('UV','Tracking')


#boundry of blue color
	l_b = np.array([l_h,l_s,l_v]) #lower bound of blue color
	u_b = np.array([u_h,u_s,u_v]) #upper bound of blue color

#threshold 

	mask = cv2.inRange(hsv,l_b,u_b) 

	result = cv2.bitwise_and(image,image,mask=mask)

	cv2.imshow('image',image)
	cv2.imshow('mask',mask)
	cv2.imshow('result',result)
	
	key = cv2.waitKey(1)
	if key == 27:
		break
cv2.destroyAllWindows()

