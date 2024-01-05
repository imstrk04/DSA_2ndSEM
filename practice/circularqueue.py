import ctypes

class CQueue:
    def __init__(self, cap):
        self.cap = cap
        self.front = self.rear = 0
        self.item = self.makearray(cap)
        
    def makearray(self, cap):
        temp = (cap * ctypes.py_object)()
        return temp

    def next(self, pos):
        return (pos + 1) % self.cap

    def isempty(self):
        return self.front == self.rear
    
    def isfull(self):
        return ((self.rear + 1) % self.cap == self.front)
    
    def enqueue(self, ele):
        if self.isfull():
            raise Full("CQueue is full")
        else:
            self.item[self.rear] = ele
            self.rear = self.next(self.rear)
    
    def dequeue(self):
        if self.isempty():
            raise Empty("CQueue is empty")
        else:
            ele = self.item[self.front]
            self.item[self.front] = None
            self.front += 1
            return ele

    def __str__(self):
        return str([self.item[i] for i in range(self.front,self.rear)])

class Full(Exception):
    pass

class Empty(Exception):
    pass


c = CQueue(5)
c.enqueue(100)
c.enqueue(200)
c.enqueue(300)
c.enqueue(400)
print(c.dequeue())
print(c)