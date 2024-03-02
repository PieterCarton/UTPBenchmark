#!/usr/bin/env bash
# setup netem env here
tc qdisc add dev lo root netem delay 250ms 10ms loss 1\%
java -jar configtestread.jar &
java -jar configtestwrite.jar "testPlan/testplan2.csv" "testData/testfile.jpg" localhost 
