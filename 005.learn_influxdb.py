#Basic program to upload data into influxdb
#!/usr/bin/python
import pandas as pd,time,datetime
import numpy as np,os,sys,json,dateutil.parser
from pandas import DataFrame, read_csv
from datetime import datetime,timedelta, date
from decimal import Decimal

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


# Initialize influxdb
token = os.environ.get("INFLUXDB_TOKEN")
org = "IBM"
url = "http://localhost:8086"
bucket="test"

with InfluxDBClient(url=url,token=token,org=org,debug=False)as client:
    # create a point with my data
    p=Point("my_measurement").tag("location","prague").field("temperatur",25).time(datetime.utcnow(),WritePrecision.MS)
    
    #get the write api
    write_api=client.write_api()    
    
    #write api using point structure
    write_api.write(bucket=bucket,record=p)
    
    
    
