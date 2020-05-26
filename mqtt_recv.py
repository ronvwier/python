import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	#The callback for when the client connects to the broker
    client.subscribe([('time/#',0),('timer/#',0),('env/#',0),('inverter/#',0)])

def on_message(client, userdata, msg):
	#The callback for when a PUBLISH message is received from the server.
	print(f"Message received-> {msg.topic} {msg.payload} retain={msg.retain} qos={msg.qos}")


def on_log(client, userdata, level, buf):
    print("log: ",buf) 

client = mqtt.Client("",clean_session=True)  # Create instance of client with ID
client.on_connect = on_connect
client.on_message = on_message
#client.on_log=on_log

client.connect('192.168.0.129')

while True:
	print('loop')
	client.loop()  # Start networking daemon