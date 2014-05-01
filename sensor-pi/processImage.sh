#!/bin/sh

echo "Processing Image..."

prefixString="processed_"
filename=$1

python processImage.py -n $filename -p $prefixString

echo "Sending Image..."

python sendImage.py $prefixString$filename

echo "Image Sent"
