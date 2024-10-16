
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Functions
import face_R
import triangulation as tri


# Open both cameras
cap_right = cv2.imread('right_image1.png')                    
cap_left =  cv2.imread('left_image1.png')

frame_rate = 120    #Camera frame rate (maximum at 120 fps)

B = 9               #Distance between the cameras [cm]
f = 6               #Camera lense's focal length [mm]
alpha = 56.6        #Camera field of view in the horisontal plane [degrees]

frame_right = cap_right
frame_left = cap_left


circles_right = face_R.fface(frame_right)
circles_left  = face_R.fface(frame_left,)

    # If no face can be caught in one camera show text "TRACKING LOST"
if np.all(circles_right) == None or np.all(circles_left) == None:
    cv2.putText(frame_right, "TRACKING LOST", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
    cv2.putText(frame_left, "TRACKING LOST", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)

else:
    # Function to calculate depth of object. Outputs vector of all depths in case of several faces.
    depth = tri.find_depth(circles_right, circles_left, frame_right, frame_left, B, f, alpha)

    cv2.putText(frame_right, "TRACKING", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
    cv2.putText(frame_left, "TRACKING", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
    cv2.putText(frame_right, "Distance(cm): " + str(round(depth*205.8,3)), (200,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
    cv2.putText(frame_left, "Distance(cm): " + str(round(depth*205.8,3)), (200,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0),2)
    # Multiply computer value with 205.8 to get real-life depth in [cm]. The factor was found manually.
    print("Depth: ", depth*205.8)                                            


    # Show the frames
cv2.circle(frame_left, circles_left, 5, (255, 255, 0), -1)
    # print("point: ", circles_left)                                            

cv2.imshow("frame right", frame_right) 
cv2.imshow("frame left", frame_left)
    # Hit "q" to close the window
cv2.waitKey()


cv2.destroyAllWindows()