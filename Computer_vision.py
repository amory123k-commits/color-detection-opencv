import numpy as np
import cv2
from PIL import Image
from collections import deque
# using get_limits from util.py
from util import get_limits

# define the color to be detected in BGR format
color=np.array([51,153,255])


# initialize the defualt webcam
webcam=cv2.VideoCapture(0)
# get the lower and upper limit from method get_limits
lower_limit,upper_limit=get_limits(color)
# create queue to calc last 5 avg positions to improve time complexity 

positions=deque(maxlen=5)
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
            positions.append(box)
            if len(positions)==5:
                # calculate average of last 5 positions (Smooth rectangle)
                avg_x1=sum(p[0] for p in positions)//5
                avg_y1=sum(p[1] for p in positions)//5
                avg_x2=sum(p[2] for p in positions)//5
                avg_y2=sum(p[3] for p in positions)//5
            #drawing a rectangle around the detected color 
                frame = cv2.rectangle(frame,(avg_x1,avg_y1),(avg_x2,avg_y2),(0,255,0),2)
            else:
                x1,y1,x2,y2=box
                frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0, 255, 0), 2)
        else:
            # when is color disappear
            positions.clear()
        
        
        cv2.imshow("Webcam",frame)
        cv2.imshow("Mask",mask)
        #press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
        
        
#release the webcam and close all windows
webcam.release()
cv2.destroyAllWindows()      

    

