from NNRunClass import *
import os
import glob

def parseNNRunFile(filename, dir):
    nnRunObj = NNRun()
    nnRunObj.name = filename
    rawNNFile = open(dir + "/NNRuns/" + filename, "r")
    currEpoch = 0.0
    for line in rawNNFile:
        temp = line.split()

        if temp[0] == 'Epoch':
            if currEpoch != 0.0:
                nnRunObj.addEpoch(currEpoch)
            currEpoch = Epoch()

        elif temp[1][0] == '[':
            currEpoch.time = int(temp[-13].split('s')[0]);
            currEpoch.valAcc = float(temp[-1])
            currEpoch.valLoss = float(temp[-4])
            currEpoch.acc = float(temp[-7])
            currEpoch.loss = float(temp[-10])

        elif temp[0] == "Found":
            if nnRunObj.numTrainImg == 0.0:
                nnRunObj.numTrainImg = int(temp[1])
            else:
                nnRunObj.numValImg = int(temp[1])

    if currEpoch != 0.0:
        nnRunObj.addEpoch(currEpoch)
        nnRunObj.lastValPercent = currEpoch.valAcc
        nnRunObj.lastTrainPercent = currEpoch.acc

    nnRunObj.valImgPercent = nnRunObj.numValImg / (float(nnRunObj.numTrainImg) + float(nnRunObj.numValImg));

    cat_dirs = [d for d in os.listdir(dir + '/data/') if os.path.isdir(os.path.join(dir + '/data/', d))]
    for name in cat_dirs:
        nnRunObj.addClassName(name)
        
    return nnRunObj;
