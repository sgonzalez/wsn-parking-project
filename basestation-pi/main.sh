#!/bin/sh

echo -e "Running basestation program..."

echo -e "Checking internet connection..."
wget -q --tries=10 --timeout=20 http://google.com
if [[ $? -eq 0 ]]; then
        echo " GOOD"
else
        echo " FAILED"
        exit 1
fi