#https://psutil.readthedocs.io/en/latest/
#!/usr/bin/env python
import psutil
# gives a single float value
cpu_usage=psutil.cpu_percent()
# gives an object with many fields
psutil.virtual_memory()
# you can convert that object to a dictionary 
dict(psutil.virtual_memory()._asdict())
# you can have the percentage of used RAM
cpu_mem=psutil.virtual_memory().percent
79.2
# you can calculate percentage of available memory
mem_avail=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
20.8

print("CPU_RAM usage  = ",cpu_mem)
print("CPU_usage = ",cpu_usage)
print("available memory =",mem_avail)

# from __future__ import print_function
import psutil
print("CPU percent=",psutil.cpu_percent())
print(psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])
