#!/bin/bash -xe

docker run -it \
-h common-syslog \
-v $PWD/log:/var/log \
--rm \
syslog-server

