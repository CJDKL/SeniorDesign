# Run script file to take one picture
# Process it through CNN model to write the result in result.txt file
# MQTT protocol to send the result file to IOS app

#!/bin/bash

#python camera.py

#python classify.py --model pokedex.model --labelbin lb.pickle \
#	--image image.jpg

python classify.py --model pokedex.model --labelbin lb.pickle \
	--image examples/watchTV.jpg

python mqtt.py
