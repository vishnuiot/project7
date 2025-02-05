import pandas as pd

data ={'value':[10,20],'tag1':['a','b'],'tag2':['x','y']}
df = pd.DataFrame(data)
print(df)
points=[]
for index,row in df.iterrows():
  point={'measurement':'cpu_parameters','tags':{'tag1':row['tag1']},'time':None,'fields':{'value':row['value']} }
  points.append(point)
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
  bucket="db"

  client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
  # write_api = client.write_api(write_options=SYNCHRONOUS)


  write_api = client.write_api(write_options=SYNCHRONOUS)
  write_api.write(bucket=bucket, org="zurich", record=point)
  time.sleep(1) # separate points by 1 second
    
print(point)
