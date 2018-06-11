import timeit
from PIL import Image
import numpy as np
import skimage.io as io
import tensorflow as tf
import glob


DAMAGED_LABEL = 1

def setupRecs():
        print "\t\t--------------"
        start_time = timeit.default_timer()
        print "\t\tSetting up Records..."

        tfrecords_filename = 'NNRecord.tfrecords'

        if len(glob.glob('NNRecord.tfrecords')) != 0:
            stop_time = timeit.default_timer()
            print "\t\tDuration: " + str(stop_time - start_time) + " Seconds"
            print "\t\t--------------"
            return

        writer = tf.python_io.TFRecordWriter(tfrecords_filename)

        for im_path in glob.glob("Damaged/*.jpg"):
            img = np.array(Image.open(im_path))
            height = img.shape[0]
            width = img.shape[1]

            img_raw = img.tostring()

            example = tf.train.Example(features=tf.train.Features(feature={
                'height': _int64_feature(height),
                'width': _int64_feature(width),
                'image_raw': _bytes_feature(img_raw),
                'label': _int64_feature(DAMAGED_LABEL)}))
            writer.write(example.SerializeToString())

        for im_path in glob.glob("Undamaged/*.jpg"):
            img = np.array(Image.open(im_path))
            height = img.shape[0]
            width = img.shape[1]

            img_raw = img.tostring()

            example = tf.train.Example(features=tf.train.Features(feature={
                'height': _int64_feature(height),
                'width': _int64_feature(width),
                'image_raw': _bytes_feature(img_raw),
                'label': _int64_feature(DAMAGED_LABEL)}))
            writer.write(example.SerializeToString())


        writer.close()

        stop_time = timeit.default_timer()
        print "\t\tDuration: " + str(stop_time - start_time) + " Seconds"
        print "\t\t--------------"
