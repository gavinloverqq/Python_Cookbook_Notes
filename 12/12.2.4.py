import threading
import time

# Worker thread
def worker(n, sema):
    # Wait to be signaled
    sema.acquire()

    # Do some work
    print('Working', n)

# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

# 为什么此处输出是按顺序的，而不是乱序的？？？
for x in range(10):
    y = input()
    sema.release()

