from Libs import load_model, os, hub, tensorflow
from EnvVariableGetter import getVar
class Model:
    def __init__(self):
        self.model=self.loadModel()
        print("[Info] Model loaded...")
        
    def loadModel(self):
        modelPath=getVar("MODEL_PATH")
        # print(os.listdir(modelPath))
        model=load_model("./Model/Model_4-Acc_0.75-Loss_0.96.hdf5")
        return model

    def predict(self, frame):
        return self.model.predict(frame)