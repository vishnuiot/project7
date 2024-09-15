#https://psutil.readthedocs.io/en/latest/
#!/usr/bin/env python
import os
import psutil
print('The CPU usage is: ', psutil.cpu_percent(1))
print("The no of CPU's is :",os.cpu_count())
# print("CPU percent=",psutil.cpu_percent())
print(psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])