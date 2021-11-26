from customDoubleLinkedList import CustomDoubleLinkedList

# Create a doubly linked list with one node
list = CustomDoubleLinkedList()

# Add information
for data in range(1, 7):
    list.append(data)

print("Count: ", list.count)

# Print the contents of the linked list in reverse order
print("+++++++++++++++++++++++++++")

probe = list

for word in probe.iter("desc"):
    print(word)
print("+++++++++++++++++++++++++++")

node = 3
print(f"Node {node} was deleted: ", list.delete(node))
print("Count: ", list.count)

node = 10
print(f"Node {node} was deleted: ", list.delete(node))
print("Count: ", list.count)

print("+++++++++++++++++++++++++++")

for word in probe.iter("asc"):
    print(word)
print("+++++++++++++++++++++++++++")

for word in probe.iter("order"):
    print(word)
print("+++++++++++++++++++++++++++")

print(list.contain(3))

print("+++++++++++++++++++++++++++")

probe = list
