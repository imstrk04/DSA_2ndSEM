#Q1 Matrix ADT
class Matrix:
    def __init__(self, r = 0, c = 0):
        '''Constructor to initialize the datamembers'''
        self.row = r
        self.col = c
        self.order = (self.row, self.col)
        self.matrix = []
        for i in range(r):
            l1 = [0] * c
            self.matrix.append(l1)
    
    def __sub__(self, other):
        '''
        User defined method to subtract two matrices
        '''
        if self.order != other.order:
            raise ValueError("Dimensions of two matrices aren't same.")
        else:
            result = [[0 for j in range(self.col)] for i in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result


#Quick Sort
def median(l):
    n = len(l)
    low,mid,high = l[0], l[n//2], l[-1]
    if low > high:
        l[0],l[-1] = l[-1], l[0]
    if high > mid:
        l[-1], l[n//2] = l[n//2], l[-1]
    if low > mid:
        l[0], l[n//2], l[n//2], l[0]
    return l

def partition(l, begin, end):
    pivot = l[end]
    i,j = begin, end - 1
    while (i <= j):
        while (l[i] <= pivot and i < end):
            i += 1
        while (l[j] > pivot and j >= begin):
            j = j - 1
        if i < j:
            l[i], l[j] = l[j], l[i]
    l[i], l[end] = l[end], l[i]
    return i, l[i:i+1]

def qsort(l):
    if len(l) < 2:
        return l
    else:
        l = median(l)
        sorted_pos, mid = partition(l, 0, len(l)-1)
        return qsort(l[:sorted_pos]) + mid + qsort(l[sorted_pos+1:])
    
#Q2 Singly Linked List

class Node:
    __slots__ = ['item', 'next']
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0
    
    def append(self, ele):
        temp = Node(ele)
        self.tail.next = temp
        self.tail = temp
        self.size += 1
        
    def displayODD(self):
        pos = self.head.next
        count = 1
        while (pos != None):
            if count % 2 != 0:
                print(str(pos.item) + "->", end = " ")
                pos = pos.next
                count += 1
            pos = pos.next
            count += 1

        print("END")

    def display(self):
        pos = self.head.next
        while (pos != None):
            print(str(pos.item) + "->", end = " ")
            pos = pos.next
        print("END")

    def delete_even_numbers(self):
        if self.head.next is None:
            return

        dummy = Node(0)
        dummy.next = self.head.next

        
        curr = dummy
        while curr.next is not None:
            if curr.next.item % 2 == 0:
                curr.next = curr.next.next
                self.size -= 1
            else:
                curr = curr.next

        self.head.next = dummy.next
        if dummy.next is None:
            self.tail = self.head
        

s = LinkedList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
s.append(7)
s.append(8)
s.displayODD()
s.delete_even_numbers()
s.display()