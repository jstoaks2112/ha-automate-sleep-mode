# ha-automate-sleep-mode
a little python script to suspend or put your desktop linux machine to sleep

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
