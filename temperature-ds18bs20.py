#!/usr/bin/env python

import os
import glob
import time
import urllib2

#USER DEFINED VARIABLES
#Please insert your station id here:
sid = "INSERT YOUR STATION ID"
#Please insert your station token here:
token = "INSERT YOUR TOKEN"
#Set the interval in seconds to send data to weather-o-matic
sleeptime = 3600 #update every hour


# load the kernel modules needed to handle the sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# find the path of a sensor directory 
devicelist = glob.glob('/sys/bus/w1/devices/*')
# append the device file name to get the absolute path of the sensor 
devicefile = "" #devicelist[1] + '/w1_slave'
for device in devicelist:
      if device != "w1_bus_master1":
            devicefile = device + '/w1_slave'

# open the file representing the sensor.
while True:
      fileobj = open(devicefile,'r')
      lines = fileobj.readlines()
      fileobj.close()
      temp_pos = lines[1][:-1].find("t=")
      if temp_pos != -1:
          tempData = lines[1][temp_pos+2:]
          temperature = float(tempData)
          temperature /= 1000;
          print temperature # For Debug purposes
          urllib2.urlopen("http://weather-o-matic.herokuapp.com/submit?id=" + sid + "&token=" + token + "&value=" + str(temperature)).read()
          print "Sent data to w-o-m"
      else:
          print "Failed to read temperature" 
      time.sleep(sleeptime)
    
   

