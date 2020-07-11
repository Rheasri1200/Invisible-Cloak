import cv2
import numpy as np
import time
import argparse


print("""
Harry :  Hey !! Ms Riya Would you like to try my invisibility cloak ??
         Its awesome !!
        
         be Ready to get Invisible  Thanks For watching .....................
    """)
cap = cv2.VideoCapture(0)


time.sleep(3)
count = 0
background=0


for i in range(60):
	ret,background = cap.read()



while(cap.isOpened()):
	ret, img = cap.read()
	if not ret:
		break
	count+=1
	#img = np.flip(img,axis=1)
	
	# Converting the color space from BGR to HSV
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Generating mask to detect red color
	lower_blue = np.array([94, 80, 2])
	upper_blue = np.array([126, 255, 255])
	mask1 = cv2.inRange(hsv,lower_blue,upper_blue)

	lower_red = np.array([130,80,2])
	upper_red = np.array([140,255,255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	mask1 = mask1+mask2

	# Refining the mask corresponding to the detected red color
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
	mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
	mask2 = cv2.bitwise_not(mask1)

	# Generating the final output
	res1 = cv2.bitwise_and(background,background,mask=mask1)
	res2 = cv2.bitwise_and(img,img,mask=mask2)
	final_output = cv2.addWeighted(res1,1,res2,1,0)

	cv2.imshow('Magic !!!',final_output)
	k = cv2.waitKey(10)
	if k == 27:
		break
cv2.destroyAllWindows() 

