#Basic program to upload data into influxdb
#!/usr/bin/python
import pandas as pd,time,datetime
import numpy as np,os,sys,json,dateutil.parser
from pandas import DataFrame, read_csv
from datetime import timedelta, date
from decimal import Decimal

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

csv_filename="dataset1"+".csv"

# Initialize influxdb
token = os.environ.get("INFLUXDB_TOKEN")
org = "IBM"
url = "http://localhost:8086"
bucket="test"

# decimal not default float64
def decimal_from_value(value):
    return Decimal(value)

# creating a data frame
df=pd.DataFrame()
df=pd.read_csv(csv_filename,converters={'Lat': decimal_from_value})
size_df=len(df)
print (df)
print(size_df)
# columns for database
time=pd.Timestamp.now()  
journal_name=df['Journal_name']
impact_factor=df['Impactfactor']
university_name=df['University_name']
Latitude=df['Lat'][1]
Longitude=df['Long'][1]
print(Latitude)



# Influxdb write operation


client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "university of chicago").field("Latitude",Latitude,)
p = influxdb_client.Point("my_measurement").tag("location", "university of chicago").field("Longitude",Longitude)

# p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
# write_api.write(bucket=database, org=org, record=p)
