import ctypes

class CircularQueue:
    def __init__(self, cap):
        '''
            Constructor to initialise variables
        '''
        self.cap = cap
        self.item = self.makearray(cap)
        self.rear = self.front = 0

    def makearray(self, cap):
        '''
            Method to create compact arrays
        '''
        temp = (cap * ctypes.py_object)()
        return temp

    def next(self, pos):
        '''
            Method to go next in the data structure.
        '''
        return ( pos + 1 ) % self.cap
    
    def isEmpty(self):
        '''
            Method to check if circular queue is empty.
        '''
        return (self.front == self.rear)
    
    def isFull(self):
        '''
            Method to check if circular queue is full.
        '''
        return ((self.rear + 1) % self.cap == self.front)
    
    def enqueue(self, ele):
        '''
            Method to add elements to the circular queue.
        '''
        if (self.isFull()):
            print("Queue is Full. No more orders accepted.")
        else:
            self.item[self.rear] = ele
            self.rear = self.next(self.rear)
            print("Order placed Successfully")
    
    def dequeue(self):
        '''
            Method to remove elements from circular queue.
        '''
        if self.isEmpty():
            print("No more orders to serve")
        else:
            order = self.item[self.front]
            self.front = self.next(self.front)
            print("Serving order", order)
    
class Full(Exception):
    pass

class Empty(Exception):
    pass