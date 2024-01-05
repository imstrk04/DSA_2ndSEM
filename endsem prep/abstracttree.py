from abc import ABC, abstractmethod

class AbstractTree():
    @abstractmethod
    def root(self):
        pass

    @abstractmethod
    def parent(self,pos):
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

    def isRoot(self,pos):
        return self.root() == pos
    
    def isLeaf(self, pos):
        return self.num_children(pos) == 0
    
    def isEmpty(self):
        return self.root() == None

    def depthN(self,pos):
        if self.isRoot(pos):
            return 0
        else:
            return self.depthN(self.parent(pos)) + 1
    
    def heightN(self, pos):
        if self.isLeaf(pos):
            return 0
        else:
            return max(self.heightN(child) for child in self.children(pos)) + 1
    
    def height(self, pos = None):
        if pos == None:
            if self.isEmpty() != True:
                return -1
            pos = self.root()
            return self.heightN(pos)
        