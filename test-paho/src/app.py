import paho.mqtt.client as mqtt

import time
import json
import random


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("api/#", 0)


def on_message_msgs(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/messages/#
    print("MESSAGES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_message_bytes(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/bytes/#
    print("BYTES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_message(mosq, obj, msg):
    # This callback will be called for messages that we receive that do not
    # match any patterns defined in topic specific callbacks, i.e. in this case
    # those messages that do not have topics $SYS/broker/messages/# nor
    # $SYS/broker/bytes/#
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = mqtt.Client()

# Add message callbacks that will only trigger on a specific subscription match
client.message_callback_add("api/logger/pollingfreq", on_message_msgs)
client.message_callback_add("api/#", on_message_bytes)
client.on_message = on_message
client.on_connect = on_connect

# client.connect("iot.eclipse.org", 1883, 60)

# client = mqtt.Client()
# client.on_connect = on_connect
#
# client.connect("iot.eclipse.org", 1883, 60)
# # mqtt is docker service name
client.connect("mqtt", 1883, 60)

client.loop_start()


class MQTT_ch_set(object):

    def __init__(self):
        self.channel = str
        self.newvalue = float


mqtt_ch0_set = MQTT_ch_set()
mqtt_ch0_set.channel = 'ch0'
mqtt_ch0_set.newvalue = 0.004


# https://stackoverflow.com/questions/10252010/serializing-class-instance-to-json
# print(json.dumps(mqtt_raw_01.__dict__))


while True:

    topic = 'api/logger/pollingfreq'
    payload = json.dumps(mqtt_ch0_set.__dict__)
    # print(payload)
    client.publish(topic=topic, payload=payload, qos=0, retain=False)

    topic = 'api//ch0/set'
    payload = json.dumps(mqtt_ch0_set.__dict__)
    print(payload)
    client.publish(topic=topic, payload=payload, qos=0, retain=False)



    time.sleep(3.0)
