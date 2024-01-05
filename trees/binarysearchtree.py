from linkedbinarytree import LinkedBinaryTree

class BSTNode:
    __slots__ = ['value', 'left', 'right', 'parent']
    def __init__(self,value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, item=None, Tright=None, Tleft=None):
        super().__init__(item, Tleft, Tright)
        self._root = None
        self.size = 0

    def insert(self, pos, ele):
        if self._root is None:
            self._root = BSTNode(ele)
            self.size += 1
        else:
            if ele < pos.value:
                if pos.left is None:
                    pos.left = BSTNode(ele)
                    self.size += 1
                else:
                    self.insert(pos.left, ele)
                    self.size += 1
            elif ele > pos.value:
                if pos.right is None:
                    pos.right = BSTNode(ele)
                    self.size += 1
                else:
                    self.insert(pos.right, ele)
                    self.size += 1
            else:
                return

    def search(self, pos, item):
        if item == pos.value:
            return pos
        elif item < pos.value and pos.left is not None:
            return self.search(pos.left, item)
        elif item > pos.value and pos.right is not None:
            return self.search(pos.right, item)

    def findmin(self, pos=None):
        if pos is None:
            return pos.parent
        elif pos.left is not None:
            return self.findmin(pos.left)
        else:
            return pos.value

    def findmax(self, pos=None):
        if pos is None:
            return pos.parent
        elif pos.right is not None:
            return self.findmax(pos.right)
        else:
            return pos.value

    def inorder(self, pos):
        res = ""
        if pos.left is not None:
            res += self.inorder(pos.left)
            res += ", "
        res += str(pos.value)
        if pos.right is not None:
            res += ", "
            res += self.inorder(pos.right)
        return res


    def __str__(self):
        self.string = ""
        self.inorder(self._root)
        return self.string

B = BinarySearchTree(11)
B.insert(B._root, 11)
B.insert(B._root, 1)
B.insert(B._root, 5)
B.insert(B._root, 112)
B.insert(B._root, 19)
B.insert(B._root, 22)
B.insert(B._root, 47)
B.insert(B._root, 83)
B.insert(B._root, 119)
B.insert(B._root, 121)
B.insert(B._root, 0)
B.insert(B._root, 32)
result = B.inorder(B._root)
print(result)
print("Maximum Element:",B.findmax(B._root))
print("Minimum Element:",B.findmin(B._root))
print(B.search(B._root,22))
