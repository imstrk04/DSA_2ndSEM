from abc import ABC, abstractmethod
class AbstractTree(ABC):
    @abstractmethod
    def getRoot(self):
        return Exception("Not Implemented")
    @abstractmethod
    def getParent(self,pos):
        return Exception("Not Implemented")
    @abstractmethod
    def getNum_children(self,pos):
        return Exception("Not Implemented")
    @abstractmethod
    def getChildren(self,pos):
        return Exception("Not Implemented")
    @abstractmethod
    def __len__(self):
        return Exception("Not Implemented")
    def isRoot(self,pos):
        return self.getRoot() == pos
    def isLeaf(self,pos):
        return self.getNum_children(pos) == 0
    def isEmpty(self):
        return len(self) == 0
    def depthN(self,pos):
        if self.isRoot(pos):
            return 0
        else:
            return 1 + self.depthN(self.getParent(pos))
    def heightN(self,pos):
        if self.isLeaf(pos):
            return 0
        else:
            return 1 + max([self.heightN(child) for child in self.getChildren(pos)])
    def height(self):
        return self.heightN(self.getRoot())

class AbstractBinaryTree(AbstractTree):
    @abstractmethod
    def getLeft(self,pos):
        raise Exception("Not Implemented")
    @abstractmethod
    def getRight(self,pos):
        raise Exception("Not Implemented")
    def getChildren(self,pos):
        if pos is None:
            return None
        if self.getLeft(pos) is not None:
            yield self.getLeft(pos)
        if self.getRight(pos) is not None:
            yield self.getRight(pos)
    def sibling(self,pos):
        parent = self.getParent(pos)
        if parent is None:
            return None
        if pos == self.right(parent):
            return self.left(parent)
        else:
            return self.right(parent)

