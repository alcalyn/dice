FROM resin/raspberry-pi-python:3.6-slim

RUN apt-get update && apt-get install -y \
        git \
        i2c-tools \
        python3-smbus \
        python-smbus \
	&& apt-get -y clean \
	&& apt-get -y purge \
        && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
