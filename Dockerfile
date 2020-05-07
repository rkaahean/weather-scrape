FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade \
    && apt-get install python3.6 -y \
    && apt-get install python3-pip -y

RUN alias python=python3 && alias pip=pip3

COPY requirements.txt /tmp/


RUN pip3 install --upgrade --ignore-installed -r /tmp/requirements.txt



