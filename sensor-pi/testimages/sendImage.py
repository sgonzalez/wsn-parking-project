# Python script for the pi to post to website after getting an image

import sys
import requests

# This file will post an image to the ACMx server. It uses the 'requests'
# module for Multipart-Encoding of the image file. See 
# http://docs.python-requests.org/ for documentation. Prints server response
# to the console.
# 
# Args:
#		sensorID: The ID of the sensor who recorded the image.
#		image: A file handle that was opened for binary reading.
#					e.g. f = open('img.png', 'rb')
#
#	Returns:
#		(nothing)
#
imagePath = sys.argv[1]
sensorID = 2

print imagePath

image = open(imagePath, 'rb')

url = "http://wsn:raspberryp1@acmxlabs.org/smartlots/pidata"

# Construct the file payload.
fPayload = {"image": image}

# Construct normal form variables payload.
dPayload = {
	"id": sensorID
}
# Create a requests object to handle all the urllib2 stuff.
r = requests.post(url, data=dPayload, files=fPayload)

# Print out the server's response.
print r.text