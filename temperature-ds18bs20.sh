#! /bin/bash
#Loading the modules
modprobe w1-gpio
modprobe w1-therm

#INSERT YOUR DATA HERE:
#Please insert your device Name here:
devicename="INSERT DEVICE NAME"
#Please insert your station id here:
sid="INSERT STATION ID"
#Please insert your station token here:
token="INSERT TOKEN"

# Read Temperature
tempread=`cat /sys/bus/w1/devices/$devicename/w1_slave`
temp=`echo $tempread | egrep -o '.{5}$'`
temp2=`echo "scale=2; $temp / 1000" | bc`

#Send data
curl --request GET 'http://weather-o-matic.herokuapp.com/submit?id=$sid&token=$token&value=$temp2'

# Output the value for debugging etc.
echo $temp2
