from linkedbinarytree_sada import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):

    def __init__(self,item = None, t_left = None, t_right = None):
        super().__init__(item, t_left, t_right)
        self.size = 0
    
    def isLeaf(self, pos):
        return self.getLeft(pos) is None and self.getRight(pos) is None

    def append(self,ele,pos = None):
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
                return self.addRight(ele,pos)
            else:
                return self.append(ele, self.getRight(pos))
        else:
            return None

    def findmind(self, pos = 0):
        if pos == 0:
            pos = self.getRoot()
        
        if pos.left is not None:
            return self.find(pos.left)
        else:
            return pos.item
    
    def findmin(self,pos = 0):
        if pos == 0:
            pos = self.getRoot()
        
        if pos.right is not None:
            return self.findmin(pos.right)
        else:
            return pos.item
    
    def all_children(self,pos):
        l = [childr.item for childr in self.getChildren(pos)]
        return l

    def search(self, item, pos=None):
            if pos is None:
                pos = self.getRoot()

            if pos.item == item:
                return pos

            if item < pos.item and self.getLeft(pos) is not None:
                return self.search(item, self.getLeft(pos))
            elif item > pos.item and self.getRight(pos) is not None:
                return self.search(item, self.getRight(pos))
            else:
                return None
    
    def delete(self, item):
        pos = self.search(item)

        parent = pos.parent

        if self.getLeft(pos) is None and self.getRight(pos) is None: #No children
            if parent.left == pos:
                parent.left = None
                return
            elif parent.right == pos:
                parent.right = None
                return
        elif self.getLeft(pos) is not None and self.getRight(pos) is None: #one child - left
            parent.left = pos.left
            pos.parent = pos.left = pos.right = None
        elif self.getRight(pos) is not None and self.getLeft(pos) is None: #one child - right
            parent.right = pos.right
            pos.parent = pos.right = pos.left = None
        else: #Two children
            r = self.findmin(pos.right)
            pos.item = r.item
            self.delete(r.item)

    def getminNode(self,pos):
        while self.getLeft(pos) is not None:
            pos = self.getLeft(pos)
        return pos

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.append(10,bst.root)
    bst.append(100,bst.root)
    bst.append(2,bst.root)
    bst.append(21,bst.root)
    bst.append(44,bst.root)
    bst.append(-1,bst.root)
    bst.append(4,bst.root)
    bst.append(119,bst.root)
    bst.append(25,bst.root)
    print(bst)