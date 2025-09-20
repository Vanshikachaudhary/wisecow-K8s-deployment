import psutil
import logging
from datetime import datetime

CPU_THRESHOLD = 80        
MEMORY_THRESHOLD = 80     
DISK_THRESHOLD = 80       
PROCESS_THRESHOLD = 200   

LOG_FILE = "system_health.log"

# Setup logging

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_alert(message):
    """Log alert to console and log file."""
    print("[ALERT]", message)
    logging.warning(message)

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage normal: {cpu_usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        log_alert(f"High Memory usage detected: {memory.percent}%")
    else:
        logging.info(f"Memory usage normal: {memory.percent}%")

def check_disk():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        log_alert(f"Low Disk Space detected: {disk.percent}% used")
    else:
        logging.info(f"Disk usage normal: {disk.percent}% used")

def check_processes():
    num_processes = len(psutil.pids())
    if num_processes > PROCESS_THRESHOLD:
        log_alert(f"High number of running processes: {num_processes}")
    else:
        logging.info(f"Process count normal: {num_processes}")

def main():
    print("Running System Health Check...")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    print("Check complete. See log file for details.")

if __name__ == "__main__":
    main()