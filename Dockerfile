FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade \
    && apt-get install python3.6 -y \
    && apt-get install python3-pip -y \
    && apt-get install git -y \
    && apt-get install vim -y

RUN alias python=python3 && alias pip=pip3
RUN git clone https://github.com/rkaahean/weather-scrape.git ~/app

COPY requirements.txt /tmp/
COPY config.ini /root/app/

RUN pip3 install --upgrade --ignore-installed -r /tmp/requirements.txt

WORKDIR /root/app

ENTRYPOINT ["python3"]



