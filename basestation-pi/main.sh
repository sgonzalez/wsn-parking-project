#!/bin/sh

echo -ne "Running basestation program..."

echo -ne "Checking internet connection..."
if ping -t 1 -c 1 google.com > /dev/null 2>&1
then
  echo " GOOD"
else
  echo " FAILED"
  exit 1
fi