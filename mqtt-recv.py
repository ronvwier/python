import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	#The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe("test/message")

def on_message(client, userdata, msg):
	#The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))

client = mqtt.Client("digi_mqtt_test")  # Create instance of client with ID
client.on_connect = on_connect
client.on_message = on_message
# client.connect("m2m.eclipse.org", 1883, 60)  
# Connect to (broker, port, keepalive-time)
client.connect('192.168.0.129', 1883,60)
client.loop_forever()  # Start networking daemon