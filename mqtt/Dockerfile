FROM debian:stretch

ARG  MOSQUITTOVERSION
ENV  MOSQUITTOVERSION 1.4.15


RUN apt-get update     && \
    apt-get upgrade -y && \
    apt-get install -y wget build-essential libwrap0-dev libssl-dev python-distutils-extra \
                       libc-ares-dev uuid-dev
RUN apt-get install -y libwebsockets-dev
RUN apt-get install -y gosu sudo

RUN     mkdir -p /mosquitto/src
WORKDIR          /mosquitto/src
RUN     wget http://mosquitto.org/files/source/mosquitto-$MOSQUITTOVERSION.tar.gz
RUN     tar xvzf ./mosquitto-$MOSQUITTOVERSION.tar.gz
WORKDIR /mosquitto/src/mosquitto-$MOSQUITTOVERSION
RUN     make WITH_WEBSOCKETS=yes && make install


WORKDIR /mosquitto

RUN mkdir -p /mosquitto/config /mosquitto/data /mosquitto/log
COPY ./mosquitto/config/mosquitto.conf /mosquitto/config/
COPY docker-entrypoint.sh /mosquitto/docker-entrypoint.sh


EXPOSE 1883
EXPOSE 9001

# RUN chown -R mosquitto:mosquitto /mosquitto

RUN ["chmod", "+x", "/mosquitto/docker-entrypoint.sh"]

ENTRYPOINT ["/mosquitto/docker-entrypoint.sh"]

CMD ["mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]
