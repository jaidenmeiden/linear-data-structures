from customTwoWayNode import CustomTwoWayNode

# Create a doubly linked list with one node
head = CustomTwoWayNode(1)
tail = head

# Add four node to the end of the linked list
for data in range(2, 6):
    tail.next = CustomTwoWayNode(data, tail)
    tail = tail.next

# Print the contents of the linked list in reverse order
print("+++++++++++++++++++++++++++")

probe = tail

while probe is not None:
    print(probe.data)
    probe = probe.previous

print("+++++++++++++++++++++++++++")

probe = head

while probe is not None:
    print(probe.data)
    probe = probe.next