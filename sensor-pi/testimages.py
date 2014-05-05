#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO
import subprocess
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

count = 0
up = False
down = False
command = ""
filename = ""
index = 0
camera_pause = "500"

def takepic(imageName):
  print("picture")
  command = "sudo raspistill -o " + imageName + " -q 100 -t " + camera_pause
  print(command)
  os.system(command)
  
while(True):
  if(up==True):
    if(GPIO.input(24)==False):
      now = datetime.datetime.now()
      timeString = now.strftime("%Y-%m-%d_%H%M%S")
      filename = "photo-"+timeString+".jpg"
      takepic(filename)
      subprocess.call(['./processImage.sh', filename, '&'])
  up = GPIO.input(24)
  count = count+1
  sleep(.1)
print "done"
      
