FROM alpine:3.8

MAINTAINER Tomoyuki KOYAMA <webmaster@koyama.me>

RUN apk update && \
    apk add tzdata bash rsyslog && \
    : "Configure timezone" && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    echo "Asia/Tokyo" > /etc/timezone && \
    apk del tzdata && \
    rm -rf /var/cache/apk/* 

EXPOSE 514

# PROTOCOL:UDP
ENV SYSLOG_PORT=514

VOLUME /var/log

ADD ./entrypoint.sh /

CMD /bin/bash /entrypoint.sh && \
    /usr/sbin/rsyslogd -f /etc/rsyslog.conf -n

