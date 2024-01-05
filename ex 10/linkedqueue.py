class Node:
    __slots__ = ['item', 'next']
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class LinkedQueue:
    __slots__ = ['front', 'rear','size']
    def __init__(self):
        self.front = self.rear = Node()
        self.size = 0
    
    def __len__(self):
        return self.size

    def isempty(self):
        return self.front.next == None
    
    def enqueue(self, ele):
        self.rear.next = Node(ele)
        self.rear = self.rear.next
        self.size += 1

    def dequeue(self):
        if self.isempty():
            raise Empty("Queue is empty")
        ele = self.front.next.item
        self.front = self.front.next
        self.size -= 1
        return ele

    def __str__(self):
        out = ''
        pos = self.front.next
        while (pos != None):
            out += str(pos.item) + " -> "
            pos = pos.next
        out += "END"
        return out

class Empty(Exception):
    pass

q = LinkedQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
print(q.dequeue())
print(q)