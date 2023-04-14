From ubuntu:20.04

ENV DEBIAN_FRONTEND nointeractive

RUN apt-get update; \
	apt-get install -y \
        python3 \
        python3-pip \
        socat; \
    pip3 install \
        pytest \
        allure-pytest \
        pytest-xdist \
        eventlet \
        paramiko \
        pyserial \
        PyYAML; \
    mkdir -p /root/ltt

# # Open Comment if you need pytest installed with **allure**.
# ENV ALLURE_VERSION=2.21.0
# RUN apt-get install -y \
#         wget \
#         unzip\
#         openjdk-11-jdk; \
#     wget github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip; \
#     unzip allure-${ALLURE_VERSION}.zip; \
#     rm -rf allure-${ALLURE_VERSION}.zip \
#     ln -s `pwd`/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure

COPY ./ /root/ltt