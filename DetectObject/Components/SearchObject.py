from Libs import cv2, load_model
from DetectObject.Components import ModelProcess
from EnvVariableGetter import getVar
class SearchOnImage:
    def __init__(self):
        self.size=int(getVar("IMAGE_SEARCH_SIZE"))
        self.ModelProcessObj=ModelProcess.Model()

    def search(self, frame):
        frameHeight, frameWidth, _=frame.shape
        for height in range(frameHeight):
            for width in range(frameWidth):
                self.imageProcess(frame[height:height+self.size, width:width+self.size, :])# [heightStart:heightEnd, widthStart:widthEnd]
                break
            break

    def imageProcess(self, frame):
        frame=cv2.resize(frame, (self.size, self.size))
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame=frame/255
        frame=frame.reshape(1, self.size, self.size, 1)
        print(self.ModelProcessObj.predict(frame)[0].tolist().index(max(self.ModelProcessObj.predict(frame)[0])))
        