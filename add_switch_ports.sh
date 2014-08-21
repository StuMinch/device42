#!/bin/bash
for i in {6..48}
do
   curl -X POST -d "port=SW1-P5&switch=sj1-sv5-0103-cmls-01&up_admin=no"  -u 'username:password' https://192.168.0.10/api/1.0/switchports/ --insecure
done
