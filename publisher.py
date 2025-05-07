import paho.mqtt.client as mqtt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Successful connection callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to broker")
    else:
        print(f"❌ Connection error")

# Init MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# Set callback for onConnect
client.on_connect = on_connect

# Set SSL/TLS default configs
client.tls_set()

try:
    # Connect to the broker on port 8883, using in this case a public one (https://www.hivemq.com/mqtt/public-mqtt-broker/)
    # Secure communication requires a stronger broker!
    client.connect("broker.hivemq.com", 8883, 60)
    
    while True:
        # Ask the user to type topic and message
        topic = input("📬 type the topic: ")
        messaggio = input("📝 type the message: ")
        
        print(f"📤 sending message..")
        
        # Publish the message
        client.publish(topic, messaggio)
        
        # Wait for user input to send another message
        input("✅ message sent. Press enter to send another message")
        print(f" ")
        print(f" ")
        
except Exception as e:
    print(f"❌ Connection error")
