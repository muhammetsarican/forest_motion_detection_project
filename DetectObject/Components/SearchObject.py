from Libs import cv2, load_model
from DetectObject.Components import ModelProcess
from EnvVariableGetter import getVar
from DataProcess import data
from DetectObject.Components import FrameSchema, MarkTheObject
class SearchOnImage:
    def __init__(self, cam):
        self.cam=cam
        self.size=int(getVar("IMAGE_SEARCH_SIZE"))
        print(f"[Info]_Size is {self.size}")
        self.ModelProcessObj=ModelProcess.Model()
        self.classes=data(getVar("CLASS_DATA_PATH")).getFromTxt()

    def search(self):
        frameHeight, frameWidth, _=self.cam.frame.shape
        for heightStart in range(_,frameHeight,self.size):
            for widthStart in range(_,frameWidth,self.size):
                heightEnd=heightStart+self.size
                widthEnd=widthStart+self.size
                imgClass, ratio=self.findClass(self.imageProcess(self.cam.frame[heightStart:heightEnd, widthStart:widthEnd, :]))# [heightStart:heightEnd, widthStart:widthEnd]
                if imgClass=="sheep":
                    MarkTheObject.markObject(self.cam.frame, FrameSchema.Frame("image", imgClass, widthStart, widthEnd, heightStart, heightEnd), ratio)
        cv2.imshow("frame2", self.cam.frame)
        cv2.waitKey(0)
    # def searchInBox()
    def imageProcess(self, frame):
        frame=cv2.resize(frame, (128, 128))
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame=frame/255
        frame=frame.reshape(1, 128, 128, 1)
        return self.ModelProcessObj.predict(frame)
                
    def findClass(self, predictObject):
        predictList=predictObject[0].tolist()
        predictedIndex, predictedRatio=predictList.index(max(predictList)), max(predictList)
        print(self.classes[predictedIndex], predictedRatio)
        return self.classes[predictedIndex], float(predictedRatio)
        