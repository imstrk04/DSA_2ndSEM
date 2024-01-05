from abstracttreepranaav import AbstractTree, abstractmethod
class AbstractBinaryTree(AbstractTree):
    @abstractmethod
    def getLeft(self, pos):
        raise Exception("Not implemented")

    @abstractmethod
    def getRight(self, pos):
        raise Exception("Not implemented")

    def getChildren(self, pos):
        if pos is None:
            return None
        if self.getLeft(pos) is not None:
            yield self.getLeft(pos)
        if self.getRight(pos) is not None:
            yield self.getRight(pos)

    def sibling(self, pos):
        parent = self.getParent(pos)
        if parent is None:
            return None
        if pos == self.right(parent):
            return self.left(parent)
        else:
            return self.right(parent)