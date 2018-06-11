from setupDirectory import setupDir
from setupRecords import setupRecs
import timeit

def setupNN(dir):
    print "\t--------------"
    start_time = timeit.default_timer()
    print "\tSetting up NN..."

    setupDir(dir)
    #setupRecs()


    stop_time = timeit.default_timer()
    print "\tDuration: " + str(stop_time - start_time) + " Seconds"
    print "\t--------------"
