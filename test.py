#This script is used to collect CPU parameters and save them in a CSV file
# It also processes the data for ingestion into InfluxDB
# and prepares it in a format suitable for uploading to InfluxDB.
# It uses the psutil library to gather system information and pandas for data manipulation.
# The script is designed to run in a specific directory and assumes that the necessary libraries are installed
from datetime import datetime
import pandas as pd,os,psutil,numpy as np
# Important to specify working directory in os.chdir
os.chdir("/home/vishnu/Documents/002.influxdb_docker/project7_CPU_parameters")



# datetime object containing current date and time
now = datetime.now()             # Time for recording into data frame
t=psutil.sensors_temperatures()  # Temp tuple to be converted to integer
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

#load raw data into a DataFrame object for saving as csv:Data can be passed only as a list
df = pd.DataFrame(data)
print(df) 
# append data frame to CSV file
df.to_csv('system_data.csv', mode='a', index=False, header=True)# Change header =False if header is not required

# process data for ingestion into influxdB
influxdb_df=df.drop(['time'],axis=1)
# print(influxdb_df)
tag1=list(influxdb_df.keys())
# print(tag1)
# print(type(tag1))
# print(len(tag1))


value=influxdb_df.values.tolist()
value = np.array(value)
value=value.flatten().tolist()
# print (value)
# print(type(value))
# print(len(value))


data_for_influxdb={'value':value,'tag1':tag1}
# print(data_for_influxdb)
df = pd.DataFrame(data_for_influxdb)
print(df)
