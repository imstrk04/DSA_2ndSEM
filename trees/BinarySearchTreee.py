from linkedbinarytree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, item=None, Tleft=None, Tright=None):
        super().__init__(item,Tleft,Tright)

    def insert(self, item, pos):
        if item == pos.item:
            return
        elif item<pos.item:
            if pos.left is None:
                pos.left = self.addLeft(item,pos)
            else:
                self.insert(item, pos.left)
        elif item>pos.item:
            if pos.right is None:
                pos.right = self.addRight(item,pos)
            else:
                self.insert(item, pos.right)

    def search(self, item, pos):
        if item == pos.item:
            return pos
        elif item<pos.item and pos.left is not None:
                return self.search(item, pos.left)
        elif item>pos.item and pos.right is not None:
               return self.search(item, pos.right)
        
    def findmax(self, pos=None):
         if pos is None:
              return pos.parent
         elif pos.right is not None:
              return self.findmax(pos.right)
         else:
              return pos   
         
    def findmin(self, pos=None):
         if pos is None:
              return pos.parent
         elif pos.left is not None:
              return self.findmin(pos.left)
         else:
              return pos   

    def delete(self, item)  :
         pos = self.search(item, self.root)
        
         
         parent = pos.parent   
         if pos.left is None and pos.right is None: # No children
             
              if parent.left == pos:
                   parent.left = None
                   self.size-=1
                   return
              elif parent.right == pos:
                   parent.right = None
                   self.size-=1
         elif pos.left is not None and pos.right is None: # one children - left
              parent.left = pos.left
              pos.parent = pos.left = pos.right = None
              self.size -=1
         elif pos.right is not None and pos.left is None: # one children - right
              parent.right = pos.right
              pos.parent = pos.left = pos.right = None
              self.size -=1
         else: #Two children
              r = self.findmin(pos.right)
              pos.item = r.item
              r.item = 1000000
              self.delete(r.item)
            
    def mirror(self, pos=None):
         if pos is None or pos.left is None or pos.right is None:
              return
         if pos.left is not None and pos.left is not None:
              pos.left.item, pos.right.item = pos.right.item, pos.left.item
         self.mirror(pos.left)
         self.mirror(pos.right)
     
b = BinarySearchTree()
b.insert(10, b.root)