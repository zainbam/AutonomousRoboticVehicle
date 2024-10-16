import cv2
print(cv2.__version__)
from matplotlib import pyplot as plt
width=758
height=572

class mpFace:
    topLeft=None

    import mediapipe as mp 
    def __init__(self):
        self.myFace=self.mp.solutions.face_detection.FaceDetection()
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myFace.process(frameRGB)
        faceBoundBoxs=[]
        topLeft=None

        if results.detections != None:
            for face in results.detections:
                bBox=face.location_data.relative_bounding_box
                topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
                bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
                faceBoundBoxs.append((topLeft,bottomRight))
        return faceBoundBoxs

def fface(frame):
    out = None
    # img = cv2.imread('right_image1.png')  
    # frame=cv2.resize(frame,(width,height))
    x=None
    wi=None
    hi=None
    findFace=mpFace()
    faceLoc=findFace.Marks(frame)
    for face in faceLoc:
        x=face[0]
        wi=face[1][0]-face[0][0]
        hi=face[1][1]-face[0][1]
        cv2.rectangle(frame,face[0],face[1],(255,0,0),3)
    out=(int(x[0]+wi/2),int(x[1]+hi/2))
    print("point: ", out)                                            


    return out

        



# cv2.imshow("frame left", img) 
# cv2.waitKey()

# # plt.imshow("frame left", img)
# cv2.destroyAllWindows()

