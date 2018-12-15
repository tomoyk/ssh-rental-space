#!/bin/bash -xe

docker run -it \
-h circleA \
-e SSH_USER=sshuser \
-e SSH_PASSWORD=StrongPassword1357 \
-e SSH_PORT=11122 \
ssh-server

