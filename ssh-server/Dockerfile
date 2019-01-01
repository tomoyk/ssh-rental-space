FROM alpine:3.8

MAINTAINER Tomoyuki KOYAMA <webmaster@koyama.me>

ENV SSH_USER          guest22
ENV SSH_USER_UID      2000
ENV SSH_PASSWORD      L1nuxCLU8
ENV SSH_PORT          22
ENV MAX_SESSION       3
ENV PERMIT_ROOT_LOGIN no
ENV SYSLOG_SERVER     172.17.0.2
ENV SYSLOG_PORT       514

RUN apk add --update --no-cache openssh openssh-sftp-server tzdata rsyslog && \
    : "Configure timezone" && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    echo "Asia/Tokyo" > /etc/timezone && \
    apk del tzdata && \
    rm -rf /var/cache/apk/* 

EXPOSE $SSH_PORT

VOLUME /www-data
VOLUME /var/log

ADD ./entrypoint.sh /
ADD ./motd /etc
# ADD ./sshd_banner /etc/ssh

CMD /bin/sh /entrypoint.sh && \
    /bin/rm -f /entrypoint.sh && \
    /usr/sbin/sshd -4 -f /etc/ssh/sshd_config && \
    /usr/sbin/rsyslogd -f /etc/rsyslog.conf -n

