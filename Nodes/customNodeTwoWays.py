"""
Nodes y singly linked list

The node methods should be incorporated into the Node class.
"""


class CustomNodeTwoWays(object):
    """Represents a single linked node."""

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous
