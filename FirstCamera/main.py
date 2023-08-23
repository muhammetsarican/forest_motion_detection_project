from Libs import cv2
from ImageGetter import getImage
from EnvVariableGetter import getVar
class fCamera:
    path=getVar("FIRST_IMAGE_PATH")
    def __init__(self):
        self.frame=getImage(self.path)
        cv2.imshow("First Camera", self.frame)
        cv2.waitKey(0)
        
    def destroyAll():
        cv2.destroyAllWindows()