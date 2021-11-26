from customNodeTwoWays import CustomNodeTwoWays


class CustomDoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        """ Append an item to the list. """
        new_node = CustomNodeTwoWays(data, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def delete(self, data):
        current = self.head
        node_deleted = False

        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.previous = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.previous
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    node_deleted = True
                    break

                current = current.next

        if node_deleted:
            self.count -= 1

        return node_deleted

    def iter(self, direction):
        if direction == 'desc':
            current = self.tail
            while current:
                val = current.data
                current = current.previous
                yield val
        elif direction == 'asc':
            current = self.head
            while current:
                val = current.data
                current = current.next
                yield val
        else:
            print("No way!")

    def contain(self, data):
        for node_data in self.iter('desc'):
            if data == node_data:
                return True

        return False

    def clear(self):
        """ Clear the entire list. """
        self.tail = None
        self.head = None
        self.count = 0
