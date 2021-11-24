"""
Nodes y singly linked list

The node methods should be incorporated into the Node class.
"""
from customNode import CustomNode


class CustomSingleLinkedList(object):
    """Represents a single linked node."""

    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        node = CustomNode(data)

        if self.tail is None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next

            current.next = node

        self.size += 1

    def depth(self):
        return str(self.size)

    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data

            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found!')

    def clear(self):
        self.tail = None
        self.size = 0
