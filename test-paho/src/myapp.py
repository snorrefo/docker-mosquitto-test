import paho.mqtt.client as mqtt
import time
import json
import random


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

client = mqtt.Client()
client.on_connect = on_connect


# client.connect("iot.eclipse.org", 1883, 60)
# mqtt is docker service name
client.connect("mqtt", 1883, 60)

client.loop_start()


#
# happy-bubbles/ble/esp-link-03-r3/raw/2fb597bc5b2d
# {
#   "hostname" : "esp-link-03-r3",
#   "mac" : "2fb597bc5b2d",
#   "rssi" : -83,
#   "is_scan_response" : "0",
#   "type" : "3",
#   "data" : "1eff0600010920009b740ed6f44b284ec855f71063686e988e7f903a226534"
# }
#
# happy-bubbles/ble/esp-link-01-test/raw/2fb597bc5b2d
# {
#   "hostname" : "esp-link-01-test",
#   "mac" : "2fb597bc5b2d",
#   "rssi" : -83,
#   "is_scan_response" : "0",
#   "type" : "3",
#   "data" : "1eff0600010920009b740ed6f44b284ec855f71063686e988e7f903a226534"
# }

# mqtt_raw_01 = {
#     "hostname": "esp-link-01-test",
#     "mac": "2fb597bc5b2d",
#     "rssi": -83,
#     "is_scan_response": "0",
#     "type": "3",
#     "data": "1eff0600010920009b740ed6f44b284ec855f71063686e988e7f903a226534",
#     }
#
# print(json.dumps(mqtt_raw_01))

class MQTT_raw(object):
    """Class for setting values for MQTT messages published to
    happy-bubbles/ble/esp-link-01-test/raw/2fb597bc5b2d"""

    def __init__(self):
        self.hostname = str
        self.mac = str
        self.rssi = int
        self.is_scan_response = str
        self.type = str
        self.data = str


mqtt_raw_01 = MQTT_raw()
mqtt_raw_01.hostname = "esp-link-01-test"
mqtt_raw_01.mac = "2fb597bc5b2d"
mqtt_raw_01.rssi = -83
mqtt_raw_01.is_scan_response = "0"
mqtt_raw_01.type = "3"
mqtt_raw_01.data = \
    "1eff0600010920009b740ed6f44b284ec855f71063686e988e7f903a226534"

# https://stackoverflow.com/questions/10252010/serializing-class-instance-to-json
print(json.dumps(mqtt_raw_01.__dict__))


mqtt_raw_02 = MQTT_raw()
mqtt_raw_02.hostname = "esp-link-02-test"
mqtt_raw_02.mac = "2fb597bc5b2d"
mqtt_raw_02.rssi = -80
mqtt_raw_02.is_scan_response = "0"
mqtt_raw_02.type = "3"
mqtt_raw_02.data = \
    "1eff0600010920009b740ed6f44b284ec855f71063686e988e7f903a226534"

k = 1
nl = 0
while True:
    random.seed()

    close = random.randint(-39, -30)
    far = random.randint(-79, -70)

    if k > 10:
        k = 1
        if nl == 0:
            nl = 1
        else:
            nl = 0

    if nl == 0:
        mqtt_raw_01.rssi = close
        mqtt_raw_02.rssi = far
    else:
        mqtt_raw_01.rssi = far
        mqtt_raw_02.rssi = close

    k += 1

    # happy-bubbles/ble/esp-link-01-test/raw/2fb597bc5b2d
    topic = 'happy-bubbles/ble/' + mqtt_raw_01.hostname + '/raw/' + \
            mqtt_raw_01.mac
    payload = json.dumps(mqtt_raw_01.__dict__)
    # print(payload)
    client.publish(topic=topic, payload=payload, qos=0, retain=False)

    # happy-bubbles/ble/esp-link-02-test/raw/2fb597bc5b2d
    topic = 'happy-bubbles/ble/' + mqtt_raw_02.hostname + '/raw/' + \
            mqtt_raw_02.mac
    payload = json.dumps(mqtt_raw_02.__dict__)
    # print(payload)
    client.publish(topic=topic, payload=payload, qos=0, retain=False)
    time.sleep(1.0)
