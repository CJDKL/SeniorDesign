# Credit Source for basic program layout:
#   https://www.pyimagesearch.com/2018/04/16/keras-and-convolutional-neural-networks-cnns/
# Author: Darence Lim and Tracy Sun
# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image examples/charmander_counter.png

# import the necessary packages
from phue import Bridge
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
import time

#Connect to phue bridge
b = Bridge('192.168.1.2')
b.connect()
b.get_api()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to label binarizer")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
output = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (96, 96))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network and the label
# binarizer
print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())

# classify the input image
print("[INFO] classifying image...")
proba = model.predict(image)[0]
idx = np.argmax(proba)
label = lb.classes_[idx]

# we'll mark our prediction as "correct" of the input image filename
# contains the predicted label text (obviously this makes the
# assumption that you have named your testing image files this way)
filename = args["image"][args["image"].rfind(os.path.sep) + 1:]
#correct = "correct" if filename.rfind(label) != -1 else "incorrect"

# set brightness level to the recommended light level
# by National Optical Astronomy Observatory
f = open("lux.txt", "r")
currentLux = int(f.read())
f.close()

# watch TV range between 125 - 175
if(label=="watchTV"):
    desiredLux = 150
    while (currentLux > 175 or currentLux < 125):
        temp1 = brightness = b.get_light(5,'bri')
        factor = 0
        if (currentLux < 125):
            b.set_light(5, 'on', True)
            if(desiredLux - currentLux > 1000):
                factor = 35
            if(desiredLux - currentLux > 500):
                factor = 23
            if(desiredLux - currentLux > 200):
                factor = 15
            if(desiredLux - currentLux > 100):
                factor = 10
            if(desiredLux - currentLux <= 100):
                factor = 7
            temp1 = temp1 + factor
            if (temp1 > 255):
                temp1 = 255
            b.set_light(5, 'bri', temp1)
        if (currentLux > 175):
            if(currentLux - desiredLux > 1000):
                factor = 35
            if(currentLux - desiredLux > 500):
                factor = 23
            if(currentLux - desiredLux > 200):
                factor = 15
            if(currentLux - desiredLux > 100):
                factor = 10
            if(currentLux - desiredLux <= 100):
                factor = 7
            temp1 = temp1 - factor
            if (temp1 <= 0 ):
                temp1 = 0
                b.set_light(5, 'on', False)
            b.set_light(5, 'bri', temp1)
        time.sleep(1)
        f = open("lux.txt", "r")
        currentLux = int(f.read())
        f.close()

# eating range 200 - 300
if(label=="eating"):
    desiredLux = 250
    while (currentLux > 300 or currentLux < 200):
        temp1 = brightness = b.get_light(5,'bri')
        factor = 0
        if (currentLux < 200):
            b.set_light(5, 'on', True)
            if(desiredLux - currentLux > 1000):
                factor = 35
            if(desiredLux - currentLux > 500):
                factor = 23
            if(desiredLux - currentLux > 200):
                factor = 15
            if(desiredLux - currentLux > 100):
                factor = 10
            if(desiredLux - currentLux <= 100):
                factor = 7
            temp1 = temp1 + factor
            if (temp1 > 255):
                temp1 = 255
            b.set_light(5, 'bri', temp1)
        if (currentLux > 300):
            if(currentLux - desiredLux > 1000):
                factor = 35
            if(currentLux - desiredLux > 500):
                factor = 23
            if(currentLux - desiredLux > 200):
                factor = 15
            if(currentLux - desiredLux > 100):
                factor = 10
            if(currentLux - desiredLux <= 100):
                factor = 7
            temp1 = temp1 - factor
            if (temp1 <= 0 ):
                temp1 = 0
                b.set_light(5, 'on', False)
            b.set_light(5, 'bri', temp1)
        time.sleep(1)
        f = open("lux.txt", "r")
        currentLux = int(f.read())
        f.close()

# reading range between 450 - 550
if(label=="readingChair"):
    desiredLux = 500
    while (currentLux > 550 or currentLux < 450):
        temp1 = brightness = b.get_light(5,'bri')
        factor = 0
        if (currentLux < 450):
            b.set_light(5, 'on', True)
            if(desiredLux - currentLux > 1000):
                factor = 35
            if(desiredLux - currentLux > 500):
                factor = 23
            if(desiredLux - currentLux > 200):
                factor = 15
            if(desiredLux - currentLux > 100):
                factor = 10
            if(desiredLux - currentLux <= 100):
                factor = 7
            temp1 = temp1 + factor
            if (temp1 > 255):
                temp1 = 255
            b.set_light(5, 'bri', temp1)
        if (currentLux > 550):
            if(currentLux - desiredLux > 1000):
                factor = 35
            if(currentLux - desiredLux > 500):
                factor = 23
            if(currentLux - desiredLux > 200):
                factor = 15
            if(currentLux - desiredLux > 100):
                factor = 10
            if(currentLux - desiredLux <= 100):
                factor = 7
            temp1 = temp1 - factor
            if (temp1 <= 0 ):
                temp1 = 0
                b.set_light(5, 'on', False)
            b.set_light(5, 'bri', temp1)
        time.sleep(1)
        f = open("lux.txt", "r")
        currentLux = int(f.read())
        f.close()

# sleeping turn off the lights
if(label=="sleepingBed" or label=="sleepingCouch"):
    b.set_light(5, 'on', False)

# build the label and draw the label on the image
activity = label
label = "{}: {:.2f}%".format(label, proba[idx] * 100)
output = imutils.resize(output, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

# show the output image
print("[INFO] {}".format(label))
brightness = b.get_light(5,'bri')
print("[BRIGHTNESS] {}".format(brightness))

# write label and brightness into text file
f = open("result.txt","wb")
f.write(activity)
f.write(" ")
f.write(str(brightness))

#cv2.imshow("Output", output)
#cv2.waitKey(0)
