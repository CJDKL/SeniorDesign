#!/bin/bash

#python camera.py

#python classify.py --model pokedex.model --labelbin lb.pickle \
#	--image image.jpg

python classify.py --model pokedex.model --labelbin lb.pickle \
	--image examples/watchTV.jpg

python mqtt.py