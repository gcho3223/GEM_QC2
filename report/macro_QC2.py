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

## date & folder
date_input = input("Enter the date (YYYYMMDD): ")
DataFolder = "QC2_results/data_ME0_foils_" + date_input
## megger
#megger_directory = DataFolder+"/megger"
#Megger = [f[:-4] for f in os.listdir(megger_directory) if f.endswith('.txt')]
## long
Long = [f[:-4] for f in os.listdir(DataFolder) if f.startswith('QC2LONG_PART1') and f.endswith('.txt')]
## All
AllChFile = next((f[:-4] for f in os.listdir(DataFolder) if f.startswith('QC2_all_channels_monitor') and f.endswith('.txt')), None)
## the number ofchannels
TestedChannel = [str(i) for i in range(len(Long))]

##### make report #####
for idx_c in range(len(TestedChannel)):
    if(Type == "megger"):
        cmd_megger = f'python3 QC2_megger_generator.py {date_input}'
        finmsg_megger = 'megger file is made!!'
        os.system(cmd_megger)
        print(finmsg_megger)
    elif(Type == "iv"):
        cmd_iv = 'python3 QC2_IV-plot-generator.py %s %s'%(DataFolder,TestedChannel[idx_c]) # IV plot
        finmsg_iv = 'IV plot & text file is made for Channel %s!!'%(TestedChannel[idx_c])
        print(cmd_iv)
        os.system(cmd_iv)
        print(finmsg_iv)
        print('All IV plots is finished!!!!!!')
    elif(Type == "report"):
        megger_directory = DataFolder+"/megger"
        Megger = [f[:-4] for f in os.listdir(megger_directory) if f.endswith('.txt')]
        cmd_report = 'python3 QC2_report.py %s %s %s %s'%(DataFolder,Long[idx_c],Megger[idx_c],AllChFile) # report
        finmsg_report = 'report for %s is made!!'%(Long[idx_c])
        print(cmd_report)
        os.system(cmd_report)
        print(finmsg_report)
        print('All repoart is finished!!!!!!')
if(Type == "all"):
    cmd_megger = f'python3 QC2_megger_generator.py {date_input}'
    finmsg_megger = 'megger file is made!!'
    os.system(cmd_megger)
    print(finmsg_megger)
    for idx_c in range(len(TestedChannel)):
        cmd_iv = 'python3 QC2_IV-plot-generator.py %s %s'%(DataFolder,TestedChannel[idx_c]) # IV plot
        finmsg_iv = 'IV plot & text file is made for Channel %s!!'%(TestedChannel[idx_c])
        print(cmd_iv)
        os.system(cmd_iv)
        print(finmsg_iv)
    for idx_c in range(len(TestedChannel)):
        megger_directory = DataFolder+"/megger"
        Megger = [f[:-4] for f in os.listdir(megger_directory) if f.endswith('.txt')]
        cmd_report = 'python3 QC2_report.py %s %s %s %s'%(DataFolder,Long[idx_c],Megger[idx_c],AllChFile) # report
        finmsg_report = 'report for %s is made!!'%(Long[idx_c])
        print(cmd_report)
        os.system(cmd_report)
        print(finmsg_report)
        print('All IV plots & repoart is finished!!!!!!')