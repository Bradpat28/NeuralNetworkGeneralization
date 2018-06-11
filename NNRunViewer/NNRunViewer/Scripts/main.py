from setup import setupNN
from run import runNN
from data import manageData
from visualization import visualizeNN

import timeit
import datetime
import sys

DEFAULT_NUM_EPOCHS = 5
DEFAULT_STEPS_PER_EPOCH = 25
DEFAULT_VAL_STEPS = 25
DEFAULT_VAL_PERCENT = .20
DEFAULT_BATCH_SIZE = 35

def main():
    print "--------------"
    print "Running Main..."
    start_time = timeit.default_timer()
    idVal = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
    if not len(sys.argv) == 7:
        exit("Error Invalid Runtime Arguments. EX: python main.py [working directory] [numEpochs or -1] [stepsPerEpoch or -1] [validationSteps or -1] [validationPercent or -1] [batchSize or -1]")
    dir = sys.argv[1]
    num_epochs = DEFAULT_NUM_EPOCHS
    steps_per_epoch = DEFAULT_STEPS_PER_EPOCH
    val_steps = DEFAULT_VAL_STEPS
    val_percent = DEFAULT_VAL_PERCENT
    batch_size = DEFAULT_BATCH_SIZE
    if int(sys.argv[2]) != -1:
        num_epochs = int(sys.argv[2])
    if int(sys.argv[3]) != -1:
        steps_per_epoch = int(sys.argv[3])
    if int(sys.argv[4]) != -1:
        val_steps = int(sys.argv[4])
    if int(sys.argv[5]) != -1:
        val_percent = int(sys.argv[5])
    if int(sys.argv[6]) != -1:
        batch_size = int(sys.argv[6])



    print dir
    setupNN(dir)
    runNN(idVal, dir, num_epochs, steps_per_epoch, val_steps, val_percent, batch_size)
    manageData(idVal, dir)
    visualizeNN(idVal, dir)


    stop_time = timeit.default_timer()
    print "Total Duration: " + str(stop_time - start_time) + " Seconds"
    print "--------------"

if __name__ == '__main__':
    main()
