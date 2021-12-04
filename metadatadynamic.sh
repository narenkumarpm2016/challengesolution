#!/bin/bash
TOKEN=`curl --request PUT "http://169.254.169.254/latest/api/token" --header "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
curl --write-out "\n" --request GET "http://169.254.169.254/latest/dynamic/instance-identity/document" --header "X-aws-ec2-metadata-token: $TOKEN"
