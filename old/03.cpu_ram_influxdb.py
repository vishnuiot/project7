#working demo code  -- Export token to connect
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import WriteApi, WriteOptions

token = os.environ.get("INFLUXDB_TOKEN")
url = "http://localhost:8086"
bucket="CPU_Bucket"
org="Zurich"
client = influxdb_client.InfluxDBClient(url=url,token=token,org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

import os
import psutil
cpu=psutil.cpu_percent(1)
print('The CPU usage is: ', cpu)

# write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

# for value in range(5):
#   point = (Point("measurement1").tag("tagname1", "tagvalue1").field("field1", value))
#   write_api.write(bucket=bucket, org="Zurich", record=point)
#   time.sleep(1) # separate points by 1 second
  
# write_api = client.write_api(write_options=SYNCHRONOUS)
# client = influxdb_client.InfluxDBClient(url=url,token=token,org=org)
# # #write
# point = (Point("measurement1").tag("tagname1", "tagvalue1").field("field1", cpu) )

# write_api.write(bucket=bucket, org=org, record=point)
# time.sleep(1) # separate points by 1 second



