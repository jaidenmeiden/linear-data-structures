from nodeQueue import NodeQueue

x = NodeQueue()

x.enqueue('eggs')
x.enqueue('ham')
x.enqueue('spam')
print("head.data: ", x.head.data)
print("head.next.data: ", x.head.next.data)
print("tail.data: ", x.tail.data)
print("tail.previous.data: ", x.tail.previous.data)
print("count: ", x.count)
x.dequeue()
print("head.data: ", x.head.data)
