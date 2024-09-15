#working demo code  -- Export token to connect
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import WriteApi, WriteOptions

token = os.environ.get("INFLUXDB_TOKEN")
org = "demo"
url = "http://localhost:8086"
bucket="demo_bucket"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)

for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="demo", record=point)
  time.sleep(1) # separate points by 1 second

# p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
# write_api.write(bucket=bucket, org=org, record=p)
