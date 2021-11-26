from customDoubleLinkedList import CustomDoubleLinkedList

# Create a doubly linked list with one node
list = CustomDoubleLinkedList()

# Add information
for data in range(1, 7):
    list.append(data)

print(list.count)

# Print the contents of the linked list in reverse order
print("+++++++++++++++++++++++++++")

probe = list

print(list.contain(3))

print("+++++++++++++++++++++++++++")

probe = list
