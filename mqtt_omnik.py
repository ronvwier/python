#!/usr/bin/python3
import datetime
import paho.mqtt.client as mqtt
import json
from omnik import *

# Get date/time and inverter data
sensor = OMNIK('192.168.0.133')
x_time = datetime.datetime.now().isoformat()

if sensor.read():
    # Fill the dictionary and format the JSON message
    x_dict = { 'time':x_time, 'currentPower':sensor.currentPower,  'yieldToday':sensor.yieldToday, 'yieldTotal': sensor.yieldTotal }
    message = json.dumps(x_dict)
    print(message)

    # Publish to MQTT server
    SERVER = '192.168.0.129'
    client = mqtt.Client()
    client.connect(SERVER)
    client.publish("inverter/omnik", message ,retain=True)
    client.disconnect()
else:
    print('Omnik inverter offline')