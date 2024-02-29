FROM python:3.8-alpine
RUN apk add iproute2 vim iputils-ping python3 py3-pip openjdk11 bash

WORKDIR /home
COPY testData /home/testData
COPY testPlan /home/testPlan
COPY configtestread.jar /home/
COPY configtestwrite.jar /home/
COPY benchmark.bash /home/
RUN chmod +x /home/benchmark.bash
