#working demo code  -- Export token to connect
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import WriteApi, WriteOptions

token = os.environ.get("INFLUXDB_TOKEN")
org = "demo"
url = "http://localhost:8086"
bucket="check"

client = influxdb_client.InfluxDBClient(url=url,token=token,org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

import os
import psutil
cpu=psutil.cpu_percent(1)
print('The CPU usage is: ', cpu)
# print("The no of CPU's is :",os.cpu_count())

# for value in range(5):
point = (Point("measurement1").tag("tagname1", "tagvalue1").field("field1", cpu) )
write_api.write(bucket=bucket, org="demo", record=point)
time.sleep(1) # separate points by 1 second

