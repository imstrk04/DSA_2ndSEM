from abc import ABC, abstractmethod

class AbstractTree():
    @abstractmethod
    def root(self):
        raise Exception("Not Implemented")

    @abstractmethod
    def parent(self, pos):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def numChildren(self,pos):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def children(self,pos):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def __len__(self):
        raise Exception("Not Implemented")
    
    def isRoot(self, pos):
        return pos == self.root()

    def isLeaf(self,pos):
        return self.numChildren(pos) == 0
    
    def isEmpty(self):
        return len(self) == 0
    
    def depthN(self,pos):
        if pos is None:
            return 0
        else:
            return 1 + self.depthN(self.parent(pos))
    
    def heightN(self,pos):
        if pos is None:
            return 0
        else:
            return 1 + max(self.heightN(child) for child in self.children(pos))
    
    def height(self,pos =None):
        if pos is None:
            if self.isEmpty():
                return -1
            pos = self.root()
        return self.heightN(pos)

class AbstractBinaryTree(AbstractTree):
    @abstractmethod
    def left(self,pos):
        raise Exception("Not Implemented")

    @abstractmethod
    def right(self,pos):
        raise Exception("Not Implemented")
    
    def children(self, pos):
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)
    
    def sibling(self,pos):
        parent = self.parent(pos)
        if parent is None:
            return None
        else:
            if pos == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

class LinkedBinaryTree(AbstractBinaryTree):
    class _BTNode:
        __slots__ = ['_item', '_parent', '_left','_right']

        def __init__(self, item = None, parent = None, left = None, right = None):
            self._item = item
            self._parent = parent
            self._left = left 
            self._right = right
    
        def getItem(self):
            return self._item
        
        def setItem(self, item):
            self._item = item
    
    __slots__ = ["_root", "_size"]  
   
    def __init__(self, item = None, Tleft = None, Tright = None):
        self._root = None
        self._size = 0

        if (item is not None):
            self._root = self.addRoot(item)
            if Tleft is not None:
                if Tleft._root is not None:
                    Tleft._root._parent = self._root
                    self._root._left = Tleft._root
                    Tleft._root = None
                    self._size += Tleft._size
            if Tright is not None:
                if Tright._root is not None:
                    Tright._root._parent = self._root
                    self._root._right = Tright._root
                    Tright._root = None
                    self._size += Tright._size

    
    def addRoot(self, item):
        if self.root is not None:
            raise ValueError("Root already exists")
        self._root = self.BTNode(item)
        self.size += 1
        return self._root
    
    def __str__(self):

        def preorder(pos):
            res = f"{pos._item}"
            if pos._left is not None:
                res += preorder(pos._left)
            if pos._right is not None:
                res += preorder(pos._right)
            return res
        if self._root is None:
            return '[]'
        return preorder(self._root)

    def root(self):
        return self._root
    
    def __len__(self):
        return self._size

    def parent(self, pos):
        if pos is None:
            return None
        return pos._parent
    
    def numChildren(self, pos):
        count = 0
        if pos is None:
            return count
        if pos._left is not None:
            count += 1
        if pos._right is not None:
            count += 1
        return count
    
    def left(self,pos):
        if pos is None:
            return None
        return pos._left
    
    def right(self, pos):
        if pos is None:
            return None
        return pos._right

    def addLeft(self,item, pos):
        if pos is None:
            raise TypeError("Not valid position")
        if pos._left is not None:
            raise ValueError("Left child already exists")
        pos._left = self._BTNode(item,pos)
        self._size += 1
        return pos._left
    
    def addRight(self, item, pos):
        if pos is None:
            raise TypeError("Not Valid Position")
        if pos._right is not None:
            raise ValueError("Right child already exists")
        pos._right = self._BTNode(item, pos)
        self._size += 1
        return pos._right

class ExpressionTree(LinkedBinaryTree):
    def __init__(self, item = None, Tleft = None, Tright = None):
        super().__init__(item, Tleft,Tright)

    def construct(self,str):
        s = []
        for ch in str:
            if ch in '+-*/':
                print("operator")
                rchild = s.pop()
                lchild = s.pop()
                s.append(ExpressionTree(ch,lchild,rchild))
            else:
                print("operand")
                s.append(ExpressionTree(ch))
        return s.pop()

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self,item = None, Tleft = None, Tright = None):
        super().__init__(item, Tleft, Tright)
    
    def insert(self, item, pos):
        print(pos._item)
        if item == pos._item:
            return
        elif item < pos._item:
            if pos._left is None:
                pos._left = self.addLeft(item,pos)
            else:
                self.insert(item,pos.left)
        elif item > pos._item:
            if pos._right is None:
                pos._right = self.addRight(item, pos)
            else:
                self.insert(item, pos._right)
    
    def search(self,item,pos):
        if item == pos._item:
            return pos
        elif item < pos._item and pos._left is not None:
            return self.search(item,pos._left)
        elif item > pos._item and pos._right is not None:
            return self.search(item,pos.right)
    
    def findmax(self,pos = None):
        if pos is None:
            return pos._parent
        elif pos._right is not None:
            return self.findmax(pos.right)
        else:
            return pos
    
    def findmin(self,pos = None):
        if pos is None:
            return pos._parent
        elif pos._left is not None:
            return self.findmin(pos._left)
        else:
            return pos
    
    def delete(self,item):
        pos = self.search(item, self._root)
        parent = pos._parent

        if pos._left is None and pos._right is None: #no child
            if parent._left == pos:
                parent._left = None
                return
            elif parent._right == pos:
                parent._right = None
                return
        elif pos._left is not None and pos._right is None: #one child - left
            parent._left = pos._left
            pos._parent = pos._left = pos._right = None
        elif pos._right is not None and pos._left is None: #one child - right
            parent._right = pos._right
            pos._parent = pos._left = pos._right = None
        else: #Two children
            r = self.findmin(self._root)
            pos._item = r._item
            r._item = 1000000
            self.delete(r._item)