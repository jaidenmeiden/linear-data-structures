from customNode import CustomNode

index = 1
new_item = "ham"

head = CustomNode(None, None)
head.next = head

# Search for node at position index - 1 or the last position
probe = head

while index > 0 and probe.next != head:
    probe = probe.next
    index -= 1

# Insert new node after node at position index - 1 or last position
probe.next = CustomNode(new_item, probe.next)

print(probe.next.data)
print(probe.next.next.data)
print(probe.next.next.next.data)
