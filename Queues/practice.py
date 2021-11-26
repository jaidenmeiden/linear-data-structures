from listQueue import ListQueue

x = ListQueue()
x.enqueue('eegs')
x.enqueue('ham')
x.enqueue('spam')
print("+++++++++++++++++++++++++++")
print(x.items)
print("+++++++++++++++++++++++++++")
x.traverse()
print("+++++++++++++++++++++++++++")
x.dequeue()
for i in range(x.size):
    print(x.items[i])
