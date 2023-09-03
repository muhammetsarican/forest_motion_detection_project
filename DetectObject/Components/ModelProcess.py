from Libs import load_model, os, hub
from EnvVariableGetter import getVar
class Model:
    def __init__(self):
        self.model=self.loadModel()
        print("[Info] Model loaded...")
        
    def loadModel(self):
        modelPath=getVar("MODEL_PATH")
        print(os.listdir(modelPath))
        model=load_model(modelPath+"Model_7-Acc_0.95-Loss_0.19.hdf5", custom_objects={'KerasLayer':hub.KerasLayer})
        return model

    def predict(self, frame):
        return self.model.predict(frame)