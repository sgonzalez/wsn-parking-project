#!/bin/sh

# Note: requires connecting a button to GPIO 24 on the raspberry pi

echo -e "Running test image acquisition program..."

cd wsn-parking-proejct/sensor-pi
sudo python testimages.py