class LinkedBinaryTree(AbstractBinaryTree):
    class BTNode:
        __slots__ = ['item', 'left', 'right', 'parent']
        def __init__(self, item, left = None, right = None, parent = None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent
        def __getitem__(self):
            return self.item
        def __setitem__(self,item):
            self.item = item
    __slots__ = ['root', 'size']
    def __init__(self,item = None, t_left = None, t_right = None):
        self.root = None
        self.size = 0
        self.string = ""
        if item is not None:
            self.root = self.addRoot(item)
        if t_left is not None:
            if t_left.root is not None:
                t_left.root.parent = self.root
                self.root.left = t_left.root
                self.size += t_left.size
                t_left.root = None
        if t_right is not None:
            if t_right.root is not None:
                t_right.root.parent = self.root
                self.root.right = t_right.root
                self.size += t_right.size
                t_right.root = None
    def addRoot(self,item):
        if self.root is not None:
            raise ValueError("Root already Exists")
        else:
            self.root = self.BTNode(item)
            self.size += 1
            return self.root
    def  __len__(self):
        return self.size
    def getParent(self,pos):
        return pos.parent
    def getLeft(self,pos):
        if pos is None:
            return None
        return pos.left
    def getRight(self,pos):
        if pos is None:
            return None
        return pos.right
    def getRoot(self):
        return self.root
    def getSize(self):
        return self.size
    def getNum_children(self,pos):
        if pos is None:
            return 0
        else:
            return 1 + self.getNum_children(pos.left) + self.getNum_children(pos.right)
    def addLeft(self,item,pos = None):
        if pos is None:
            pos = self.root
        if self.getLeft(pos) is not None:
            raise ValueError("Left child alreay exists!")
        else:
            pos.left = self.BTNode(item,parent = pos)
            self.size += 1
            return pos.left
    def addRight(self,item,pos):
        if pos is None:
            pos = self.root
        if self.getRight(pos) is not None:
            raise ValueError("Right Child already exists!")
        else:
            pos.right = self.BTNode(item, parent = pos)
            self.size += 1
            return pos.right
    def preorder(self, pos):
        self.string += str(pos.item) + ","
        if pos.left is not None:
            self.preorder(pos.left)
        if pos.right is not None:
            self.preorder(pos.right)

    def postorder(self, pos):
        if pos.left is not None:
            self.postorder(pos.left)
        if pos.right is not None:
            self.postorder(pos.right)
        self.string += str(pos.item) + ","

    def inorder(self, pos):
        if pos.left is not None:
            self.inorder(pos.left)
        self.string += str(pos.item) + ","
        if pos.right is not None:
            self.inorder(pos.right)

    def __str__(self):
        self.string = "The preorder is: "
        self.preorder(self.root)
        self.string = self.string[:-1]  # Remove the trailing comma
        self.string += "\nThe inorder is: "
        self.inorder(self.root)
        self.string = self.string[:-1]  # Remove the trailing comma
        self.string += "\nThe postorder is: "
        self.postorder(self.root)
        self.string = self.string[:-1]  # Remove the trailing comma
        return self.string

    def mirror_tree(self):
        self._mirror_tree(self.root)

    def _mirror_tree(self,pos):
        if pos is None:
            return
        pos.left, pos.right = pos.right, pos.left
        self._mirror_tree(pos.left)
        self._mirror_tree(pos.right)
        
T = LinkedBinaryTree()
root = T.addRoot(10)
left_child = T.addLeft(20, pos=root)
right_child = T.addRight(30, pos=root)
left_child1 = T.addLeft(40, pos=left_child)
right_child1 =T.addRight(50, pos=right_child)
T.addRight(60,pos = left_child1)
T.addLeft(70,pos = left_child1)
T.addRight(80, pos = right_child1)
T.addLeft(90,pos = right_child1)        

print("Original Tree:")
print(T)

T.mirror_tree()

print("\nMirror Tree:")
print(T)
print("-----------------------------------------")
print()




class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, item=None, t_left=None, t_right=None):
        super().__init__(item, t_left, t_right)

    def isLeaf(self, pos):
        return self.getLeft(pos) is None and self.getRight(pos) is None

    def append(self, ele, pos=None):
        if pos is None:
            if self.isEmpty():
                self.addRoot(ele)
                return None
            else:
                pos = self.getRoot()
        if ele < pos.item:
            if self.getLeft(pos) is None:
                self.addLeft(ele, pos)
            else:
                self.append(ele, self.getLeft(pos))
        elif ele > pos.item:
            if self.getRight(pos) is None:
                self.addRight(ele, pos)
            else:
                self.append(ele, self.getRight(pos))
        else:
            return None

    def findmin(self, pos=None):
        if pos is None:
            pos = self.getRoot()
        if pos.left is not None:
            return self.findmin(pos.left)
        else:
            return pos.item

    def findmax(self, pos=None):
        if pos is None:
            pos = self.getRoot()
        if pos.right is not None:
            return self.findmax(pos.right)
        else:
            return pos.item

    def all_children(self, pos):
        l = [child.item for child in self.getChildren(pos)]
        return l

    def search(self, item, pos):
        if pos is None or item == pos.item:
            return pos
        elif item < pos.item:
            return self.search(item, self.getLeft(pos))
        else:
            return self.search(item, self.getRight(pos))

    def findminpos(self, pos=None):
        if pos is None:
            pos = self.getRoot()
        if pos.right is not None:
            return self.findminpos(pos.right)
        else:
            return pos

    def delete(self, item):
        pos = self.search(item, self.getRoot())

        if pos is None:
            return False

        parent = self.getParent(pos)

        if pos.left is None and pos.right is None:  # No Child
            if parent is not None:
                if parent.left == pos:
                    parent.left = None
                else:
                    parent.right = None

        elif pos.left is not None and pos.right is None:  # 1 child - left
            if parent is not None:
                if parent.left == pos:
                    parent.left = pos.left
                else:
                    parent.right = pos.left
                pos.left.parent = parent
            else:
                self.root = pos.left
                pos.left.parent = None

            pos.parent = pos.left = pos.right = None

        elif pos.right is not None and pos.left is None:  # 1 child - right
            if parent is not None:
                if parent.left == pos:
                    parent.left = pos.right
                else:
                    parent.right = pos.right
                pos.right.parent = parent
            else:
                self.root = pos.right
                pos.right.parent = None

            pos.parent = pos.left = pos.right = None

        else:  # 2 children
            r = self.findminpos(pos.right)
            pos.item = r.item
            r.item = 1000000
            self.delete(r.item)





# Driver code
bst = BinarySearchTree()

# Appending nodes
bst.append(50)
bst.append(30)
bst.append(40)
bst.append(70)
bst.append(60)
bst.append(10)

# Printing the original tree
print("Original Tree:")
print(bst)

# Finding the minimum and maximum values
min_val = bst.findmin()
max_val = bst.findmax()
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)

# Deleting a node with no child
delete_success = bst.delete(30)
print("Deletion Successful:", delete_success)
print("Updated Tree:")
print(bst)


