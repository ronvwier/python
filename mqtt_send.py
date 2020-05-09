import paho.mqtt.client as mqtt

SERVER = 'server'
#SERVER = 'mqtt.eclipse.org'

# This is the Publisher
client = mqtt.Client()
client.connect(SERVER)
client.publish("test/message", "Hello windows world! #1 on " + SERVER,retain=True)
client.publish("test/message", "Hello windows world! #2 on " + SERVER,retain=True)
client.disconnect()