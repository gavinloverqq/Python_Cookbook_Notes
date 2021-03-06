import threading

class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    _lock = threading.RLock()
    def __init__(self, initial_value = 0):
        self._value = initial_value

    def incr(self,delta=1):
        '''
        Increment the counter with locking
        '''
        with SharedCounter._lock:
            self._value += delta

    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        with SharedCounter._lock:
             self.incr(-delta)


def incrAndDecrMillion(sharedCounter):
    for x in range(1, 100000):
        sharedCounter.incr()
        sharedCounter.decr()
    print("sharedCounter done")

sharedCounter = SharedCounter(0)

for x in range(1, 20):
    t = threading.Thread(target=incrAndDecrMillion, args=(sharedCounter,))
    t.start()
    print(x, " thread started!")