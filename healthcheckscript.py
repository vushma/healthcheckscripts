import os
print("uptime and Load average for the server ")
os.system('uptime')
print("Ram utilization")
os.system('free -g')
print("disk utilization")
os.system('df -h')
