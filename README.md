# UTPBenchmark
WIP script for benchmarking UTP4j performance

# How to run
The benchmark can currently only be run on Linux. In order to run the benchmark, the following must be installed:
- Java 1.8+
- iproute 2

On linux, run: 

`sudo ./runbenchmark.bash [path/to/testplan.csv] [path/to/file/to/send]`

If no testplan is provided, the default testplan located in `testPlan/testplan2.csv` is used for the benchmark. See the `testPlan` section for all available test plan configurations.

# Benchmark configurations
This repository contains a number of pre-made UTP4J benchmark test configurations. The following test configuration CSV files can be found inside of the testPlan directory:
- *target_buffering_delay_benchmark.csv*: Test UTP configurations with target buffering delays (C_CNTRL_TARGET_MICROS) varying between 10ms to 300ms. As long as the estimated buffering delay stays below the target, the UTP4J algorithm will try to increase the congestion window. A higher target buffering delay makes the UTP algorithm more agressive, but might cause high congestion.
- *fast_resend_benchmark.csv*: Test UTP configurations with the number of skipped acknowledgements needed for fast retransmit (MAX_SKIP_RESEND) varying between 2 and 30. A low number of skipped acknowledgements might make UTP unnecessarily resend packages, while a high number of skipped acknowledgements might lead to long retransmission times.
- *pkt_size_benchmark.csv*: Test UTP configurations with varying packet sizes (MAX_PKT_SIZE, MIN_PKT_SIZE) and packet size modes (PKT_SIZE_MODE).
- *congestion_window_increase_benchmark.csv*: Test UTP configurations with the maximum congestion window varying from 3 kB to 15 kB.
- *skip_packets_until_ack_benchmark.csv*: Test UTP configurations with differing selective acknowledgement parameters.

# Benchmark Data Processing
To conveniently process the lengthy log files into a neat table, a log to .xlsx conversion script can be found in `dataFormatting/convert_testlog_to_excel.py`.
Inside the script, select the logfile to convert and the UTP parameters to display inside the resulting table.
Then run the script to get an excel file containing the averaged tranfer speeds of all repetitions of the same parameters. 