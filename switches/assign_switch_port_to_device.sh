#!/bin/bash

curl -X POST -d "port=SW2-P1&switch=sv5-rack2-switchB&device=some-server-01"  -u 'username:password' https://10.100.0.114/api/1.0/switchports/ --insecure
sleep 1

curl -X POST -d "port=SW2-P2&switch=sv5-rack2-switchB&device=some-server-02"  -u 'username:password' https://10.100.0.114/api/1.0/switchports/ --insecure
sleep 1

curl -X POST -d "port=SW2-P3&switch=sv5-rack2-switchB&device=some-server-03"  -u 'username:password' https://10.100.0.114/api/1.0/switchports/ --insecure
sleep 1

