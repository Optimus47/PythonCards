from multiprocessing import Process

def worker():
    print("Процесс работает")

p = Process(target=worker)
p.start()
p.join()
