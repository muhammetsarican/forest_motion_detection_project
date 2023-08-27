from Libs import cv2
import random
def randomColorGenerator():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
def convertObjectInfo(objectInfo):
    imagePath=objectInfo["image_path"]
    objectName=objectInfo["object_name"]
    widthStart=objectInfo["object_position"]["widthStart"]
    widthEnd=objectInfo["object_position"]["widthEnd"]
    heightStart=objectInfo["object_position"]["heightStart"]
    heightEnd=objectInfo["object_position"]["heightEnd"]
    return imagePath, objectName, widthStart, widthEnd, heightStart, heightEnd
def markObject(frame, objectInfo, ratio):
    randomColor=randomColorGenerator()
    imagePath, objectName, widthStart, widthEnd, heightStart, heightEnd=convertObjectInfo(objectInfo.getFrameInfo())
    print(imagePath, objectName, widthStart, widthEnd, heightStart, heightEnd)
    cv2.putText(frame, "{} %{:.2f}".format(objectName, ratio), (widthStart+10, heightStart+25), cv2.CHAIN_APPROX_SIMPLE, 0.4, randomColor, 1)
    cv2.rectangle(frame, (widthStart, heightStart), (widthEnd, heightEnd), randomColor, 1)
