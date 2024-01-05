import ctypes
class DynamicArray:
    def __init__(self,cap):
        self.cap = cap
        self.A = self.makearray(cap)
        self.n = 0
    
    def makearray(self,cap):
        temp = (cap * ctypes.py_object)()
        return temp

    def resize(self,cap):
        B = self.makearray(cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.cap = cap
    
    def append(self,ele):
        if self.n == self.cap:
            self.resize(2*self.cap)
        self.A[self.n] = ele
        self.n += 1
    
    