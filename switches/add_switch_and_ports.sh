#!/bin/bash

# Add the switch hardware
curl -X POST -d "name=sv5-rack2-switchB&type=physical&hardware=30&is_it_switch=yes&in_service=yes&service_level=production&macaddress=08:9e:01:ce:c0:43" -u 'username:password' https://10.100.0.114/api/device/ --insecure

sleep 5

# Add the switch ports
for i in {1..52}
do
   curl -X POST -d "port=SW2-P$i&switch=sv5-rack2-switchB"  -u 'username:password' https://10.100.0.114/api/1.0/switchports/ --insecure
done