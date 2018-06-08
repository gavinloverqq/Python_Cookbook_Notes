#启动和停止线程

import time
from threading import Thread

# def countDown(n):
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#         time.sleep(1)
#
# from threading import Thread
# t = Thread(target=countDown, args=(15,), daemon=True)
# t.start()
# if t.is_alive():
#     print("alive")
# else:
#     print("die")
# t.join()


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate() # Signal termination
t.join()      # Wait for actual termination (if needed)

