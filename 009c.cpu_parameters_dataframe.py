import pandas as pd,os,psutil
# import os
# import psutil
print('The CPU usage is: ', psutil.cpu_percent(1))
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
print(now)

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

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 
# append data frame to CSV file
df.to_csv('system_data.csv', mode='a', index=False, header=False)

#Influxdb Section to upload CPU,Temp
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
# Section to load token
from dotenv import load_dotenv
import os
load_dotenv('apikey.env')
user = os.getenv('INFLUXDB_TOKEN')
#print (user)  prints api token - pre production

token = os.environ.get("INFLUXDB_TOKEN")
org = "zurich"
url = "http://localhost:8086"
bucket="cpu"


# write_api = client.write_api(write_options=SYNCHRONOUS)
# write_api.write(bucket=bucket, org="zurich", record=point)
# time.sleep(5) # separate points by 1 second
