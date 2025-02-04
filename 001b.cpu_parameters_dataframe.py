import pandas as pd,os,psutil
# import os
# import psutil
print('The CPU usage is: ', psutil.cpu_percent(1))
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
print(now)

t=psutil.sensors_temperatures()
# conversion of tuple to integer
core_0=int(t["coretemp"][1][1])
core_1=int(t["coretemp"][2][1])
core_2=int(t["coretemp"][3][1])
core_3=int(t["coretemp"][4][1])




data = {
  "time":now ,
  "no_of_cores": [os.cpu_count()],
  "RAM"        : [psutil.virtual_memory()[2]],
  "cpu_1_usage": [psutil.cpu_percent(1)],
  "cpu_2_usage": [psutil.cpu_percent(2)],
  "cpu_3_usage": [psutil.cpu_percent(3)],
  "cpu_4_usage": [psutil.cpu_percent(4)],
  "cpu_5_usage": [psutil.cpu_percent(5)],
  "cpu_6_usage": [psutil.cpu_percent(6)],
  "cpu_7_usage": [psutil.cpu_percent(7)],
  "cpu_8_usage": [psutil.cpu_percent(8)],
  "cpu_1_temp" : [int(t["coretemp"][1][1])],
  "cpu_2_temp" : [int(t["coretemp"][1][1])],
  "cpu_3_temp" : [int(t["coretemp"][1][1])],
  "cpu_4_temp" : [int(t["coretemp"][1][1])]
      }

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 