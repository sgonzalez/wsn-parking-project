#!/bin/sh

echo -e "Processing Image..."

prefixString="processed_"
filename=$1

sudo python testimages/processImage.py -n $filename -p $prefixString

echo -e "Sending Image..."

sudo python testimages/sendImage.py $prefixString$filename

echo -e "Image Sent"