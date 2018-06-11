import timeit
from NNRunClass import *
import pickle
import glob
import sys
import shutil
from PIL import Image, ImageFile
import json
from keras.models import model_from_json
import os
import numpy as np


def classify():
    if not len(sys.argv) == 3:
        exit("Need to specify a working directory")
    dir = sys.argv[1]
    nnRunToUse = sys.argv[2]

    f = open(dir + "/NNRuns/" + nnRunToUse + ".json", 'r')
    model = model_from_json(f.read())
    model.load_weights(dir + "/NNRuns/" + nnRunToUse + ".h5")

    classify_dir = glob.glob(dir + "/classify");
    if len(classify_dir) == 0:
        sys.exit("Error:'Classify Dirrectory Not Found':Could not find directory named 'classify'");

    undecide_dir = glob.glob(dir + "/classify/Undecided")
    if len(undecide_dir) == 0:
        os.mkdir(dir + "/classify/Undecided")
    nnRunFile = open(dir + "/NNRuns/" + nnRunToUse + ".nnRun")
    nn = pickle.load(nnRunFile)
    class_names = nn.classNames
    cat_dirs = [d for d in os.listdir(dir + '/classify/') if os.path.isdir(os.path.join(dir + '/classify/', d))]
    if len(cat_dirs) - 1 != len(class_names):
        for name in class_names:
            print name
            os.mkdir(dir + "/classify/" + name)


    imgFiles = glob.glob(dir + "/classify" + "/*.png")
    numFiles = 0;
    for img in imgFiles:
        im = Image.open(img)
        rgb_im = im.convert('RGB')
        rgb_im.save(dir + "/classify/image_"+ str(numFiles) + ".jpg")
        numFiles += 1

    imgFiles = glob.glob(dir + "/classify/*.PNG")
    for img in imgFiles:
        im = Image.open(img)
        rgb_im = im.convert('RGB')
        rgb_im.save(dir +  "/classify/image_"+ str(numFiles) + ".jpg")
        numFiles += 1

    imgFiles = glob.glob(dir + "/classify/*.JPG")
    for img in imgFiles:
        shutil.copyfile(img,dir +  "/classify/image_"+ str(numFiles) + ".jpg")
        numFiles += 1

    imgFiles = glob.glob(dir + "/classify/*.jpeg")
    for img in imgFiles:
        shutil.copyfile(img,dir +  "/classify/image_"+ str(numFiles) + ".jpg")
        numFiles += 1

    photos = glob.glob(dir + "/classify/*.jpg")
    numImages = 0
    class_names.reverse()
    for photo in photos:
        print photo
        im = Image.open(photo)
        size = 100,100
        img = im.resize(size)
        image = np.expand_dims(img, axis=0)
        #print im
        result = model.predict(image)
        best_ind = 0
        second_best_ind = 1
        i = 0;
        print result
        for x in result[0]:
            print x
            if x > result[0][best_ind]:
                second_best_ind = best_ind
                best_ind = i

            i += 1

        print class_names[best_ind]


        if abs(result[0][best_ind] - result[0][second_best_ind]) < .2:
            shutil.move(photo, dir + "/classify/Undecided/image" + str(numImages) + ".jpg")
        else:
            #if (result[0][best_ind] > .5):
            shutil.move(photo, dir + "/classify/" + class_names[best_ind] + "/image" + str(numImages) + ".jpg")
            #else:
            #    shutil.move(photo, dir + "/classify/Undecided/image" + str(numImages) + ".jpg")
        numImages += 1








if __name__ == '__main__':
    classify()
