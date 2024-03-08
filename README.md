# UTPBenchmark
WIP script for benchmarking UTP4j performance

# How to run
On linux, run: 

`./runbenchmark.bat [path/to/testplan.csv]`

On windows, run:

`./runbenchmark.bat [path/to/testplan.csv]`

If no testplan is provided, the default testplan located in `testPlan/testplan2.csv` is used for the benchmark. See the `testPlan` for all available test plan configurations.

# Benchmark configurations
This repository contains a number of pre-made UTP4J benchmark test configurations. The following test configuration CSV files can be found inside of the testPlan directory:
- *target_buffering_delay_benchmark.csv*: Test UTP configurations with  target buffering delays (C_CNTRL_TARGET_MICROS) varying between 10ms to 300ms. As long as the estimated buffering delay stays below the target, the UTP4J algorithm will try to increase the congestion window. A higher target buffering delay makes the UTP algorithm more agressive, but might cause high congestion.
` *fast_resend_benchmark*: lorum ipsum