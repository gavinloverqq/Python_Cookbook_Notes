from queue import Queue
from threading import Thread
import random

# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        data = random.randint(0, 10)
        print("P ", data)
        out_q.put(data)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        # Process the data
        print("C ", data)
        # Indicate completion
        in_q.task_done()

# Create the shared queue and launch both threads
q = Queue(10)
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# Wait for all produced items to be consumed
q.join()