class frameInfo:
    def __init__(self, imagePath, objectName, widthStart, widthEnd, heightStart, heightEnd):
        self.imagePath=imagePath
        self.objectName=objectName
        self.widthStart=widthStart
        self.widthEnd=widthEnd
        self.heightStart=heightStart
        self.heightEnd=heightEnd
    def getFrameInfo(self):
        return {
            "image_path":self.imagePath,
            "object_name":self.objectName,
            "object_position":[
                {                
                    "widthStart":self.widthStart,
                    "widthEnd":self.widthEnd,
                    "heightStart":self.heightStart,
                    "heightEnd":self.heightEnd
                }
            ]
        }