#https://psutil.readthedocs.io/en/latest/
#!/usr/bin/env python
import os
import psutil
print('The CPU usage is: ', psutil.cpu_percent(1))
print("The no of CPU's is :",os.cpu_count())
# print("CPU percent=",psutil.cpu_percent())
print(psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])
print(type(psutil.virtual_memory()[2]))
memory=psutil.virtual_memory()[2]
cpu_cores=os.cpu_count()
print(memory,cpu_cores)
memory_type=type(memory)
cpu_cores_type=type(cpu_cores)
print("The type of memory,cpu cores=",type(memory),type(cpu_cores))
print("The type of memory={} ,cpu cores={}".format (memory_type,cpu_cores_type))



#Influxdb Section to upload CPU,Temp
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


from dotenv import load_dotenv
import os
load_dotenv('apikey.env')
user = os.getenv('INFLUXDB_TOKEN')
#print (user)  prints api token - pre production

token = os.environ.get("INFLUXDB_TOKEN")
org = "zurich"
url = "http://localhost:8086"
bucket="cpu"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

point = (Point("cpu_memory").tag("memorytag", "memorytagvalue").field("cpumemoryvalue",memory))
point = (Point("cpu_memory").tag("corestag", "corestagvalue").field("corecountvalue",cpu_cores))

write_api = client.write_api(write_options=SYNCHRONOUS)
write_api.write(bucket=bucket, org="zurich", record=point)
time.sleep(1) # separate points by 1 second

