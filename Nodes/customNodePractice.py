from customNode import CustomNode

# Creating 3 differents nodes
node1 = None
node2 = CustomNode("A", None)
node3 = CustomNode("B", node2)
print("Memory node1", node1)
print("Memory node2", node2)
print(node2.data)
print(node2.next)
print("Memory node3", node3)
print(node3.data)
print(node3.next)
print(node3.next.data)

# This causes an Atribute Error
# node1.next = node3

node1 = CustomNode("C", node3)
print("Memory node1", node1)
print(node1.data)
print(node1.next.data)

print("+++++++++++++++++++++++++++++++")
head = None
for count in range(1, 5):
    head = CustomNode(count, head)

while head is not None:
    print(head.data)
    head = head.next
