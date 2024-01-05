class Node:
    __slots__ = ['item', 'next']
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class CiruclarLinkedList:
    def __init__(self):
        self.tail = self.head = Node()
        self.head.next = self.head
        self.size = 0
    
    def isempty(self):
        return self.head.next == self.head

    def append(self, ele):
        temp = Node(ele)
        if self.head == self.tail:
            self.head.next = temp
            self.tail = temp
            self.size += 1
            return
        
        self.tail.next = temp
        temp.next = self.head
        self.tail = temp
        self.size += 1

    def display(self):
        pos = self.head.next
        first = str(pos.item)
        out = " "
        while (pos != self.head):
            out += str(pos.item) + " <-> "
            pos = pos.next
        out += "HEAD"
        return out

    def remove(self, val):
        if self.isempty():
            return

        current = self.head.next
        previous = self.head

        while current != self.head:
            if current.item == val:
                previous.next = current.next

                # If the node being removed is the tail, update the tail pointer
                if current == self.tail:
                    self.tail = previous

                # If the node being removed is the head, update the head pointer
                if current == self.head.next:
                    self.head.next = current.next

                self.size -= 1
                return

            previous = current
            current = current.next

c = CiruclarLinkedList()
c.append(10)
c.append(20)
c.append(30)
c.append(40)
c.append(50)
print(c.display()) 
c.remove(30)
print(c.display())