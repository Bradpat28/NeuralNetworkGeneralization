import timeit
from parseHelper import parseNNRunFile
import pickle



def manageData(filename, dir):
    print "\t--------------"
    start_time = timeit.default_timer()
    print "\tManaging Data..."

    #Create a NNRun object to represent the NNRun
    nnRun = parseNNRunFile(filename, dir)
    nnRunFile = open(dir + "/NNRuns/" + filename  + ".nnRun", "wb")
    #Save the NNRun object in a .nnRun file
    pickle.dump(nnRun, nnRunFile);
    nnRunFile.close()


    stop_time = timeit.default_timer()
    print "\tDuration: " + str(stop_time - start_time) + " Seconds"
    print "\t--------------"
