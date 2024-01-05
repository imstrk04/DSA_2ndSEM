'''
#Dynamic Array method
import ctypes

class Queue:
    def __init__(self,cap):
        self.cap = cap
        self.front = self.rear = 0
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
        return self.front == self.rear

    def enqueue(self, ele):
        if self.rear == self.cap:
            self.resize(2 * self.cap)
        self.item[self.rear] = ele
        self.rear += 1
    
    def dequeue(self):
        if self.isempty():
            raise Empty("Queue is empty")
        ele = self.item[self.front]
        self.item[self.front] = None
        self.front += 1
        return ele

    def __str__(self):
        return str([self.item[i] for i in range(self.front,self.rear)])

    def __len__(self):
        return self.rear - self.front

class Empty(Exception):
    pass

q = Queue(5)
q.enqueue(10) 
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q)
print(q.dequeue())
print(q)
print(len(q))'''
#Wrapper method

class Queue:
    def __init__(self):
        self.item = []
    
    def isempty(self):
        return len(self.item) == 0

    def enqueue(self,ele):
        self.item.append(ele)
    
    def dequeue(self):
        return self.item.pop(0)

    def __len__(self):
        return len(self.item)

    def __str__(self):
        return str([self.item[i] for i in range(len(self.item))])

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


def is_palindrome(string):
    Q = Queue()

    for char in string:
        Q.enqueue(char)

    while not Q.isempty():
        if Q.dequeue() != string[-1]:
            return False
        string = string[:-1]
    return True

print(is_palindrome("mam"))

def reverseusingstack(list):
    q = Queue()
    s = Stack()
    s1 = Stack()

    for i in list:
        q.enqueue(i)
    
    for i in range(len(q)):
        s.push(q.dequeue())
    
    for i in range(len(s)):
        s1.push(s.pop())

    print(s1)

reverseusingstack([1,2,3,4,5])