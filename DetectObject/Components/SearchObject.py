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
                
                self.littleFrames(framePart)
                # imgClass, ratio=self.findClass(self.imageProcess(framePart))# [heightStart:heightEnd, widthStart:widthEnd]
                # if widthStart >200:
                #     self.cornerDetection(framePart)
                # if imgClass!="fire" or ratio>0.99:
                #     MarkTheObject.markObject(self.cam.frame, FrameSchema.Frame("image", imgClass, widthStart, widthEnd, heightStart, heightEnd), ratio)
                # break
            # break
        cv2.imshow("frame2", self.cam.frame)
        cv2.waitKey(0)
        # cv2.imshow("frame2", self.cam.frame)
        # cv2.waitKey(0)
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

    def cornerDetection(self, frame):
        # erodedFrame=cv2.erode(frame, (np.ones((15, 15),np.uint8)),iterations=1)
        # dilatedFrame=cv2.dilate(frame, (np.ones((15, 15), np.uint8)), iterations=1)
        	
        # canniedFrame = cv2.Canny(frame, threshold1=30, threshold2=100)
        
        # cv2.imshow("eroded", erodedFrame)
        # cv2.imshow("dilated", dilatedFrame)
        # cv2.imshow("canny", canniedFrame)
        
        # # gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # # sobel_x= np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        # # sobel_y= np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        
        # # img_sobel_x = convolve(gray, sobel_x, mode='same')
        # # img_sobel_y = convolve(gray, sobel_y, mode='same')
        
        # # gradient_magnitude = np.sqrt(np.square(img_sobel_x) + np.square(img_sobel_y))
        # # cv2.imshow("canny", gradient_magnitude)
        # def gaussian_kernel(size, sigma):
        #     if size % 2 == 0:
        #         size = size + 1

        #     max_point = size // 2  # both directions (x,y) maximum cell start point
        #     min_point = -max_point  # both directions (x,y) minimum cell start point

        #     K = np.zeros((size, size))  # kernel matrix
        #     for x in range(min_point, max_point + 1):
        #         for y in range(min_point, max_point + 1):
        #             value = (1 / (2 * np.pi * (sigma ** 2)) * np.exp((-(x ** 2 + y ** 2)) / (2 * (sigma ** 2))))
        #             K[x - min_point, y - min_point] = value
        #     return K

        
        # kernel = gaussian_kernel(11, 2)

        # gaussianFrame = cv2.filter2D(frame, -1, kernel)
        
        # img_gaussian = np.float64(frame)

        # mask_x = np.zeros((2, 1))
        # mask_x[0] = -1
        # mask_x[1] = 1

        # I_x = cv2.filter2D(img_gaussian, -1, mask_x)
        # mask_y = mask_x.T
        # I_y = cv2.filter2D(img_gaussian, -1, mask_y)
        
        # Gm = (I_x ** 2 + I_y ** 2) ** 0.5
        # Gd = np.rad2deg(np.arctan2(I_y, I_x))
        
        # cv2.imshow("gaussian", gaussianFrame)
        # cv2.imshow("I_x", I_x)
        # cv2.imshow("I_y", I_y)
        # cv2.imshow("Gm", Gm)
        # cv2.imshow("Gd", Gd)
        # Convert to graycsale
        # img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # # Blur the image for better edge detection
        # img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
        # # Sobel Edge Detection
        # sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
        # sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
        # sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
        # # Display Sobel Edge Detection Images
        # cv2.imshow('Sobel X', sobelx)
        # cv2.imshow('Sobel Y', sobely)
        # cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
        # cv2.waitKey(0)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Find Canny edges
        edged = cv2.Canny(gray, 30, 200)
        
        # Finding Contours
        # Use a copy of the image e.g. edged.copy()
        # since findContours alters the image
        contours, hierarchy = cv2.findContours(edged, 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        cv2.imshow('Canny Edges After Contouring', edged)
        cv2.waitKey(0)
        
        print("Number of Contours found = " + str(len(contours)))
        
        # Draw all contours
        # -1 signifies drawing all contours
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
        
        cv2.imshow('Contours', frame)
        cv2.waitKey(0)

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
                    if imgClass!="fire" and ratio>0.99:
                        # cv2.rectangle(frame, (widthStart, heightStart), (widthStart+parts, heightStart+parts), randomColor, 1)
                        MarkTheObject.markObject(frame, FrameSchema.Frame("image", imgClass, widthStart, widthStart+parts, heightStart, heightStart+parts), ratio)
                        foundPoints.append({
                            "widthStart":widthStart,
                            "heightStart":heightStart,
                            "widthStart+parts":widthStart+parts,
                            "heightStart+parts":heightStart+parts,
                        })
        # cv2.imshow("frame2", frame)
        # cv2.waitKey(0)
        # print(foundPoints)
        # print([minWidthStart["widthStart"] for minWidthStart in foundPoints if minWidthStart["heightStart"]==32])