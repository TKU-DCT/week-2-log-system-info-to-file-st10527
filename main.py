# Week 2 – Logging System Info
# Use Copilot to help you complete the code

import psutil
from datetime import datetime

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # TODO: Use psutil to get CPU, memory, and disk usage
    cpu = 
    memory = 
    disk = 

    log_line = f"[{now}] CPU: {cpu}% | MEM: {memory}% | DISK: {disk}%\n"
    return log_line

def write_log(log_line):
    # TODO: Open 'log.txt' in append mode and write the log_line
    pass

if __name__ == "__main__":
    line = get_system_info()
    print("Logging:", line)
    write_log(line)
