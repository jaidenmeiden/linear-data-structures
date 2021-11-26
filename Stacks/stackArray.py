from customStackArray import CustomStackArray


class StackArray:
    def __init__(self, size):
        self.top = None
        self.size = size
        self.node = CustomStackArray(size)

    def push(self):
        self.size += 1
        self.node.__append__(self.size)

    def pop(self):
        if self.node.__len__() > 0:
            val = self.size - 1
            self.node.__pop__(val)
            self.size -= 1
            return val
        else:
            return "The stack is empty"

    def peek(self):
        """If we have an element on top"""
        if self.node.__len__() > 0:
            return self.node.__getitem__(self.size - 1)
        else:
            return "The stack is empty"

    def clear(self):
        while self.node.__len__() > 0:
            self.pop()
