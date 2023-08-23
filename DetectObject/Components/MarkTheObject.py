from Libs import cv2
def convertObjectInfo(objectInfo):
    imagePath=objectInfo["image_path"]
    objectName=objectInfo["object_name"]
    widthStart=objectInfo["object_position"]["widthStart"]
    widthEnd=objectInfo["object_position"]["widthEnd"]
    heightStart=objectInfo["object_position"]["heightStart"]
    heightEnd=objectInfo["object_position"]["heightEnd"]
    return imagePath, objectName, widthStart, widthEnd, heightStart, heightEnd
def markObject(self, objectInfo):
    imagePath, objectName, widthStart, widthEnd, heightStart, heightEnd=convertObjectInfo(objectInfo)
    cv2.putText(self.frame, objectName, (widthStart+10, heightStart+10), cv2.CHAIN_APPROX_SIMPLE, 1, (0, 255, 0), 1)
    cv2.rectangle(self.frame, (widthStart, widthEnd), (heightStart, heightEnd), (0, 255, 0), 1)