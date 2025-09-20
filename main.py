# Week 2 – Logging System Info
# Use Copilot to help you complete the code

import psutil
from datetime import datetime

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log_line = f"[{now}] CPU: {cpu}% | MEM: {memory}% | DISK: {disk}%\n"
    return log_line

def write_log(log_line):
    with open("log.txt", "a") as f:
        f.write(log_line)

if __name__ == "__main__":
    line = get_system_info()
    print("Logging:", line)
    write_log(line)
