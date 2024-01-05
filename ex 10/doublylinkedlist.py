from dnode import DNode

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = DNode(None, None, None)
        self.size = 0
    
    def isempty(self):
        return (self.head == self.tail)
    
    def append(self, ele):
        temp = DNode(ele, None)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.size += 1

    def display(self):
        pos = self.head.next
        while (pos != None):
            if pos.item != None:
                print(pos.item, end = " ")
                pos = pos.next
    
    def reverse_display(self):
        pos = self.tail
        while (pos != None):
            if pos.item == None:
                break
            print(pos.item, end = " ")
            pos = pos.prev

    def find(self, ele):
        pos = self.head.next
        while (pos != None):
            if pos.item == ele:
                return pos
        return None
    
    def insert(self, position, ele):
        pos = self.head
        for i in range(position - 1):
            pos = pos.next
        temp = DNode(ele, None, None)

        if pos.next == None:
            self.append(ele)
            return self.display()
        else:
            temp.prev = pos
            temp.next = pos.next
            pos.next.prev = temp
            pos.next = temp
        self.size += 1
        return self.display()
    
    def find_prev(self, data):
        pos = self.head.next
        while (pos.next != None):
            if (pos.next.item == data):
                return pos
            else:
                pos = pos.next
        return None
    
    def reverse(self):
        current = self.head.next
        prev_node = None  # Initialize the previous node to None
        while current:
            next_node = current.next  # Store the next node temporarily
            current.next = prev_node  # Reverse the next pointer
            current.prev = next_node  # Reverse the prev pointer
            prev_node = current  # Move the previous node pointer
            current = next_node  # Move to the next node

        # Update the head and tail pointers after reversal
        self.tail, self.head = self.head, self.tail

    
    
    

D = DoublyLinkedList()
#appending
D.append(10)
D.append(20)
D.append(30)
D.append(40)
D.append(50)

#displaying initial linked list
print("Initial linked list:")
D.display()
print()

'''#Reversed linked list
print("Reverse Linked List:")
D.reverse_display()
print()

#inserting 40
print("Insert 40:")
print(D.insert(4,100))
print()

#Removing 40
print("Removing 40")
print(D.remove(40))
print()

#checking if empty
print("Check if empty")
print(D.isempty())
print()'''
D.reverse()
D.display()