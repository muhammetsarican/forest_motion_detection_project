from Libs import os
from ErrorHandler import error 
def getVar(envVarName):
    if envVarName is not None:
        return str(os.getenv(envVarName))
    else:
        error("We didnt find the env variable!")