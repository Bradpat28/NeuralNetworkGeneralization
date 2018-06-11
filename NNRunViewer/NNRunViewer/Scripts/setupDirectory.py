import glob
import sys
import os
import shutil
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import timeit
import random
import math

VALIDATION_PERCENT= .2

def setupDir(dir):
    print "\t\t--------------"
    start_time = timeit.default_timer()
    print "\t\tSetting up Directory..."

    #Make a Directory to store the NN runs
    NN_dir = glob.glob(dir + "/NNRuns")
    if len(NN_dir) == 0:
        os.mkdir(dir + "/NNRuns")

    #Make a directory for Train data
    train_dir = glob.glob(dir + "/Train")
    if len(train_dir) == 0:
        os.mkdir(dir + "/Train")

    #Make a directory for Validation data
    val_dir = glob.glob(dir + "/Validation")
    if len(val_dir) == 0:
        os.mkdir(dir + "/Validation")

    #Expect there to be a folder called "data" in the working directory
    root_data_dir = glob.glob(dir + "/data")
    if len(root_data_dir) == 0:
        sys.exit("Error:'Data Directory Not Found':Could not find directory named 'data'")

    #Make a list of all the Categories in data
    cat_dirs = [d for d in os.listdir(dir + '/data/') if os.path.isdir(os.path.join(dir + '/data/', d))]
    print "**********"
    print cat_dirs

    #Check if there is at least 2 dirs
    if len(cat_dirs) < 2:
        sys.exit("Error:'Less than 2 Categories found':Only found " + len(cat_dirs) + " Categories")

    #Check if the files are alreday made in the directory
    train_cat = [d for d in os.listdir(dir + '/Train/') if os.path.isdir(os.path.join(dir + '/Train/', d))]
    if len(train_cat) == len(cat_dirs):
        val_cat = [d for d in os.listdir(dir + '/Validation/') if os.path.isdir(os.path.join(dir + '/Validation/', d))]
        if len(val_cat) == len(cat_dirs):
            print "\t\tAlready created the correct directories...Exiting"
            stop_time = timeit.default_timer()
            print "\t\tDuration: " + str(stop_time - start_time) + " Seconds"
            print "\t\t--------------"
            return

    #Make Directories for the Categories
    for d in cat_dirs:
        os.mkdir(dir + "/Train/" + d)
        #Copy all images to the corresponding dir directory
        print dir + "/data/" + d
        copy_all_images(dir + "/data/" + d + "/", dir + "/Train/" + d + "/", d, 0)
        os.mkdir(dir + "/Validation/" + d)
        split_images_val(dir + "/Train/" + d + "/", dir + "/Validation/" + d + "/",  d)


    stop_time = timeit.default_timer()
    print "\t\tDuration: " + str(stop_time - start_time) + " Seconds"
    print "\t\t--------------"

"""
    #Convert all images in data/ to jpg and place in damaged
    number_damaged = copy_all_images("data", 1)

    internal_dirs = [d for d in os.listdir('data/Specific Material Damage') if os.path.isdir(os.path.join('data/Specific Material Damage', d))]

    for int_dir in internal_dirs:
        temp_dirs = [d for d in os.listdir('data/Specific Material Damage/' + int_dir) if os.path.isdir(os.path.join('data/Specific Material Damage/' + int_dir, d))]
        if len(temp_dirs) != 0:
            for dir_tem in temp_dirs:
                number_damaged = copy_all_images('data/Specific Material Damage/' + int_dir + "/" + dir_tem, number_damaged)

        number_damaged = copy_all_images("data/Specific Material Damage/" + int_dir, number_damaged)

    #Go through all of the files in Damaged, and separate into validation folder
    os.mkdir("Validation/Damaged/")
    file_list = glob.glob("Train/Damaged/*.jpg")
    num_transfer = len(file_list) * VALIDATION_PERCENT
    num_transfer = math.floor(num_transfer)
    indexes = random.sample(xrange(1, int(len(file_list))), int(num_transfer))
    num_val = 0
    #Transfer those images to the Validation directory
    for x in indexes:
        shutil.move(file_list[x], "Validation/Damaged/damaged_" + str(num_val) + ".jpg")
        num_val += 1
"""


def split_images_val(from_path, to_path, cat_name):
    img_files = glob.glob(from_path + "*.jpg")
    print img_files[0]
    num_transfer = math.floor(len(img_files) * VALIDATION_PERCENT)
    print num_transfer
    indexes = random.sample(xrange(0, int(len(img_files))), int(num_transfer))
    num_val = 0
    for x in indexes:
        shutil.move(img_files[x], to_path + cat_name + "_" + str(num_val) + ".jpg")
        num_val += 1

def copy_all_images(from_path, to_path, cat_name, startNum):
    number_images = startNum

    ##get all the dirs that are within this one
    internal_dirs = [d for d in os.listdir(from_path) if os.path.isdir(os.path.join(from_path, d))]
    for d in internal_dirs:
        number_images = copy_all_images(from_path + "/" + d, to_path, cat_name, number_images)

    imgFiles = glob.glob(from_path + "/*.jpg")
    for img in imgFiles:
        shutil.copyfile(img, to_path + cat_name + str(number_images) + ".jpg")
        number_images += 1

    imgFiles = glob.glob(from_path + "/*.jpeg")
    for img in imgFiles:
        shutil.copyfile(img, to_path + cat_name + str(number_images) + ".jpg")
        number_images += 1

    imgFiles = glob.glob(from_path + "/*.JPG")
    for img in imgFiles:
        shutil.copyfile(img, to_path + cat_name + str(number_images) + ".jpg")
        number_images += 1

    imgFiles = glob.glob(from_path + "/*.png")
    for img in imgFiles:
        im = Image.open(img)
        rgb_im = im.convert('RGB')
        rgb_im.save(to_path + cat_name + str(number_images) + ".jpg")
        number_images += 1

    imgFiles = glob.glob(from_path + "/*.PNG")
    for img in imgFiles:
        im = Image.open(img)
        rgb_im = im.convert('RGB')
        rgb_im.save(to_path + cat_name + str(number_images) + ".jpg")
        number_images += 1
    return number_images
