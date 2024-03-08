import pandas as pd
import openpyxl
import numpy as np

### Testplan parameter indices
PARAMETER_NAMES = ["MAX_TIMEOUT_MILLIS", 
                    "MAX_TIMEOUT_MILLIS",
                    "PKT_SIZE_MODE",
                    "MAX_PKT_SIZE",
                    "MIN_PKT_SIZE",
                    "MIN_MTU",
                    "MAX_CWND_INC",
                    "C_CNTRL_TARGET_MICROS",
                    "SEND_IN_BURST",
                    "MAX_BURST",
                    "MAX_SKIP_RESEND",
                    "MICROS_WAIT_BURST",
                    "TIME_WAIT_AFTER_FIN",
                    "ONLY_POS_GAIN",
                    "REPETITION"]

MAX_TIMEOUT_MILLIS = 0
PKT_SIZE_MODE = 1 
MAX_PKT_SIZE = 2 
MIN_PKT_SIZE = 3 
MIN_MTU = 4 
MAX_CWND_INC = 5
C_CNTRL_TARGET_MICROS = 6 
SEND_IN_BURST = 7
MAX_BURST = 8
MAX_SKIP_RESEND = 9
MICROS_WAIT_BURST = 10 
TIME_WAIT_AFTER_FIN = 11 
ONLY_POS_GAIN = 12 
REPETITION = 13
###


file_name = "AutoTestLog.txt"
params_to_display = [PKT_SIZE_MODE, MAX_PKT_SIZE, MIN_PKT_SIZE]
f = open(file_name, "r")

previous_params = None
previous_transfer_speeds = []
rows = []

for test_run in f:
    test_params, _, transfer_speed, cpu_usage = test_run.replace(" ", "").split("--")

    if previous_params != test_params:
        if previous_params != None:
            param_selection = [previous_params.split(";")[i] for i in params_to_display]
            rows.append(param_selection + [np.round(np.average(previous_transfer_speeds)),
                                           np.round(np.max(previous_transfer_speeds)),
                                           np.round(np.min(previous_transfer_speeds)),
                                           np.round(np.median(previous_transfer_speeds))])
        previous_params = test_params
        previous_transfer_speeds = []

    previous_transfer_speeds.append(int(transfer_speed.replace("kB/sec", "")))

param_selection = [previous_params.split(";")[i] for i in params_to_display]
rows.append(param_selection + [np.round(np.average(previous_transfer_speeds)),
                                np.round(np.max(previous_transfer_speeds)),
                                np.round(np.min(previous_transfer_speeds)),
                                np.round(np.median(previous_transfer_speeds))])

df = pd.DataFrame(rows, index=None, columns=[PARAMETER_NAMES[i] for i in params_to_display]+["Average Transfer Speed (kB/s)", "Maximum Transfer Speed (kB/s)", "Minimum Transfer Speed (kB/s)", "Median Transfer Speed (kB/s)"])
df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')