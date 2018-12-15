FROM alpine:3.8

MAINTAINER Tomoyuki KOYAMA <webmaster@koyama.me>

ENV SSH_USER          guest22
ENV SSH_PASSWORD      L1nuxCLU8
ENV SSH_PORT          22
ENV MAX_SESSION       3
ENV PERMIT_ROOT_LOGIN no
ENV TZ                Asia/Tokyo

RUN apk update && \
    apk add openssh openssh-sftp-server bash tzdata rsyslog && \
    : "Configure timezone" && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/* 

EXPOSE $SSH_PORT

VOLUME /www-data
VOLUME /var/log

ADD ./entrypoint.sh /
ADD ./motd /etc
# ADD ./sshd_banner /etc/ssh

CMD /bin/bash /entrypoint.sh && \
    /bin/rm -f /entrypoint.sh && \
    /usr/sbin/sshd -4 -f /etc/ssh/sshd_config && \
    /usr/sbin/rsyslogd -f /etc/rsyslog.conf -n

