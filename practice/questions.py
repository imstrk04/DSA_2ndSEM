'''import random
class Node:
    __slots__ = ['item', 'next']
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
'''
'''class SLL:
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

    def numnodes(self):
        pos = self.head.next
        count = 0
        while (pos != None):
            pos = pos.next
            count += 1
        return count

    def sum(self):
        pos = self.head.next
        sum = 0
        while (pos != None):
            sum += pos.item
            pos = pos.next
        return sum
    
    def delfirst(self, val):
        prev = self.find_prev(val)
        delnode = prev.next
        prev.next = delnode.next
        return self

    def reverse(self):
        prev = None
        curr = self.head.next

        while (curr != None):
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new
        
        self.head.next = prev

s = SLL()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
print(s)
s.reverse()
print(s)'''

'''class Stack:
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
    '''
'''
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

    def clear(self):
        pos = self.top.next
        while (pos != None):
            pos = pos.next
        self.top.next = pos
        return self

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
s.clear()
print(s)'''
'''
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
    
    def clear(self):
        for _ in range(len(self.item)):
            self.item.pop()
        return self.item

def infix_to_postfix(expression):
    # Dictionary to store operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Initialize an empty stack and an empty result string
    stack = Stack()
    postfix = ''

    for char in expression:
        # If the character is an operand, append it to the result string
        if char.isalnum():
            postfix += char
        # If the character is an opening parenthesis, push it to the stack
        elif char == '(':
            stack.push(char)
        # If the character is a closing parenthesis, pop operators from the stack and append them to the result string
        elif char == ')':
            while not stack.isempty() and stack.topelement() != '(':
                postfix += stack.pop()
            stack.pop()  # Pop the opening parenthesis from the stack
        # If the character is an operator, pop operators with higher precedence from the stack and append them to the result string
        else:
            while not stack.isempty() and stack.topelement() != '(' and precedence.get(stack.topelement(), 0) >= precedence.get(char, 0):
                postfix += stack.pop()
            stack.push(char)  # Push the current operator to the stack

    # Pop any remaining operators from the stack and append them to the result string
    while not stack.isempty():
        postfix += stack.pop()

    return postfix

infix_expression = "2 + 3 * (4 - 1)"
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)  # Output: "2 3 4 1 - * +"
'''

'''
class ShoppingCart:
    def __init__(self):
        self.tail = self.head = Node()
        self.size = 0

    def additems(self, name, price,color):
        temp = Node(name, price, color)
        temp.next = self.head.next
        self.head.next = temp
        self.size += 1

    def totalprice(self):
        pos = self.head.next
        money = 0
        while (pos != None):
            money += pos.price
            pos = pos.next
        
        return money

    def display(self):
        out = " "
        pos = self.head.next
        while (pos != None):
            out += str(pos.name) + " : " + str(pos.price) + " , " +str(pos.color) + " -> "
            pos = pos.next
        out += "END"
        return out

s = ShoppingCart()
s.additems("ABC", 100, "blue")
s.additems("DEF", 200, 'red')
s.additems("PQR", 300,'green')
print("Displaying:",s.display())
print("Total Price:",s.totalprice())'''

def bubblesort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

def selectionsort(A):
    n = len(A)
    for i in range(0,n-1):
        min = A[i]
        min_index = i
        for j in range(i+1,n):
            if A[j] < min:
                min = A[j]
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        temp = A[i]
        j = i - 1
        while (j >= 0 and A[j] > temp):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = temp
    return A

def bubblesort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] < A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        min = A[i]
        min_index = i
        for j in range(i+1,n):
            if A[j] < min:
                min = A[j]
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        temp = A[i]
        j = i - 1
        while (j >= 0 and A[j] > temp):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = temp
    return A

def binarysearch(L, low,high,srele):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if srele == L[mid]:
            return mid
        elif srele > mid:
            return binarysearch(L,mid+1,high,srele)
        elif srele < mid:
            return binarysearch(L,low,mid -1, srele)


def merge(A,B):
    C = []
    i= j= 0
    m = len(A)
    n = len(B)
    while (i < m and j < n):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if (i < m):
        C.extend(A[i:])
    elif (j < n):
        C.extend(B[j:])
    return C

print(merge([1,2,3],[4,5,6]))

def msort(L):
    length = len(L)
    if (length < 2):
        return L[:]
    else:
        mid = length // 2
        return merge(msort(L[:mid]),msort(L[mid:]))

print(msort([0]))

