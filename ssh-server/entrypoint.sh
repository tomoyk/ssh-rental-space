#!/bin/bash -xe

SSH_CONF="/etc/ssh/sshd_config"
SSH_HOST=$(ifconfig eth0 | grep inet\ addr | awk '{print $2}' | cut -f2 -d':')
SYSLOG_SERVER="172.17.0.3"

echo -e "\n===== CHANGE RSYSLOG CONF ====="
echo "*.*@${SYSLOG_SERVER}:514" >> /etc/rsyslog.conf

echo -e "\n===== GENERATE SSH KEY ====="
ssh-keygen -A 

echo -e "\n===== CHANGE SSH CONF ====="
sed -i -e "s|#Port 22|Port $SSH_PORT|g" $SSH_CONF
sed -i -e "s|#PermitRootLogin prohibit-password|PermitRootLogin $PERMIT_ROOT_LOGIN|g" $SSH_CONF
sed -i -e "s|#MaxSessions 10|MaxSessions $MAX_SESSION|g" $SSH_CONF
sed -i -e "s|#Banner none|Banner /etc/ssh/sshd_banner|g" $SSH_CONF

echo -e "\n===== ADD SSH USER ====="
mkdir /www-data/public_html
adduser -h /www-data -s /bin/bash -D ${SSH_USER}
chown ${SSH_USER}:${SSH_USER} /www-data

echo -e "\n===== SET SSH PASSWORD ====="
echo "${SSH_USER}:${SSH_PASSWORD}" | /usr/sbin/chpasswd

echo -e "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - "
echo -e "| IPaddr:\t" ${SSH_HOST}
echo -e "| Port: \t" ${SSH_PORT}
echo -e "| User: \t" ${SSH_USER}
echo -e "| Pass: \t" ${SSH_PASSWORD}
echo -e "- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
echo -e "Command: ssh ${SSH_USER}@${SSH_HOST} -p ${SSH_PORT} -o PreferredAuthentications=password\n"

