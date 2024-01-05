import random
#wrapper method
class Stack:
    def __init__(self):
        self.item = []
    
    def isempty(self):
        return len(self.item) == 0
    
    def push(self, ele):
        self.item.append(ele)
    
    def pop(self):
        return self.item.pop()
    
    def __len__(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)
    
    def topelement(self):
        return self.item[-1]

S = Stack()
n = int(input("Number of elements: "))
for _ in range(n):
    S.push(random.randint(-10,10))
print(len(S))
print(S.pop())
print(S)
print(S.topelement())
print(S.isempty())

import ctypes
#Dynamic Array method
class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = 0
        self.item = self.makearray(cap)
    
    def makearray(self, cap):
        temp = (cap * ctypes.py_object)()
        return temp
    
    def resize(self, cap):
        B = self.makearray(cap)
        for i in range(self.cap - 1):
            B[i] = self.item[i]
        self.item = B
        self.cap = cap

    def isempty(self):
        return self.top == 0

    def push(self, ele):
        if self.top == self.cap:
            self.resize(2*self.cap)
        self.item[self.top] = ele
        self.top += 1

    def pop(self):
        if self.isempty():
            raise Empty("Empty Stack")
        ele = self.item[self.top - 1]
        self.item[self.top - 1] = None
        self.top -= 1
        if (self.top < self.cap//4):
            self.resize(self.cap//2)
        return ele

    def __str__(self):
        return str([self.item[i] for i in range(self.top)])

    def __len__(self):
        return self.top
    
    def topelement(self):
        return self.item[self.top - 1]
    


class Empty(Exception):
   pass

S = Stack(5)
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
S.pop()
print(S)
print(len(S))
print(S.topelement())

import ctypes

class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = 0
        self.item = self.makearray(cap)

    def makearray(self, cap):
        temp = (cap * ctypes.py_object)()
        return temp
   
    def resize(self, cap):
        B = self.makearray(cap)
        for i in range(self.cap-1):
            B[i] = self.item[i]
        self.item = B
        self.cap = cap

    def isempty(self):
        return self.top == 0
    
    def push(self, ele):
        if self.top == self.cap:
            self.resize(2*self.cap)
        self.item[self.top] = ele
        self.top += 1

    def pop(self):
        if self.isempty():
            raise Empty("Empty Stack")
        ele = self.item[self.top - 1]
        self.item[self.top -1] = None
        self.top -= 1
        if (self.top < self.cap//4):
            self.resize(self.cap//2)
        return ele
    
    def __str__(self):
        return str([self.item[i] for i in range(self.top)])
    
    def __len__(self):
        return self.top

class Empty(Exception):
    pass

S = Stack(5)
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
print(S)
print(S.pop())
print(len(S))
