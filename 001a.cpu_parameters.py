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
core_1=int(t["coretemp"][2][1])
core_2=int(t["coretemp"][3][1])
core_3=int(t["coretemp"][4][1])
print(type(core_0))
# Type to check for integer,float,string
memory_type=type(memory)
cpu_cores_type=type(cpu_cores)
print("The type of memory,cpu cores=",type(memory),type(cpu_cores))
#print('I have {} {}'.format(a, b))
print("The type of memory={} ,cpu cores={}".format (memory_type,cpu_cores_type))


for cores in range(1,5):
    print('The Independent CPU usage is: ', psutil.cpu_percent(cores))
    
    
