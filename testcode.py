# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
    
from dotenv import load_dotenv
import os
load_dotenv('apikey.env')
user = os.getenv('INFLUXDB_TOKEN')
print (user)

for x in range(4):
    print (('core_'+str(x)))