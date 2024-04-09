import psutil

CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80  


def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"CPU usage is {cpu_percent}% which exceeds threshold of {CPU_THRESHOLD}%")
        


def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        print(f"Memory usage is {memory_percent}% which exceeds threshold of {MEMORY_THRESHOLD}%")
        


def check_disk_usage():
    disk_percent = psutil.disk_usage('/').percent
    if disk_percent > DISK_THRESHOLD:
        print(f"Disk usage is {disk_percent}% which exceeds threshold of {DISK_THRESHOLD}%")
        

def check_running_processes():
    num_processes = len(psutil.pids())
    print(f"Number of running processes: {num_processes}")


def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
