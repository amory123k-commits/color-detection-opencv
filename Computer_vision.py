import numpy as np
import cv2
from PIL import Image
#usung get_limits from util.py
from util import get_limits

#define the color to be detected in BGR format
color=np.array([51,153,255])


#initialize the defualt webcam
webcam=cv2.VideoCapture(0)
# get the lower and upper limit from method get_limits
lower_limit,upper_limit=get_limits(color)

while True:
    ret,frame=webcam.read()
    
    
    if not ret:
        break
    else:
        image_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(image_hsv,lower_limit,upper_limit)

        mask_=Image.fromarray(mask)
        box=mask_.getbbox()
        
        if box is not None:
            x1,y1,x2,y2=box
            #drawing a rectangle around the detected color 
            frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        
        
        cv2.imshow("Webcam",frame)
        cv2.imshow("Mask",mask)
        #press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
        
        
#release the webcam and close all windows
cv2.destroyAllWindows()      

    


