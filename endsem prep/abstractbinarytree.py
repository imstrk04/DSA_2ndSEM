from abc import ABC, abstractmethod
from abstracttree import AbstractTree

class AbstractBinaryTree(AbstractTree):
    @abstractmethod
    def left(self, pos):
        pass

    @abstractmethod
    def right(self, pos):
        pass

    def children(self, pos):
        if pos is None:
            return None
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)
    
    def sibling(self, pos):
        parent = self.parent(pos)
        if parent is None:
            return None
        if pos == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)


