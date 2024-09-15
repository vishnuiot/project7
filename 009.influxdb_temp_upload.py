#!/usr/bin/env python3
# The output is a named tuple, indexing pulls out the element
# Always export the influxdb passkey
import psutil
temperature=psutil.sensors_temperatures()
print(temperature)
CPU_usage = psutil.cpu_percent(interval=1, percpu=True)
print("consolidated CPU usage =",CPU_usage)
print(psutil.cpu_percent(0))

print("Number of cores in system =", psutil.cpu_count())

# <name of object>.<name of field> 

print(CPU_usage[0])

t=psutil.sensors_temperatures()
print(t["acpitz"] ,"\n")  
print(t["nvme"],"\n") 
print(t["coretemp"][0],"\n",t["coretemp"][1],"\n",t["coretemp"][2],"\n",t["coretemp"][3],"\n",t["coretemp"][4],"\n") 
print("core 0 temperature =",t["coretemp"][1][1])
print("core 1 temperature =",t["coretemp"][2][1])
print("core 2 temperature =",t["coretemp"][3][1])
print("core 3 temperature =",t["coretemp"][4][1])

# conversion of tuple to integer
core_0=int(t["coretemp"][1][1])
print(type(core_0))



import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org    = "IBM"
url    = "http://localhost:8086"
bucket  ="CPU"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
point = (Point("Cpu_temperature").tag("tagname1", "core1").field("core_0", core_0))
write_api.write(bucket=bucket, org="IBM", record=point)


# print out the query back from InfluxdB
query_api = client.query_api()
query = """from(bucket: "CPU")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "Cpu_temperature")"""
tables = query_api.query(query, org="IBM")

for table in tables:
  for record in table.records:
    print(record)