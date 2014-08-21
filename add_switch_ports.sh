#!/bin/bash
# Author: Stuart Minchington (stuarttm@me.com)
# Description: A script that utilizes device42's REST API to add multiple switch ports to a device
# For obvious reasons I am using faux details for the username, password, and IP address.
for i in {1..48}
do
   curl -X POST -d "port=SW1-P$i&switch=sj1-sv5-0103-cmls-01&up_admin=no"  -u 'username:password' https://192.168.0.10/api/1.0/switchports/ --insecure
done
