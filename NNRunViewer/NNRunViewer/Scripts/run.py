import timeit
import tensorflow as tf
from keras.optimizers import SGD
from keras.models import Sequential
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import skimage.io as io
import matplotlib.pyplot as plt
import sys


#TODO Make this dynamic as a runtime param or based on the smallest image or something
IMAGE_HEIGHT = 100
IMAGE_WIDTH = 100

TF_RECORDS = 'NNRecord.tfrecords'

def runNN(fileName, dir, num_epoch, steps_per_e, val_steps, val_percent, batch_size):
    print "\t--------------"
    start_time = timeit.default_timer()
    print "\tRunning NN..."
    old_stdout = sys.stdout
    old_stderr = sys.stderr

    sys.stdout = open(dir + "/NNRuns/" + fileName, 'w')
    sys.stderr = open(dir + "/NNRuns/" + fileName + ".errLog", "w")

    """
    ADD THE CODE FOR THE NN HERE
    """

    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3), dim_ordering="tf"))
    model.add(Activation('tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="tf"))


    model.add(Conv2D(32, (3, 3), dim_ordering="tf"))
    model.add(Activation('tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="tf"))

    model.add(Conv2D(64, (3, 3), dim_ordering="tf"))
    model.add(Activation('tanh'))
    model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="tf"))

    model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    model.add(Dense(64))
    model.add(Activation('tanh'))

    model.add(Dropout(0.5))
    model.add(Dense(2))
    model.add(Activation('sigmoid'))

    model.compile(loss='categorical_crossentropy',
                  optimizer=SGD(),
                  metrics=['accuracy'])

    """
    BETWEEN THESE
    """

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
            dir + '/Train',  # this is the target directory
            target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),  # all images will be resized to whatever specified
            batch_size=batch_size,
            class_mode='categorical')

    validation_generator = test_datagen.flow_from_directory(
        dir + '/Validation',
        target_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        batch_size=batch_size,
        class_mode='categorical')

    model.fit_generator(
    train_generator,
    steps_per_epoch= steps_per_e,
    epochs=num_epoch,
    validation_data=validation_generator,
    validation_steps=val_steps)
    
    model_json = model.to_json()
    with open(dir + "/NNRuns/" + fileName + ".json", "w") as json_file:
        json_file.write(model_json);
    
    model.save_weights(dir + "/NNRuns/" + fileName + ".h5")
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    stop_time = timeit.default_timer()
    print "\tDuration: " + str(stop_time - start_time) + " Seconds"
    print "\t--------------"
