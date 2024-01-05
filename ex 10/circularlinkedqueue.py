class Node:
    __slots__ = ['item', 'next']
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class CirucularQueue:
    def __init__(self):
        self.rear = None
        self.size = 0

    def enqueue(self, ele):
        temp = Node(ele)
        if (self.size == 0):
            temp.next = temp
            self.rear = temp
        else:
            temp.next = self.rear.next
            self.rear.next = temp
            self.rear = temp
        self.size += 1
    
    def __str__(self):
        rear = str(self.rear.item)
        out = ""
        pos = self.rear.next
        while (pos != self.rear):
            out += str(pos.item) + " <-> "
            pos = pos.next
        out += rear
        return out

    def dequeue(self):
        ele = self.rear.next.item
        pos = self.rear.next
        self.rear.next = pos.next
        return ele
    
    def rotate(self):
        self.rear = self.rear.next

c = CirucularQueue()
c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
c.enqueue(40)
c.enqueue(50)
print(c)
print(c.dequeue())
print(c)
c.rotate()
print("Rotated:", c)