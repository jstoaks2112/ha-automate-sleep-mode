import paho.mqtt.client as mqtt
import subprocess

# MQTT Settings
mqtt_broker = "your.broker.ip"
mqtt_port = 1883
mqtt_topic = "/homeassistant/sensor/desktop/sleep-mode" ## or your topic of choosing
mqtt_username = "user"
mqtt_password = "password"

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(f"Received message on topic {msg.topic}: {payload}")

    if payload == "OFF":
        print("Entering sleep mode...")
        subprocess.call(["systemctl", "suspend"])

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set MQTT username and password
client.username_pw_set(mqtt_username, mqtt_password)

# Connect to MQTT Broker
client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT loop
client.loop_forever()
