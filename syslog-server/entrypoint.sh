#!/bin/bash -xe

SYSLOG_CONF="/etc/rsyslog.conf"
SYSLOG_HOST=$(ifconfig eth0 | grep inet\ addr | awk '{print $2}' | cut -f2 -d':')

sed -i -e "s|#\$ModLoad imudp.so|\$ModLoad imudp.so|g" $SYSLOG_CONF
sed -i -e "s|#\$UDPServerRun 514|\$UDPServerRun $SYSLOG_PORT|g" $SYSLOG_CONF

echo -e "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - "
echo -e "| IPaddr: \t" $SYSLOG_HOST
echo -e "| Port: \t" $SYSLOG_PORT "/ UDP"
echo -e "- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"

