weather-o-matic-client
======================

Client scripts for the weather-o-matic community. The webapp can be found here: http://weather-o-matic.herokuapp.com/ and on github: https://github.com/bigteddy97/weather-o-matic
# bash #
There are a few steps you have to do, before you can use your bash-script.
Open the script and edit the following vars:
* devicename: This is the name of your temperature-sensor device, which can be found under /sys/bus/w1/devices/ it should look similar to this example: 10-000802ab1678
* The id of your weather station:
The id of your weather station: can be found in the web-app. It should look like an even number
* The token of your weather station:
The token of your weather station can be found in the web-app. It should look like similar to this:    68ac906495480a3404beee4874ed853a037a7a8f

You may have to install bc via:
```sudo apt-get install bc```

It is recommended to use crontab to schedule the execution of the bash script.
# python #
Also in the python script you have to edit some variables:
* The id of your weather station:
The id of your weather station: can be found in the web-app. It should look like an even number
* The token of your weather station:
The token of your weather station can be found in the web-app. It should look like similar to this:    68ac906495480a3404beee4874ed853a037a7a8f
* The script automatically schedules sending data to weather-o-matic. By changing the variable "sleeptime" you can set the interval in seconds between to api-requests.

### General: ###
Start the script with su for the first time to successfully mount the 1-wire protocol modules. You also could execute the modprobe commands on startup.

## tested with ##
* Temperature sensor DS18S20
* Temperature sensor DS18B20
