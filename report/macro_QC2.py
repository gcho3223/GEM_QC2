##################################
##                              ##
##  QC2 make a report           ##
##                              ##
##################################

import os
import sys
import shutil
import time

## Type
Type = str(sys.argv[1])
## channels
TestedChannel = [
    "0",
    #"1",
    #"2",
    #"3",
    #"4",
    #"5",
    #"6"
]
DataFolder = "data_ME0_foils_20241202"
AllChFile = "QC2_all_channels_monitor_20241203_07-27"
## megger
Megger = [
    "QC2FAST_ME0-G12-KR-B08-0034_20241129_13-23", #ch0
    #"QC2FAST_ME0-G12-KR-B08-0033_20241129_14-41", #ch1
    #"QC2FAST_ME0-G12-KR-B08-0032_20241129_16-00", #ch2
    #"QC2FAST_ME0-G12-KR-B08-0031_20241129_17-18", #ch3
    #"QC2FAST_ME0-G12-KR-B08-0036_20241129_18-36", #ch4
    #"QC2FAST_ME0-G12-KR-B08-0035_20241129_19-55", #ch5
    #"QC2FAST_ME0-G12-KR-B08-0030_20241129_21-13", #ch6
]
## long
Long = [
    "QC2LONG_PART1_ME0-G12-KR-B08-0034_20241202_14-35", #ch0
    #"QC2LONG_PART1_ME0-G12-KR-B08-0033_20241129_14-41", #ch1
    #"QC2LONG_PART1_ME0-G12-KR-B08-0032_20241129_16-00", #ch2
    #"QC2LONG_PART1_ME0-G12-KR-B08-0031_20241129_17-18", #ch3
    #"QC2LONG_PART1_ME0-G12-KR-B08-0036_20241129_18-36", #ch4
    #"QC2LONG_PART1_ME0-G12-KR-B08-0035_20241129_19-55", #ch5
    #"QC2LONG_PART1_ME0-G12-KR-B08-0030_20241129_21-13", #ch6
]

##### make report #####
for idx_c in range(len(TestedChannel)):
    if(Type == "iv"):
        cmd_iv = 'python3 QC2_IV-plot-generator.py %s %s'%(DataFolder,TestedChannel[idx_c]) # IV plot
        finmsg_iv = 'IV plot & text file is made for Channel %s!!'%(TestedChannel[idx_c])
        print(cmd_iv)
        os.system(cmd_iv)
        print(finmsg_iv)
        print('All IV plots is finished!!!!!!')
    elif(Type == "report"):
        cmd_report = 'python3 QC2_report.py %s %s %s %s'%(DataFolder,Long[idx_c],Megger[idx_c],AllChFile) # report
        finmsg_report = 'report for %s is made!!'%(Long[idx_c])
        print(cmd_report)
        os.system(cmd_report)
        print(finmsg_report)
        print('All repoart is finished!!!!!!')
if(Type == "all"):
    for idx_c in range(len(TestedChannel)):
        cmd_iv = 'python3 QC2_IV-plot-generator.py %s %s'%(DataFolder,TestedChannel[idx_c]) # IV plot
        finmsg_iv = 'IV plot & text file is made for Channel %s!!'%(TestedChannel[idx_c])
        print(cmd_iv)
        os.system(cmd_iv)
        print(finmsg_iv)
    for idx_c in range(len(TestedChannel)):
        cmd_report = 'python3 QC2_report.py %s %s %s %s'%(DataFolder,Long[idx_c],Megger[idx_c],AllChFile) # report
        finmsg_report = 'report for %s is made!!'%(Long[idx_c])
        print(cmd_report)
        os.system(cmd_report)
        print(finmsg_report)
        print('All IV plots & repoart is finished!!!!!!')