from linkedbtpranaav import LinkedBinaryTree
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
                return self.addLeft(ele, pos)
            else:
                return self.append(ele, self.getLeft(pos))
        elif ele > pos.item:
            if self.getRight(pos) is None:
                return self.addRight(ele, pos)
            else:
                return self.append(ele, self.getRight(pos))
        else:
            return None
   
    def findmin(self,pos=0):

        if pos == 0:
            pos = self.getRoot()

        if pos.left is not None:

            return self.findmin(pos.left)
        
        else:

            return pos.item
        
    def findmax(self,pos=0):

        if pos == 0:
            pos = self.getRoot()

        if pos.right is not None:

            return self.findmax(pos.right)
        
        else:

            return pos.item
        
    def all_children(self,pos):

        l = [childr.item for childr in self.getChildren(pos)]
        return l

    def delete(self, ele, pos=0):
        if pos is 0:
            pos = self.getRoot()

        if pos is None:
            return None  

        if ele < pos.item:
            self.delete(ele, self.getLeft(pos))
        elif ele > pos.item:
            self.delete(ele, self.getRight(pos))
        else:
            if self.isLeaf(pos):  
                if pos == self.getRoot():
                    self.root = None
                else:
                    parent = self.getParent(pos)
                    if self.getLeft(parent) == pos:
                        parent.left = None
                    else:
                        parent.right = None
            elif self.getLeft(pos) is None or self.getRight(pos) is None:
                if self.getLeft(pos) is None:
                    child = self.getRight(pos)
                else:
                    child = self.getLeft(pos)
                if pos == self.getRoot():
                    self.root = child
                else:
                    parent = self.getParent(pos)
                    if self.getLeft(parent) == pos:
                        parent.left = child
                    else:
                        parent.right = child
            else:  
                min_node = self.getminNode(self.getRight(pos))
                pos.item = min_node.item
                self.delete(min_node.item, self.getRight(pos))

    def getminNode(self, pos):
        """Returns the node with the maximum value in the subtree rooted at 'pos'."""
        while self.getLeft(pos) is not None:
            pos = self.getLeft(pos)
        return pos