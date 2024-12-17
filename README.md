# 📦Dependancies
- need to install the following packages
```
pip install numpy==1.22.4
pip install matplotlib
pip install scipy
pip install pandas
pip install fpdf
pip install mplhep
pip install openpyxl
```

# 💡How to run
```
python3 macro_QC2.py <option>
```
```option``` is ```megger```, ```iv```, ```report```, ```all```   
```megger```: make megger file   
```iv```: make IV plot   
```report```: make report   
```all```: make all steps (megger->iv->report)

# ⚠️Importances & Notes
- You should **right the date**   
- **Do not change the file name**   
- All steps can be done individually, but **make the megger file first**   
- If you want to make report, you should **make the IV plot first** 

# 🏹Sequence
- ```macro.QC2.py all``` will be followed by megger generator, IV plot generator, and report generator   
1. megger generator (```QC2_megger_generator.py <date>```)     
    - will be recieved from you, and you should input the megger data in the megger generator   
2. IV plot generator (```QC2_IV-plot-generator.py <data_folder> <index_to_open>```)    
    - will make the IV plots and save it in ```IVplot``` directory   
3. report generator (```QC2_report.py <data_folder> <long_file_name> <megger_file_name> <all_channels_file_name>```)   
    - to make the report file, need to have the IV plot file and megger file   
    - will make the report file and save it in ```pdf_reports``` directory   

## 1. 📑Megger Generator
```python3 QC2_megger_generator.py <date>``` or ```python3 macro_QC2.py megger```   
1. enter the date in the format of ```YYYYMMDD```   
then, megger directory will be created in ```QC2_results/data_ME0_foils_<date>``` and start entering the megger data   
```   
Enter the date (YYYYMMDD):   
'megger' directory has been created: QC2_results/data_ME0_foils_<date>/megger   
start entering the QC2FAST data for the file:  QC2FAST_ME0-<type>-KR-<batch>-<foil number>_<date>_<time>.txt   
Imp Spark @ 0.5 min:   
```
2. enter the megger data <Imp> <number of sparks>
```
Imp Spark @ 0.5 min: 70 0   
```
3. When you finish entering the megger data, check it
```
File content:
Time (minutes)  Impedance (GOhm)        Sparks
0.5     100     0
1       100     0
2       23      0
3       23      0
4       100     0
5       100     0

Is the content correct? (y/n):
```
4-1. if the values are correct, enter ```y```
```
Is the content correct? (y/n): y
file has been created: QC2_results/data_ME0_foils_<date>/megger/QC2FAST_ME0-<type>-KR-<batch>-<foil number>_<date>_<time>.txt
start entering the QC2FAST data for the file:  QC2FAST_ME0-<type>-KR-<batch>-<foil number>_<date>_<time>.txt
```
and entering the megger values for next foil   
4-2. if not, enter ```n``` and change the values
```
Is the content correct? (y/n): n
Enter the wrong time:
```
5. enter the wrong time, and enter the correct values
```
Enter the wrong time: 2
Imp Spark @ 2.0 min:
```
6. check the values again, and enter ```y``` or ```n```

## 2. 📈IV Plot Generator
```python3 macro_QC2.py iv```   
- enter the date
- the generator will runinng for the number of indices of the foils   
```python3 QC2_IV-plot-generator.py <data_folder> <index_to_open>```
- this is also the same as the megger generator, but the generator will run for the number of indices of the foils   
- ```index_to_open``` is the index of the foil to open, not the foil channel number!!   
- iv plots will be saved in ```IVplot``` directory   
```
📂 IVplot   
├── 📂txt   
│ └── 📜QC2LONG_PART1_*IVplot.txt
└── 📜QC2LONG_PART1_*IVplot.png
```
## 3. 📈Report Generator
```python3 macro_QC2.py report```   
- enter the date
- the generator will run for all foils to make the report      
```python3 QC2_report.py <data_folder> <long_file_name> <megger_file_name> <all_channels_file_name>```
- this is also generating the report file for the foil     