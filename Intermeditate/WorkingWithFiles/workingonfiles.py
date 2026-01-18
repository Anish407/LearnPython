##  pip install psutil - to install psutil package, it is not part of the standard library
# it is used to get information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.
# ex: System-level metrics like CPU and memory usage, process management, disk usage, network statistics, and sensor data.
# number of bytes read/written to disk, bytes sent/received, connections, interface stats
# Sensors (depending on OS): temperatures, battery, fans
import json

import psutil
from pprint import pprint
import os;

def print_system_process_info():
    all_processes = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        all_processes.append(p.info)  # p.info is already a dict

    pprint(all_processes)
    
def print_disk_partitions():
    print("Disk Partitions:")
    pprint(psutil.disk_partitions())
    print("---\n")

def print_os_info():
    print("---- OS name")
    print(os.name)
    print("---- OS environ")  
    pprint(os.environ)
    envs= json.dumps(dict(os.environ), indent=2)
    print(envs)
    print("------ specific env variables ------")
    print("PATH:", os.getenv('NUMBER_OF_PROCESSORS'))
    print("---- Current Working Directory")
    print(os.getcwd())
    print("---- List files in current directory")
    pprint(os.listdir('.'))
   
    
# print_system_process_info()
# print_disk_partitions()
print_os_info()




        