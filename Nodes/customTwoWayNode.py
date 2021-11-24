from customNode import CustomNode


class CustomTwoWayNode(CustomNode):
    def __init__(self, data, previous=None, next=None):
        CustomNode.__init__(self, data, next)
        self.previous = previous
