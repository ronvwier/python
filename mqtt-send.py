import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("192.168.0.129",1883,60)
client.publish("test/message", "Hello windows world! #1",retain=True)
client.publish("test/message", "Hello windows world! #2",retain=True)
client.disconnect()