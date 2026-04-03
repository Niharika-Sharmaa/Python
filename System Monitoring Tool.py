import psutil
import time

def monitor():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent

        print(f"CPU Usage: {cpu}% | RAM Usage: {memory}%")
        time.sleep(1)

monitor()