def median(L):
    n = len(L)
    low, mid, high = L[0], L[n // 2], L[-1]
    if low >  high:
        L[0], L[-1] = L[-1], L[0]
    if high > mid:
        L[-1], L[n//2] = L[n//2],L[-1]
    if low > mid:
        L[0], L[n//2] = L[n//2], L[0]
    return L

def partition(L,begin,end):
    pivot = L[end]
    i, j = begin, end - 1
    while (i <= j):
        while (L[i] <= pivot and i < end):
            i += 1
        while (L[j] > pivot and j >= begin):
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    L[i], L[end] = L[end], L[i]
    return i, L[i:i+1]

def qsort(L):
    if len(L) < 2:
        return L
    else:
        L = median(L)
        sorted_pos, mid = partition(L,0,len(L)-1)
        return qsort(L[:sorted_pos]) + mid + qsort(L[sorted_pos+1:])

'''class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.price = data[name][0]
        self.quantity = quantity

data = {"Earpods":[5000, 'JBL', '250NC'], 
        "iPad":[60000,'Apple', 'Pro'], 
        "Shirt":[350, 'M', 'Black'], 
        "Pant":[2000, 'S', 'Dark Blue']}
'''

class Node:
    __slots__ = ['item', 'next']
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0

    def append(self, ele):
        temp = Node(ele)
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def reverse_k_group(self, k):
        if k <= 1 or self.size < k:
            return

        dummy = Node()
        dummy.next = self.head.next
        prev_group_tail = dummy
        curr = self.head.next

        while curr:
            group_head = curr
            group_tail = curr
            count = 1

            while count < k and group_tail.next:
                group_tail = group_tail.next
                count += 1

            if count == k:
                next_group_head = group_tail.next
                self.reverse_group(group_head, group_tail)
                prev_group_tail.next = group_tail
                group_tail.next = next_group_head
                prev_group_tail = group_head
                curr = next_group_head
            else:
                break

        self.head.next = dummy.next

    def reverse_group(self, head, tail):
        curr = head
        prev = None

        while curr != tail:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        curr.next = prev
        head.next = None
        self.head.next = tail

    def display(self):
            pos = self.head
            while pos:
                print(pos.item, end=" -> ")
                pos = pos.next
            print("END")

class KValue(Exception):
    pass

# Create an instance of the SLL class
sll = SLL()

# Append elements to the linked list
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.append(7)
sll.append(8)
sll.append(9)
sll.append(10)

# Display the original linked list
print("Original Linked List:")
sll.display()
print()

# Reverse the linked list nodes in groups of size k
k = 3
sll.reverse_k_group(k)

# Display the modified linked list
print(f"Linked List with Nodes Reversed in Groups of {k}:")
sll.display()

import random

def polynomial():
    '''
    This functions takes in the degree of polynomial from user
    and uses random module to create coefficients and appends
    to a list and returns the list.

    Returns : A list of coefficients
    '''
    n = int(input("Enter the degree of polynomial: "))
    coeff = []
    for i in range(n+1):
        coeffs = random.randint(1,100)
        coeff.append(coeffs)
    
    print("Coefficients are: ", coeff)
    return coeff

def getx():
    '''
    This function takes in the value of x from user
    to evaluate the polynomial.
    
    Returns the value of x to be used in main function.
    '''
    x = int(input("Enter the value of x: "))
    return x

def Bruteforce(coeff, x):
    n = len(coeff)
    result = 0
    for i in coeff:
        coeff = i
        for j in range(1,n):
            coeff = coeff * x
        result += coeff
        n -= 1
    return result

def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        min = A[i]
        min_index = i
        for j in range(i+1, n):
            if A[j] < min:
                min = A[j]
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def insertionsort(A):
    n = len(A)
    for i in range(n):
        temp = A[i]
        j = i - 1
        while (j >= 0 and A[j]>temp):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = temp
    return A

print(insertionsort([5,4,3,2,1]))

def binarysearch(L,low,high,srele):
    if low > high:
        return -1
    else: 
        mid = (low + high)  // 2
        if srele == L[mid]:
            return mid
        elif srele > L[mid]:
            return binarysearch(L,mid + 1,high, srele)
        elif srele < L[mid]:
            return binarysearch(L,low,mid -1, srele)

def merge(a,b):
    c = []
    i = j = 0
    m = len(a)
    n = len(b)
    while (i<m and j <n):
        if (a[i] < b[j]):
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    if i < m :
        c.extend(a[:])
    if j < n :
        c.extend(b[:])
    return c

def msort(L):
    length = len(L)
    if length < 2:
        return L[:]
    else:
        mid = length // 2
        return merge(msort(L[:mid]), msort(L[mid:]))

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
    
print(qsort([90,80,70,60,50,40,30]))