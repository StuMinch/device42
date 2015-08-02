#!/bin/bash

# Enter attributes here:
SWITCH_NAME=switchA
HARDWARE=AS6701-32X
MAC_ADDRESS=70:72:cf:cb:f6:8a
IP_ADDRESS=10.100.254.21

# Add the switch hardware
curl -X POST -d "name=$SWITCH_NAME&type=physical&hardware=$HARDWARE&is_it_switch=yes&in_service=yes&service_level=production&macaddress=$MAC_ADDRESS" -u 'username:password' https://192.168.0.1/api/device/ --insecure

sleep 2

# Add the MGMT IP address
curl -X POST -d "device=$SWITCH_NAME&ipaddress=$IP_ADDRESS" -u 'username:password' https://192.168.0.1/api/ip/ --insecure

sleep 2

# Add the switch ports
for i in {1..32}
do
   curl -X POST -d "port=swp$i-s0&$SWITCH_NAME"  -u 'username:password' https://192.168.0.1/api/1.0/switchports/ --insecure
   curl -X POST -d "port=swp$i-s1&$SWITCH_NAME"  -u 'username:password' https://192.168.0.1/api/1.0/switchports/ --insecure
   curl -X POST -d "port=swp$i-s2&$SWITCH_NAME"  -u 'username:password' https://192.168.0.1/api/1.0/switchports/ --insecure
   curl -X POST -d "port=swp$i-s3&$SWITCH_NAME"  -u 'username:password' https://192.168.0.1/api/1.0/switchports/ --insecure
   sleep 2
done
