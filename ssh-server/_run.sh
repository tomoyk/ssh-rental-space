#!/bin/bash -xe

docker run -it \
-h circleA \
-e SSH_USER=sshuser \
-e SSH_PASSWORD=StrongPassword1357 \
-e SSH_PORT=11122 \
-e SYSLOG_SERVER="172.17.0.2" \
-v $PWD/www-data:/www-data \
--rm \
ssh-server
