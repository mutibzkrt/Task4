import sqlite3
from datetime import datetime

# Veritabanı bağlantısı oluşturma ve tablo oluşturma
def create_db():
    conn = sqlite3.connect('process_status.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS process_status (
            task_id INTEGER PRIMARY KEY,
            status TEXT,
            start_time TIMESTAMP,
            end_time TIMESTAMP,
            cpu_usage REAL,
            memory_usage REAL
        )
    ''')
    conn.commit()
    conn.close()

# Veritabanına kayıt ekleme
def log_to_db(task_id, status, start_time=None, end_time=None, cpu_usage=None, memory_usage=None):
    conn = sqlite3.connect('process_status.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO process_status (task_id, status, start_time, end_time, cpu_usage, memory_usage)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (task_id, status, start_time, end_time, cpu_usage, memory_usage))
    conn.commit()
    conn.close()

# Durumları sorgulama
def get_process_status():
    conn = sqlite3.connect('process_status.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM process_status')
    rows = cursor.fetchall()
    conn.close()
    return rows
