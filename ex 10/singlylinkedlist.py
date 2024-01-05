
from node import Node

class SLL:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0
    
    def isempty(self):
        return (self.head == self.tail)

    def append(self, val):
        temp = Node(val)
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def display(self):
        pos = self.head.next
        while (pos != None):
            print(str(pos.item) + "->", end = " ")
            pos = pos.next
        print("END")

    def insertAtFirst(self, val):
        temp = Node(val)
        temp.next = self.head.next
        self.head.next = temp
        self.size += 1
    
    def insert(self, index, val):
        pos = self.head.next
        for _ in range(index - 1):
            pos = pos.next
        temp = Node(val)
        temp.next = pos.next
        pos.next = temp    
        self.size += 1    

    def find_prev(self,sr):
        if (self.isempty()):
            print("Empty")
        pos = self.head.next
        while (pos != None):
            if (pos.next.item == sr):
                return pos
            else:
                pos = pos.next
        return None
    
    def remove(self, ele):
        if self.isempty():
            print("Empty")
        else:
            if ele == self.head.next.item:
                delnode = self.head.next
                self.head.next = delnode.next
                self.size -= 1
            else:
              prev = self.find_prev(ele)
            if prev is None:
                print("Element not present")
                delnode = None
            else:
                delnode = prev.next
                prev.next = delnode.next
                self.size -= 1
        return delnode  

    def __str__(self):
        out = ''
        pos = self.head.next
        while (pos != None):
            out += str(pos.item) + " -> "
            pos = pos.next
        out += "END"
        return out

    def __len__(self):
        return self.size
    
    def removeatfirst(self):
        remnode = self.head.next
        self.head.next = remnode.next
        if self.head == None:
            self.tail = None 
        self.size -= 1
    
    def removeatlast(self):
        if self.size <= 1:
            self.removeatfirst()  
        pos = self.head
        for i in range(self.size-1):
            pos = pos.next
        pos.next = None
        self.tail = pos
    
    def find(self, ele):
        pos = self.head.next
        while (pos != None):
            if pos.item == ele:
                return True
            pos = pos.next
        return False
    
    def removebypos(self,pos):
        if pos < 0 or pos >= self.size:
            print("Invalid Position")   
            return
        
        curr_pos = 0
        curr_node = self.head.next
        prev = self.head

        while curr_node != None and curr_pos < pos:
            prev = curr_node
            curr_node = curr_node.next
            curr_pos += 1
        
        if curr_node == None:
            print("Invalid Position")
            return

        prev.next = curr_node.next
        self.size -= 1

    def reverse(self):
        prev = None
        curr = self.head.next
        self.tail = curr

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head.next = prev

    def numberNodes(self,pos):
        if pos is None:
            return 0
        else:
            return 1 + self.numberNodes(pos.next)
        
    def concatenate(self,other):
        if self.head.next is None:
            self.head.next = other.head.next
        else:
            curr = self.head.next
            while curr is not None:
                curr = curr.next
            curr.next = other.head.next
        
        self.tail = other.tail
        self.size += other.size

if __name__ == "__main__":
    s = SLL()
    s.append(3)
    s.append(4)
    s.append(2)
    s.append(1)
    s.append(10)
    s.insertAtFirst(100)
    s.insert(3,50)

    print("Original:")
    s.display()
    print()

    print("Removing at first:")
    s.removeatfirst()
    s.display()
    print()

    print("Removing at last:")
    s.removeatlast()
    s.display()
    print()

    print("Removing 50")
    s.remove(50)
    s.display()
    print()

    print("Printing using print statement:",s)
    print()
    print("Length of linked list is:", len(s))
    print()

    print(s.find(4))

    s.removebypos(1)
    s.display()
    s.reverse()
    print("Reverse:",s)