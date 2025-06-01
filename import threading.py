import threading
import time

def worker(name, delay):
    for i in range(3):
        print(f"{name}: шаг {i+1}")
        time.sleep(delay)

thread1 = threading.Thread(target=worker, args=("Поток 1", 1))
thread2 = threading.Thread(target=worker, args=("Поток 2", 2.5))

thread1.start()
thread2.start()
print("Ожидание завершения потоков...")
thread1.join()
thread2.join()
