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
cpu_core_usage_type=type(psutil.cpu_percent(1))
print("The type of memory,cpu cores=",type(memory),type(cpu_cores))
print("The type of memory={} ,cpu cores={}".format (memory_type,cpu_cores_type))

t=psutil.sensors_temperatures()
coretemp1=t["coretemp"][1][1]
coretemp2=t["coretemp"][2][1]
coretemp3=t["coretemp"][3][1]
coretemp4=t["coretemp"][4][1]
print("core 0 temperature =",t["coretemp"][1][1])
print("core 1 temperature =",t["coretemp"][2][1])
print("core 2 temperature =",t["coretemp"][3][1])
print("core 3 temperature =",t["coretemp"][4][1])
temperature_type=type(t["coretemp"][1][1])

for cores in range(1,5):
    print('The Independent CPU usage is: ', psutil.cpu_percent(cores))


print("The type of memory,cpu cores=",type(memory),type(cpu_cores))
print("The type of memory={} ,cpu cores={}".format (memory_type,cpu_cores_type))
print("Data type= memory={} ,cpu cores={} ,temperature={},cpu_usage 1(4)={}".format (memory_type,cpu_cores_type,temperature_type,cpu_core_usage_type))


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

point = (Point("cpu_parameters").tag("memorytag", "memorytagvalue").field("cpumemoryvalue",memory))
point = (Point("cpu_parameters").tag("corestag", "corestagvalue").field("corecountvalue",cpu_cores))
point = (Point("cpu_parameters").tag("coretemp1tag", "coretemp1tagvalue").field("coretemp_1_value",coretemp1))
point = (Point("cpu_parameters").tag("coretemp2tag", "coretemp2tagvalue").field("coretemp_2_value",coretemp2))
point = (Point("cpu_parameters").tag("coretemp3tag", "coretemp3tagvalue").field("coretemp_3_value",coretemp3))
point = (Point("cpu_parameters").tag("coretemp4tag", "coretemp4tagvalue").field("coretemp_4_value",coretemp4))


write_api = client.write_api(write_options=SYNCHRONOUS)
write_api.write(bucket=bucket, org="zurich", record=point)
time.sleep(1) # separate points by 1 second

