import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	#The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe([('time/display',0),('env/out',0),('inverter/omnik',0)])

def on_message(client, userdata, msg):
	#The callback for when a PUBLISH message is received from the server.
	print("Message received-> " + msg.topic + " " + str(msg.payload))
   
def on_log(client, userdata, level, buf):
    print("log: ",buf) 

client = mqtt.Client("",clean_session=True)  # Create instance of client with ID
client.on_connect = on_connect
client.on_message = on_message
client.on_log=on_log

client.connect('192.168.0.129')

while True:
	print('loop')
	client.loop()  # Start networking daemon