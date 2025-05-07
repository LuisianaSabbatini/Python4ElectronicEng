import paho.mqtt.client as mqtt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Successful connection callback
def on_connect(client, userdata, flags, rc):
    print(f"✅ Connected to the broker")
    # Subscribe to the topic
    client.subscribe("topic1")
    client.subscribe("topic2/subtopic3/subsubtopic1")
    client.subscribe("topic2/subtopic2//#")

# Received message callback
def on_message(client, userdata, msg):
    print(f"📨 {msg.topic} -> {msg.payload.decode()}")

# Creates an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# Set callbacks
client.on_connect = on_connect
client.on_message = on_message

# Set SSL/TLS configs (default configs)
client.tls_set()

# Connect to the broker on port 8883, using a public one in this case for debugging purposes.
# Secure communication requires a stronger (and non public broker)!!
client.connect("broker.hivemq.com", 8883, 60)

# Infinite loop
client.loop_forever()
