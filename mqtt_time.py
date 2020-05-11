import datetime
import paho.mqtt.client as mqtt

# Get date and time
x = datetime.datetime.now()
print(x)

# Format message as Mon 11 May 2020,14:56
message = x.strftime('%a %d %b %Y,%H:%M')
print(message)

# Publish to MQTT server
SERVER = '192.168.0.129'
client = mqtt.Client()
client.connect(SERVER)
client.publish("time/display", message ,retain=True)
client.disconnect()