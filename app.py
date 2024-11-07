from task_runner import start_processes
from database import create_db

if __name__ == '__main__':
    # Veritabanı oluşturma
    create_db()

    # İşlemleri başlatma
    start_processes()
