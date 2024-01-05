class Node:
    __slots__ = ['item', 'next']
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
class LinkedStack:
    def __init__(self):
        self.top = Node()
        self.size = 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.top.next == None

    def top(self):
        if self.isempty():
            raise Empty("Stack Empty")
        return self.top.next.item
    
    def push(self, ele):
        self.top = Node(ele, self.top)
        self.size += 1

    def __str__(self):
        out = ''
        pos = self.top
        while (pos.next != None):
            out += str(pos.item) + " -> "
            pos = pos.next
        out += "END"
        return out

    def pop(self):
        delnode = self.top
        self.top = delnode.next
        self.size -= 1
        return delnode
                

class Empty(Exception):
    pass

s = LinkedStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s)
s.pop()
print(s)