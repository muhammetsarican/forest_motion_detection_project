class data:
    def __init__(self, path):
        self.path=path
    def getFromTxt(self):
        with open(self.path, "r", encoding="utf-8") as file:
            text=file.readlines()
        splittedText=[item.split("\n")[0] for item in text]
        return splittedText