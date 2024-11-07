import psutil
import os
import time

# Kaynak kullanımını loglama
def log_resource_usage(task_id):
    process = psutil.Process(os.getpid())  # Mevcut işlem id'sini al
    while True:
        cpu_usage = process.cpu_percent(interval=1)  # CPU kullanımı
        memory_info = process.memory_info()  # RAM kullanımı
        print(f"Task {task_id} - CPU: {cpu_usage}% - RAM: {memory_info.rss / 1024 / 1024} MB")
        time.sleep(1)  # Her saniye bir kez kontrol et
