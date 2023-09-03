from Libs import cv2, load_model, numpy as np, convolve
from DetectObject.Components import ModelProcess
from EnvVariableGetter import getVar
from DataProcess import data
from DetectObject.Components import FrameSchema, MarkTheObject
import random
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
                framePart=self.cam.frame[heightStart:heightEnd, widthStart:widthEnd, :]
                
                # self.littleFrames(framePart)
                self.cornerDetection(framePart)
                imgClass, ratio=self.findClass(self.imageProcess(framePart))# [heightStart:heightEnd, widthStart:widthEnd]
                break
            break
                # if imgClass=="sheep" or ratio>0.99:
                    # MarkTheObject.markObject(self.cam.frame, FrameSchema.Frame("image", imgClass, widthStart, widthEnd, heightStart, heightEnd), ratio)
        cv2.imshow("frame2", framePart)
        cv2.waitKey(0)
        # cv2.imshow("frame2", self.cam.frame)
        # cv2.waitKey(0)
    # def searchInBox()
    def imageProcess(self, frame):
        frame=cv2.resize(frame, (128, 128))
        # frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame=frame/255
        frame=frame.reshape(1, 128, 128, 3)
        return self.ModelProcessObj.predict(frame)
                
    def findClass(self, predictObject):
        predictList=predictObject[0].tolist()
        predictedIndex, predictedRatio=predictList.index(max(predictList)), max(predictList)
        print(self.classes[predictedIndex], predictedRatio)
        return self.classes[predictedIndex], float(predictedRatio)

    def cornerDetection(self, frame):
        erodedFrame=cv2.erode(frame, (np.ones((15, 15),np.uint8)),iterations=1)
        dilatedFrame=cv2.dilate(frame, (np.ones((15, 15), np.uint8)), iterations=1)
        	
        canniedFrame = cv2.Canny(frame, threshold1=30, threshold2=100)
        
        cv2.imshow("eroded", erodedFrame)
        cv2.imshow("dilated", dilatedFrame)
        cv2.imshow("canny", canniedFrame)

    def littleFrames(self, frame):
        # widthParts=[32, 64, 96, 128]
        foundPoints=[]
        widthHeightParts=[16, 32, 64]
        frameHeight, frameWidth, _=frame.shape
        for parts in widthHeightParts[::-1]:
            randomColor=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            for heightStart in range(0,frameHeight,parts):
                for widthStart in range(0,frameWidth,parts):
                    littleFramePart=frame[heightStart:heightStart+parts, widthStart:widthStart+parts, :]
                    imgClass, ratio=self.findClass(self.imageProcess(littleFramePart))
                    # if imgClass=="sheep":
            #             cv2.rectangle(frame, (widthStart, heightStart), (widthStart+30, heightStart+30), (0, 255, 0), 1)
            # for heightEnd in heightParts:
            #     for widthEnd in widthParts:
            #         littleFramePart=frame[0:heightEnd, 0:widthEnd, :]
            #         imgClass, ratio=self.findClass(self.imageProcess(littleFramePart))
                    if imgClass!="fire":
                        cv2.rectangle(frame, (widthStart, heightStart), (widthStart+parts, heightStart+parts), randomColor, 1)
                        foundPoints.append({
                            "widthStart":widthStart,
                            "heightStart":heightStart,
                            "widthStart+parts":widthStart+parts,
                            "heightStart+parts":heightStart+parts,
                        })
        cv2.imshow("frame2", frame)
        cv2.waitKey(0)
        print(foundPoints)
        print([minWidthStart["widthStart"] for minWidthStart in foundPoints if minWidthStart["heightStart"]==32])