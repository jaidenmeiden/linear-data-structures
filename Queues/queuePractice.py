from queue import Queue

x = Queue()
x.enqueue(5)
x.enqueue(6)
x.enqueue(7)
print(x.inbound_stack)
x.dequeue()
print(x.inbound_stack)
print(x.outbound_stack)
x.dequeue()
print(x.outbound_stack)