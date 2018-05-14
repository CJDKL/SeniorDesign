#########################################################
#MQTT
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish



#########################################################
#MQTT
def connectionStatus(client, userdata, flags, rc):
    mqttClient.subscribe("connect")

def messageDecoder(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8')
    if message == "get brightness":
        mqttClient.publish("to iOS", brightness)
        print("Brightness sent to iOS device!")
    if message == "get activity":
        mqttClient.publish("to iOS", label)
        print("Activity sent to iOS device!")
    else:
        print("Unknown message!")


f = open("result.txt", "r")
temp = f.readline().split(" ")
label = temp[0]
brightness = temp[1]
print(label)
print(brightness)
f.close()


#Instantiate Eclipse Paho as mqttClient
mqttClient = mqtt.Client("RPI")

#Set calling function functions to mqttClient
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

        
#Connect client to server
mqttClient.connect("192.168.1.3")


#Monitor client activity forever
mqttClient.loop_forever()
