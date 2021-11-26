from queue import Queue

x = Queue()
x.enqueue(5)
x.enqueue(6)
x.enqueue(7)
print("inbound_stack: ", x.inbound_stack)
print("dequeue: ", x.dequeue())
print("inbound_stack: ", x.inbound_stack)
print("outbound_stack: ", x.outbound_stack)
print("dequeue: ", x.dequeue())
print("outbound_stack: ", x.outbound_stack)
