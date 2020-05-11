#!/usr/bin/python3
import datetime
import paho.mqtt.client as mqtt

# Format message as Mon 11 May 2020,14:56
x = datetime.datetime.now()
message = x.strftime('%a %d %b %Y,%H:%M')

# Publish to MQTT server
SERVER = '192.168.0.129'
client = mqtt.Client()
client.connect(SERVER)
client.publish("time/display", message ,retain=True)
client.disconnect()