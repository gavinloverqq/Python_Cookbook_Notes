from queue import Queue
from threading import Thread
import random
import time

_sentinel = object() # 停止生产标准

# 生产者线程
def producer(out_q):
    while True:
        data = random.randint(0, 10) # 生产一个数字
        out_q.put(data)
        time.sleep(1) # sleep的值代表生产速度
        if data == 10: # 一旦生产出了10这个数字，则停止生产
            out_q.put(_sentinel)


# 消费者线程
def consumer(in_q):
    while True:
        data = in_q.get()
        if data is _sentinel: # 一旦遇到停止生产信号，则停止消费
            in_q.put(_sentinel)
            break
        print("C ", data) # 消费一个数字
        time.sleep(2) # sleep的值代表消费速度

q = Queue(5) # 初始化仓库大小
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()