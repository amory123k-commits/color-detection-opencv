import os
import cv2
import numpy as np

def get_limits(color):
    c=np.uint8([[color]])
    #convert the color from BGR to HSV
    hsvc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    #define the lower and upper limit of the color in HSV
    lower_limit=np.array([hsvc[0][0][0]-10,100,100])
    upper_limit=np.array([hsvc[0][0][0]+10,255,255])


    # convert the lower and upper limit to uint8 to accerpt the input in cv2.inRange function
    lower_limit=np.array(lower_limit,dtype=np.uint8)
    upper_limit=np.array(upper_limit,dtype=np.uint8)


    return lower_limit,upper_limit

