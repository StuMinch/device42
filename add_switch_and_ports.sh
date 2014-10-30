#!/bin/sh

# Adds the new switch hardware
curl -X POST -d "name=site1-rack1-switch1&type=physical&is_it_switch=yes&in_service=yes&service_level=production&macaddress=00:01:02:03:04:05" -u "username:password" https://your.server.com/api/device --insecure

# Add the switch ports
for i in {1..48}
do
  curl -X POST -d "port=ge/0/$i&switch=site1-rack1-switch1" -u -u "username:password" https://your.server.com/api/1.0/switchports/ --insecure
done  
