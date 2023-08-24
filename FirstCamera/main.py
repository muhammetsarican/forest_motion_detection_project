from Libs import cv2
from ImageGetter import getImage
from EnvVariableGetter import getVar
from DetectObjectLibs import *
class fCamera:
    path=getVar("FIRST_IMAGE_PATH")
    def __init__(self):
        self.frame=getImage(self.path)
        self.search()
        # cv2.imshow(str(self.frame.shape), self.frame)
        # cv2.waitKey(0)
    
    def search(self):
        SearchObject.SearchOnImage().search(self.frame)
    def destroyAll():
        cv2.destroyAllWindows()