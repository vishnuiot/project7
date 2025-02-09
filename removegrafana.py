import os
import time
import subprocess

print('------------------------------------')
print('...Removing Grafana...\n\n')
os.system("sudo apt-get remove --auto-remove grafana -y && sudo apt-get purge --auto-remove grafana -y")
time.sleep(1)
print('------------------------------------')
print('...Cleaning Up...\n\n')

os.system("sudo apt-get autoclean && sudo apt-get autoremove")
time.sleep(1)
print('------------------------------------')
print('...Checking Left-Overs...\n\n')
os.system("sudo updatedb")
time.sleep(1)

cmd = "sudo locate grafana"
openCmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
fromCmd, stderr = openCmd.communicate()
cmds = fromCmd.decode().split('\n')
print('------------------------------------')
print('...Removing Left-Overs...\n\n')

for cmd in cmds[:-1]:
    print('----------')
    print('Removing: '+str(cmd))
    os.system('sudo rm -r '+ str(cmd))

print('------------------------------------')
print('All Done!\n\n')