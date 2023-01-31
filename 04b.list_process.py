import psutil
listOfProcessNames = list()
# Iterate over all running processes
for proc in psutil.process_iter():
   # Get process detail as dictionary
   pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
   # Append dict of process detail in list
   listOfProcessNames.append(pInfoDict)


for elem in listOfProcessNames[:5] :
    print(elem)