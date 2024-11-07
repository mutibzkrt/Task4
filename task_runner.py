import multiprocessing
import time
from database import log_to_db
from resource_monitor import log_resource_usage

# İşlem fonksiyonu
def run_task(task_id):
    start_time = time.time()
    log_to_db(task_id, 'started', start_time=start_time)
    
    # Kaynak kullanımı izleme (arka planda)
    log_resource_usage(task_id)
    
    # İşlem simülasyonu
    time.sleep(2)  # 2 saniyelik bir işlem simülasyonu
    
    end_time = time.time()
    log_to_db(task_id, 'finished', start_time=start_time, end_time=end_time)

# İşlem başlatma
def start_processes():
    processes = []
    for i in range(1000):  # 1000 işlem
        process = multiprocessing.Process(target=run_task, args=(i,))
        processes.append(process)
        process.start()

    # Tüm işlemlerin bitmesini bekleyin
    for process in processes:
        process.join()
