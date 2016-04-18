from queue import Queue
from threading import Thread, Event

# A thread that produces data
def producer(out_q):
    while running:
    # Produce some data
    ...
    # Make an (data, event) pair and hand it to the consumer
    evt = Event()
    out_q.put((data, evt))
    ...
    # Wait for the consumer to process the item
    evt.wait()


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data, evt = in_q.get()
        # Process the data
        ...
        # Indicate completion
        evt.set()



