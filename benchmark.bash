#!/usr/bin/env bash
# setup netem env here
tc qdisc add dev lo root netem delay 250ms 10ms
java -jar configtestread.jar &
java -jar configtestwrite.jar
