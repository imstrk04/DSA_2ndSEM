from abc import ABC, abstractmethod

class AbstractTree():
    @abstractmethod
    def root(self):
        pass
    
    @abstractmethod
    def parent(self, pos):
        pass

    @abstractmethod
    def num_children(self, pos):
        pass

    @abstractmethod
    def children(self, pos):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def isRoot(self, pos):
        return self.root() == pos
    
    def isLeaf(self, pos):
        return self.num_children(pos) == 0
    
    def isEmpty(self):
        return self.root == None
    
    def depthN(self, pos):
        if self.isRoot(pos):
            return 0
        else:
            return self.depthN(self.parent(pos)) + 1
    
    def heightN(self, pos):
        if self.isLeaf(pos):
            return 0
        else:
            return max(self.heightN(child)for child in self.children(pos)) + 1
    
    def height(self,pos = None):
        if pos == None:
            if self.isEmpty is not True:
                return -1
            pos = self.root()
            return self.heightN(pos)
        
class AbstractBinaryTree(AbstractTree):
    @abstractmethod
    def left(self, pos):
        pass

    @abstractmethod
    def right(self, pos):
        pass

    def children(self,pos):
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
    
class LinkedBinaryTree(AbstractBinaryTree):
    class BTNode:
        __slots__ = ['item', 'left', 'right','parent']
        def __init__(self, item, left = None, right = None, parent = None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent
        
        def getitem(self):
            return self.item
        
        def setitem(self, ele):
            self.item = ele
    
    __slots__ = ['_root', 'size']
    def __init__(self, item = None, Tleft = None, Tright = None, parent = None):
        self._root = None
        self.size = 0
        if item is not None:
            self._root = self.addroot(item)
            if Tleft._root is not None:
                Tleft._root.parent = self._root
                self._root.left = Tleft._root
                self.size += Tleft.size
                Tleft._root = None
                Tleft.size = 0
            if Tright._root is not None:
                Tright._root = self._root
                self._root.right = Tright._root
                self.size += Tright.size
                Tright._root = None
                Tright.size = 0

    def addroot(self, item):
        if self._root is not None:
            raise ValueError("Root already Exist")
        self._root = self.BTNode(item)
        self.size += 1
        return self._root
    
    def __len__(self):
        return self.size
    
    def parent(self, pos):
        return pos.parent
    
    def left(self, pos):
        return pos.left 
    
    def root(self):
        return self._root
    
    def addLeft(self,item, pos):
        if self.left(pos) is not None:
            raise ValueError("Left Child already exists.")
        pos.left = self.BTNode(item, parent = pos)
        self.size += 1
        return pos.left
    
    def addRight(self, item, pos):
        if self.right(pos) is not None:
            raise ValueError("Right Child already exists.")
        pos.right = self.BTNode(item, parent = pos)
        self.size += 1
        return pos.right

    def preorder(self, pos):
        res = ""
        res = f"{pos.item}"
        if pos.left is not None:
            res += self.preorder(pos.left)
        if pos.right is not None:
            res += self.preorder(pos.right)
        return res

    def inorder(self, pos):
        res = ""
        if pos.left is not None:
            res = self.inorder(pos.left)
        res += f"{pos.item}"
        if pos.right is not None:
            res += self.inorder(pos.right)
        return res

    def preorder(self, pos):
        res = ""
        if pos.left is not None:
            res = self.preorder(pos.left)
        if pos.right is not None:
            res += self.preorder(pos.right)
        res += f"{pos.iten}"
        return res
    
    def __str__(self):
        return str(self.preorder(self._root))

    def num_children(self, pos):
        if pos is None:
            return 0
        else:
            return 1 + self.num_children(pos.left) + self.num_children(pos.right)
        
class ExpressionTree(LinkedBinaryTree):
    def __init__(self, item = None, Tleft = None, Tright = None):
        super().__init__(item, Tleft, Tright)
    
    def construct(self, expr):
        S = []
        for ch in expr:
            if ch in "+*-/":
                rchild = S.pop()
                lchild = S.pop()
                S.append(ExpressionTree(ch, lchild, rchild))
            else:
                S.append(ExpressionTree(ch))
        return S.pop()
    
    def inorder(self, pos):
        res = ""
        if pos is None:
            return None
        if pos.left is not None:
            res += self.inorder(pos.left)
        res += str(pos.item)
        if pos.right is not None:
            res += self.inorder(pos.right)
        return res
    