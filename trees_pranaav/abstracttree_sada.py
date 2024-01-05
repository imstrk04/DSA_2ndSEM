from abc import ABC, abstractmethod

class AbstractTree(ABC):
    @abstractmethod
    def getRoot(self):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def getParent(self):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def getNum_children(self,pos):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def getChildren(self,pos):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def __len__(self):
        raise Exception("Not Implemented")
    
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
    
    def heightN(self, pos):
        if self.isLeaf(pos):
            return 0
        else:
            return 1 + max([self.heightN(child) for child in self.getChildren(pos)])
    
    def height(self):
        return self.heightN(self.getRoot())