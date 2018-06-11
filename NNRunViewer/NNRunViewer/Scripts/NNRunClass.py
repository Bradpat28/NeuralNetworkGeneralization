import matplotlib.pyplot as plt

class NNRun:
    def __init__(self):
        self.epochs = []
        self.numEpochs = 0
        self.totalTime = 0
        self.numTrainImg = 0.0
        self.numValImg = 0.0
        self.name = ""
        self.valImgPercent = 0.0
        self.lastTrainPercent = 0.0
        self.lastValPercent = 0.0
        self.classNames = []

    def addEpoch(self, epoch):
        self.epochs.append(epoch)
        self.numEpochs += 1
        self.totalTime += epoch.time

    def addClassName(self, className):
        self.classNames.append(className)

    def toString(self):
        print "Name: " + self.name
        print "Total Time: " + str(self.totalTime);
        print "Num Training Images: " + str(self.numTrainImg)
        print "Num Validation Images: " + str(self.numValImg)
        print "Number Epochs: " + str(self.numEpochs);
        print "Epochs:"
        i = 0
        for epoch in self.epochs:
            print "----------------"
            print "Epoch Number : " + str (i)
            epoch.toString()
            i += 1

    def visualize(self):
        accList = []
        lossList = []
        valAccList = []
        valLossList = []
        for epoch in self.epochs:
            accList.append(epoch.acc)
            lossList.append(epoch.loss)
            valAccList.append(epoch.valAcc)
            valLossList.append(epoch.valLoss)
        plt.subplot(211)
        plt.plot(range(self.numEpochs), accList, label="Accuracy")
        plt.plot(range(self.numEpochs), valAccList, label="Validation Accuracy")
        plt.title("Accuracy")
        plt.legend(loc='upper left')

        plt.subplot(212)
        plt.plot(range(self.numEpochs), lossList, label="Loss")
        plt.plot(range(self.numEpochs), valLossList, label="Validation Loss")
        plt.title("Loss")
        plt.legend(loc='upper left')
        plt.show()

    def getAccList(self):
        accList = []
        for epoch in self.epochs:
            accList.append(epoch.acc)
        return accList

    def getValAccList(self):
        valAccList = []
        for epoch in self.epochs:
            valAccList.append(epoch.valAcc)
        return valAccList

    def getLossList(self):
        lossList = []
        for epoch in self.epochs:
            lossList.append(epoch.loss)
        return lossList

    def getValLossList(self):
        valLossList = []
        for epoch in self.epochs:
            valLossList.append(epoch.valLoss)
        return valLossList


class Epoch:
    def __init__(self):
        self.acc = 0.0
        self.valAcc = 0.0
        self.loss = 0.0
        self.valLoss = 0.0
        self.time = 0.0

    def toString(self):
        print "Accuracy: " + str(self.acc)
        print "Loss: " + str(self.loss)
        print "Validation Accuracy: " + str(self.valAcc)
        print "Validation Loss: " + str(self.valLoss)
        print "Time Taken: " + str(self.time) + " seconds"
