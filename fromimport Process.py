from multiprocessing import Process

def worker():
    print("Процесс работает")

if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    p.join()
