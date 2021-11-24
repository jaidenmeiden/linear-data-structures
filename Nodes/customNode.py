"""
Nodes y singly linked list

The node methods should be incorporated into the Node class.
"""


class CustomNode(object):
    """Represents a single linked node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
