import timeit
from NNRunClass import *
import pickle
import glob
import matplotlib.pyplot as plt
import os

import sys


def visualizeNN(filename, dir):
    print "\t--------------"
    start_time = timeit.default_timer()
    print "\tVisualizing NN..."

    #open the file and read the saved object
    nnRunFile = open(dir + "/NNRuns/" + filename + ".nnRun")
    nnRun = pickle.load(nnRunFile)
    nnRun.visualize()
    nnRunFile.close()

    #Visualize multiple NN
    #visualizeAllNN()

    stop_time = timeit.default_timer()
    print "\tDuration: " + str(stop_time - start_time) + " Seconds"
    print "\t--------------"


def visualizeAllNN():
    if not len(sys.argv) == 2:
        exit("Need to specify a working directory")
    dir = sys.argv[1]
    nnRunDir = glob.glob(dir + "/NNRuns/*.nnRun")
    nnRuns = []
    for nnRunFilename in nnRunDir:
        nnRunFile = open(nnRunFilename)
        nn = pickle.load(nnRunFile)
        nnRuns.append(nn)
        nnRunFile.close()

    # Get current size
    fig_size = plt.rcParams["figure.figsize"]

    # Set figure width to 12 and height to 9
    fig_size[0] = 20.0
    fig_size[1] = 12.0
    plt.rcParams["figure.figsize"] = fig_size

#plt.figure().suptitle('All Saved Neural Network Runs')#, fontsize=18, fontweight='bold')

    numberOfSubplots = 2 * len(nnRuns)
    for i,v in enumerate(xrange(numberOfSubplots / 2)):
        v = v + 1
        ax1 = plt.subplot(numberOfSubplots / 2, 2, 2 * i + 1)
        ax1.set_title(nnRuns[v-1].name)
        ax1.plot(range(int(nnRuns[v-1].numEpochs)), nnRuns[v-1].getValAccList(), label="Validation Accuracy")
        #ax1.plot(range(int(nnRuns[v-1].numEpochs)), nnRuns[v-1].getValLossList(), label = "Validation Loss")
        ax1.legend(loc='upper left')
        
        ax2 = plt.subplot(numberOfSubplots / 2, 2, 2 * i + 2)
        ax2.set_title(nnRuns[v-1].name)
        #ax2.plot(range(int(nnRuns[v-1].numEpochs)), nnRuns[v-1].getValAccList(), label="Validation Accuracy")
        ax2.plot(range(int(nnRuns[v-1].numEpochs)), nnRuns[v-1].getValLossList(), label="Validation Loss")
        ax2.legend(loc='upper left')
    

    plt.tight_layout() # Or equivalently,  "plt.tight_layout()"
    plt.show()

#You can run python visualization.py and get all of the graphs

if __name__ == '__main__':
    visualizeAllNN()
