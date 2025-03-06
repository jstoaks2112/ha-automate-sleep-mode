# ha-automate-sleep-mode
a little python script to suspend or put your desktop linux machine to sleep

You can use Mosquitto on Homeassistant to publish to this topic on an event trigger or automation and suspend or sleep mode the machine.

Example:
  If I leave my house and my device.tracker in HomeAssistant leaves the Home Zone, An Automation then publish's
a payload of 'OFF' when I leave the Home Zone. The Python script is subscribed to the same topic and receives the payload 'OFF'
executing sleep mode. Thus saving energy when not using the hardware.

  To wake the machine you can do this with manual interface or use a Wake On Lan Magic Packet
broadcast with the correct MAC Address. HomeAssistant has a Magic Packet Integration.


Run this script to put your machine to sleep, or install it as a service on your linux OS.

This script subscribes to the mqtt topic and listens for "OFF" then executes sleep mode.

Download the python file and place it in a directory in your /etc/
Download the Linux Service file to /etc/systemd/system

Edit the service file to reflect the path to the python script.

example: mqtt-sleep-mode.service

[Unit]
Description=MQTT Sleep Mode Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /etc/mqtt_sleep_mode.py  ## edit this line with your local path to the python script
Restart=always

[Install]
WantedBy=multi-user.target
