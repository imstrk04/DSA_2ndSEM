from abstractbinarytree import AbstractBinaryTree

class LinkedBinaryTree(AbstractBinaryTree):
    class BTNode:
        __slots__ = ['item', 'left', 'right', 'parent']
        def __init__(self, item, left=None, right=None, parent=None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent
        
        def getitem(self):
            return self.item
        
        def setitem(self, ele):
            self.item = ele

    __slots__ = ['_root', 'size']
    def __init__(self, item = None, Tleft=None, Tright=None, parent=None):
        self._root = None
        self.size = 0
        if item is not None:
            self._root = self.addRoot(item)
            if Tleft is not None:
                Tleft._root.parent = self._root
                self._root.left = Tleft._root
                self.size += Tleft.size
                Tleft._root = None
                Tleft.size = 0
            if Tright is not None:
                Tright._root.parent = self._root
                self._root.right = Tright._root
                self.size += Tright.size
                Tright._root = None
                Tright.size = 0

    def addRoot(self, item):
        if self._root is not None:
            raise ValueError("Root already exists")
        self._root = self.BTNode(item)
        self.size += 1
        return self._root
    
    def __len__(self):
        return self.size
    
    def parent(self, pos):
        return pos.parent
    
    def left(self, pos):
        return pos.left

    def right(self, pos):
        return pos.right
    
    def root(self):
        return self._root

    def addLeft(self, item, pos):
        if self.left(pos) is not None:
            raise ValueError("Left child already exists")
        pos.left = self.BTNode(item, parent=pos)
        self.size += 1
        return pos.left
    
    def addRight(self, item, pos):
        if self.right(pos) is not None:
            raise ValueError("Right child already exists")
        pos.right = self.BTNode(item, parent=pos)
        self.size += 1
        return pos.right
    
    def preorder(self, pos):
        res = ""
        res = f"{pos.item} "
        if pos.left is not None:
            res += self.preorder(pos.left) + " " 
        if pos.right is not None:
            res += self.preorder(pos.right) + " " 
        return res
    
    def inorder(self,pos):
        res = ""
        if pos.left is not None:
            res = self.inorder(pos.left) + " " 
        res += f"{pos.item}"
        if pos.right is not None:
            res += self.inorder(pos.right) + " " 
        return res

    def postorder(self, pos):
        res = ""  # Initialize res variable
        if pos.left is not None:
            res = self.postorder(pos.left) + " " 
        if pos.right is not None:
            res += self.postorder(pos.right) + " " 
        res += f"{pos.item}"
        return res

    def inorder(self,pos):
        res = ""
        if pos.left is not None:
            res = self.inorder(pos.left)
        res += f"{pos.item}"
        if pos.right is not None:
            res += self.inorder(pos.right)
        return res
    
    def __str__(self):
        return str(self.preorder(self._root))