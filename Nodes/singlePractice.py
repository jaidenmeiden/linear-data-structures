from customNode import CustomNode

# Creating a linked list
head = None
# Add five nodes to the beginning of the linked structure
for count in range(1, 3):
    head = CustomNode(count, head)
# Print the contents of the structure
while head is not None:
    print(head.data)
    head = head.next

print("+++++++++++++++++++++++++++")

""" Main linked lists operations """
# Traversal with 'probe' as aux. variable
probe = head

while probe is not None:
    print(probe.data)
    probe = probe.next

print("+++++++++++++++++++++++++++")

# Search an item
probe = head
target_item = 2
while probe is not None and target_item != probe.data:
    probe = probe.next

if probe is not None:
    print(f"Target item {target_item} has been found")
else:
    print(f"Target item {target_item} is not in the linked list")

print("+++++++++++++++++++++++++++")

# Replacement
probe = head
target_item = 3
new_item = "Z"
while probe is not None and target_item != probe.data:
    probe = probe.next

if probe is not None:
    probe.data = new_item
    print(f"{new_item} replaced the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")

# Insert new element at the beginning
head = CustomNode("F", head)

# Insert at the end
new_node = CustomNode("K")

print("+++++++++++++++++++++++++++")

if head is None:
    head = new_node
else:
    probe = head
    while probe.next is not None:
        probe = probe.next

    probe.next = new_node

# Remove at the beginning
removed_item = head.data
head = head.next
print("Removed item: ", removed_item)

print("+++++++++++++++++++++++++++")

# Remove at the end
removed_item = head.data

if head.next is None:
    head = None
else:
    probe = head

    while probe.next.next is not None:
        probe = probe.next

    removed_item = probe.next.data
    probe.next = None

print("Removed item: ", removed_item)

print("+++++++++++++++++++++++++++")

head = CustomNode("A", head)
head = CustomNode("B", head)
head = CustomNode("C", head)

# Insert at any position
new_item = input("Enter the new item: ")
index = int(input("Enter the position to insert the new item: "))

print("head: ", head)
print("index: ", index)

if head is None or index < 0:
    head = CustomNode("Py", head)
else:
    # Search for node at position index - 1 or the last position
    probe = head

    while index > 1 and probe.next is not None:
        probe = probe.next
        index -= 1

    probe.next = CustomNode(new_item, probe.next)

# Remove at any position
index = 3

if index <= 0 or head.next is None:
    removed_item = head.data
    head = head.next
    print("Removed item: ", removed_item)
else:
    # Search for nod at position index - 1
    # or the next to last position
    probe = head

    while index > 1 and probe.next.next is not None:
        probe = probe.next
        index -= 1

    removed_item = probe.next.data
    probe.next = probe.next.next
    print("Removed item: ", removed_item)
