from node import Node

class DNode(Node):
    __slots__ = ['prev']
    def __init__(self,item, next, prev = None):
        super().__init__(item, next)
        self.prev = prev
