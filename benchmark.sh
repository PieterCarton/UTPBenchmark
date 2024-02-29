#!/usr/bin/env bash
# setup netem env here
java -jar configtestread.jar &
java -jar configtestwrite.jar testPlan/testplan2.csv testData/testfile.jpg