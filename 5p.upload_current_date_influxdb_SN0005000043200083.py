#!/usr/bin/python
import pandas as pd,time,datetime
import numpy as np,os,sys,json,dateutil.parser
from influxdb import InfluxDBClient
from pandas import DataFrame, read_csv
from datetime import timedelta, date
dbname ="SN0005000043200083"
os.chdir("/home/vishnu/darfondata/"+dbname)

currentdate_filename=datetime.datetime.now().strftime("%Y%m%d")+'.csv'
df=pd.DataFrame()
dg=pd.read_csv(currentdate_filename)
df=df.append(dg,ignore_index=True)
print currentdate_filename

df.insert(1,'Timeadjusted',0) # df.insert(idx,col_name,value)
df['Timeadjusted'] = pd.to_datetime(df.Time)-pd.Timedelta(hours=8,minutes=15)
#print df
size=len(df) 
print 'original df size=',size

#Identify and drop NAN Values
tt=df[df['Timeadjusted'].isnull()]
print tt
df=df.dropna()

dg=pd.DataFrame()
df=dg.append(df,ignore_index=True)
newsize=len(df) 
print 'new size=',newsize
# columns for database
timeadjustedcolumn=pd.to_datetime(df['Timeadjusted'].astype(int))[:]
tempcolumn=df['Temperature']
EACcolumn=df['Eac_Today']
VPVcolumn=df['Vpv']
IACcolumn=df['Iac']
VACcolumn=df['Vac']
PACcolumn=df['Pac']
FACcolumn=df['Fac']
EAC_TOTAL=df['Eac_Total']
IPVcolumn=df['Ipv']
PPVcolumn=df['Ppv']
#print "analyzed time values = \n",timeadjustedcolumn  # prints converted time column values
#print df
#INFLUXDB
# The database we created
dbname =dbname
host="localhost"
port = 8086
user = "root"
password = "root"
invertorID=dbname
# Create the InfluxDB object
client = InfluxDBClient(host, 8086, user, password,dbname )
client.create_database(dbname)

for i in range(newsize):
#	print 'currentfile=',newsize
	json_body = [{
                "measurement":invertorID,
                "tags":{"col3": "col3"},
                "time":timeadjustedcolumn[i],
                "fields":{"temperature":tempcolumn[i],
                "Eac_today":EACcolumn[i],
                "Vpv":VPVcolumn[i],
                "Iac":IACcolumn[i],
                "Vac":VACcolumn[i],
                "Pac":PACcolumn[i],
                "Fac":FACcolumn[i],
                "Eac_Total":EAC_TOTAL[i],
                "Ipv":IPVcolumn[i],
                "Ppv":PPVcolumn[i]}}]
	client.write_points(json_body)

