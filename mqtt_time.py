#!/usr/bin/python3
import datetime
import paho.mqtt.client as mqtt
import json

# Format message as Mon 11 May 2020,14:56
x = datetime.datetime.now()
x_date = x.strftime('%a %d %b %Y')
x_time = x.strftime('%H:%M')
x_dict = { 'date':x_date,'time':x_time }
message = json.dumps(x_dict)

# Publish to MQTT server
SERVER = '192.168.0.129'
client = mqtt.Client()
client.connect(SERVER)
client.publish("time/display", message ,retain=True)
client.disconnect()