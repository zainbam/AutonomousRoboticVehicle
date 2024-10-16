import cv2

frame = cv2.imread('right_image1.png')                    
          
cv2.circle(frame, (363, 192), 5, (255, 255, 0), -1)
cv2.imshow("frame left", frame)
cv2.waitKey()
