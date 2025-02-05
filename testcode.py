from datetime import datetime
import pandas as pd,os,psutil
# datetime object containing current date and time
now = datetime.now()
print(now)

t=psutil.sensors_temperatures()  # Temp tuple to be converted to integer
data = {
  "time":now ,
  "no_of_cores": [os.cpu_count()],
  "RAM"        : [psutil.virtual_memory()[2]]
  # "cpu_1_usage": [psutil.cpu_percent(1)],
  # "cpu_2_usage": [psutil.cpu_percent(2)],
  # "cpu_3_usage": [psutil.cpu_percent(3)],
  # "cpu_4_usage": [psutil.cpu_percent(4)],
  # "cpu_5_usage": [psutil.cpu_percent(5)],
  # "cpu_6_usage": [psutil.cpu_percent(6)],
  # "cpu_7_usage": [psutil.cpu_percent(7)],
  # "cpu_8_usage": [psutil.cpu_percent(8)],
  # "cpu_1_temp" : [int(t["coretemp"][1][1])],
  # "cpu_2_temp" : [int(t["coretemp"][1][1])],
  # "cpu_3_temp" : [int(t["coretemp"][1][1])],
  # "cpu_4_temp" : [int(t["coretemp"][1][1])]
      }
check=list(data.keys()) #list data from the set data
print (check)
vvv=list(data.values())
print(vvv)
print(len(data))

xxx={'tags':list(data)}
print(xxx)
print (type(data))


# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df) 
# # append data frame to CSV file
# df.to_csv('system_data.csv', mode='a', index=False, header=False)
# # prepare data for ingestion into influxdb
# #Invert data
# # data ={'value':[10,20],'tag1':['a','b']}
# empty = [] # Create an Empty list
# # Create an initialized list
# print(data)
# # points=[]
# # for index,row in df.iterrows():
# #   point={'measurement':'cpu_parameters','tags':{'tag1':row['tag1']},'time':None,'fields':{'value':row['value'] }}
# #   points.append(point)

# data ={'value':[now,[os.cpu_count()]],'Measurement_parameters':['time','no_of_cores']}
# df = pd.DataFrame(data)
# print(df)

# check=list
