import random
from timeit import default_timer as timer
class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def display_area(self):
        print(f"Rectangle area: {self.calculate_area()}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def display_area(self):
        print(f"Triangle area: {self.calculate_area()}")


# Example usage:
if __name__ == "__main__":
    side_length = float(input("Enter the side length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    rectangle = Rectangle(side_length, width)
    rectangle.display_area()

    base_length = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    triangle = Triangle(base_length, height)
    triangle.display_area()


'''class Node:
    def __init__(self,item = None, next = None):
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
    
    def __str__(self):
        string = ""
        pos = self.head.next
        while pos != None:
            string += str(pos.item) + " -> "
            pos = pos.next
        string += "END"
        return string

    def last_before(self):
        pos = self.head.next
        while pos.next != self.tail:
            pos = pos.next
        last_before = pos.item
        return last_before


    
S = SLL()
n = int(input("How many inputs u wanna give: "))
for i in range(n):
    value = int(input("Enter the value: "))
    S.append(value)

print("Original Linked List:",S)
print("Last before element:", S.last_before())'''


'''
Given an integer array nums, return the maximum difference 
between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.

You must write an algorithm that runs in 
linear time and uses linear extra space.
'''

'''def user_input():
    n = int(input("how many elements: "))
    lst = []
    for i in range(n):
        lst.append(int(input("Enter the values: ")))
    return lst

def Merge(a,b):
    c = []
    i = j = 0
    m = len(a)
    n = len(b)
    while (i < m and j < n):
        if b[j] < a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i+=1    
    if i < len(a):
        c.extend(a[i:])
    elif j < len(b):
        c.extend(b[j:])
    return c

def MergeSort(list):
    n = len(list)
    if n < 2:
        return list[:]
    else:
        mid = n // 2
        return Merge(MergeSort(list[:mid]), MergeSort(list[mid:]))

def final(lst):
    print("Sorted Int array:",lst)
    l1 = []
    for i in range(1,len(lst)):
        l1.append(lst[i]-lst[i-1])
    return max(l1)

print(final(MergeSort(user_input())))
'''

'''class Node:
    def __init__(self,item = None):
        self.item = item
        self.left = None
        self.right = None
        self.parent = None

class LBT:
    def __init__(self, item = None, t_left = None, t_right = None):
        self.root = None
        self.size = 0
        if item is not None:
            self.root = self.addRoot(item)
            if t_left is not None:
                if t_left.root is not None:
                    t_left.root.parent = self.root
                    self.root.left = t_left.root
                    self.size += t_left.size
            if t_right is not None:
                if t_right.root is not None:
                    t_right.root.parent = self.root
                    self.root.right = t_right.root
                    self.size += t_right.size
    
    def addRoot(self,item):
        if self.root is not None:
            raise ValueError("Root already exists")       
        self.root = Node(item)
        self.size += 1
        return self.root

    def populate_tree(self):
        print("Enter the root node: ")
        value = int(input())
        self.root = Node(value)
        self.populate(self.root)

    def populate(self,node):
        print("Do you want to enter left of", node.item,"? (True/False): ")
        left = input().lower() == 'true'
        if left:
            print("Enter the value to left of", node.item,": ")
            value = int(input())
            node.left = Node(value)
            self.populate(node.left)

        print("Do you want to enter right of", node.item,"? (True/False): ")
        right = input().lower() == 'true'
        if right:
            print("Enter the value right of", node.item,": ")
            value = int(input())
            node.right = Node(value)
            self.populate(node.right)
    
    def display(self):
        return self.inorder(self.root)
    
    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(str(root.item), end = " ")
        self.inorder(root.right)

    def delete_pos(self,pos):
        if pos is self.root:
            self.root = None
            self.size = 0
        else:
            parent = pos.parent
            if pos == parent.left:
                parent.left = None
            if pos == parent.right:
                parent.right = None


L = LBT()
root = L.addRoot(10)
L.populate_tree()
L.display()
L.delete_pos(root)'''


#SORTING ALGORITHMS

#creating a list
'''import random
from timeit import default_timer as timer

def createLIST():
    n = int(input("Enter the number of elements: "))
    L = []
    for i in range(n):
        L.append(random.randint(1,100))
    print("Original List:", L)
    return L

#bubble sort

def BubbleSort(list):
    fn = 0
    swap = 0
    n = len(list)
    start = timer()
    for i in range(0,n-1):
        fn += 1
        for j in range(0,n-i-1):
            fn += 1
            if list[j] > list[j+1]:
                swap += 1
                list[j], list[j+1] = list[j+1], list[j]
    end = timer()
    print("f(n) =", fn)
    print("No of swappings:", swap)
    print("Exact Time:",end - start)
    return list

#print("Sorted list(Bubble sort):",BubbleSort(createLIST()))

#selection sort
def SelectionSort(seq):
    n = len(seq)
    fn = 0
    swap = 0
    start = timer()
    for i in range(n):
        fn += 1
        minIndex = i
        for j in range(i+1,n):
            fn += 1
            if seq[minIndex] > seq[j]:
                swap += 1
                minIndex = j
        seq[i], seq[minIndex] = seq[minIndex], seq[i]
    end = timer()
    print("f(n) =", fn)
    print("No of swappings:", swap)
    print("Exact Time:",end - start)
    return seq

#print("Sorted list(Selection sort):",SelectionSort(createLIST()))

def InsertionSort(seq):
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    for i in range(1,n):
        fn += 1
        temp = seq[i]
        j = i - 1
        while (j >= 0 and seq[j] >temp):
            fn += 1
            seq[j+1] = seq[j]
            j = j - 1
            swap += 1
        seq[j+1] = temp
    end = timer()
    print("f(n) =", fn)
    print("No of swappings:", swap)
    print("Exact Time:",end - start)
    return seq

#print("Sorted List(insertion sort): ", InsertionSort(createLIST()))

def Merge(a,b):
    c = []
    i = j = 0
    m = len(a)
    n = len(b)
    while (i < m and j < n):
        if b[j] < a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    if i < len(a):
        c.extend(a[i:])
    elif j < len(b):
        c.extend(b[j:])
    return c

def MergeSort(list):
    n = len(list)
    if n < 2:
        return list[:]
    else:
        mid = n // 2
        return Merge(MergeSort(list[:mid]), MergeSort(list[mid:]))

#print("Sorted List (MergeSort):", MergeSort(createLIST()))

def median(L):
    n = len(L)
    low, mid, high = L[0], L[n//2], L[n-1]
    if low > high:
        L[0], L[n-1] = L[n-1], L[0]
    if high > mid:
        L[n-1], L[n//2] = L[n//2], L[n-1]
    if low > mid:
        L[0], L[n//2] = L[n//2], L[0]
    return L

def partition(L, begin, end):
    pivot = L[end]
    i, j = begin, end -1
    while (i <= j):
        while (L[i] <= pivot and i < end):
            i += 1
        while (L[j] > pivot and j >= begin):
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    L[i], L[end] = L[end], L[i]
    return i, L[i:i+1]

def quickSort(L):
    if len(L) < 2:
        return L
    else:
        position, mid = partition(L,0,len(L)-1)
        lhs = quickSort(L[:position])
        rhs = quickSort(L[position+1:])
        return lhs + mid + rhs

#print("Sorted LIst(QUick Sort): ", quickSort(createLIST()))

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
    
class Vector:
    def __init__(self,val):
        if isinstance(val, int):
            self.dimension = val
            self.list = [0 for i in range(val)]
        elif isinstance(val, list):
            self.dimension = val
            self.list = list
        else:
            raise TypeError("Enter only an integer or list")
    
    def __len__(self):
        return self.dimension
    
    def __getitem__(self,index):
        return self.list[index]
    
    def __setitem__(self, index, val):
        self.list[index] = val
        return self.list
    
    def __add__(self,other):
        if self.dimension != len(other):
            raise ValueError("Dimensions of two vectors arent same")
        else:
            result = [0 for i in range(self.dimension)]
            for i in range(self.dimension):
                result[i] = self.list[i] + other.list[i]
            return result
    
    def __sub__(self, other):
        if self.dimension != len(other):
            raise ValueError("Dimensions of two vectors arent same")
        else:
            result = [0 for i in range(self.dimension)]
            for i in range(self.dimension):
                result[i] = self.list[i] - other.list[i]
            return result
    
    def __mul__(self, other):
        if self.dimension != len(other):
            raise ValueError("Dimensions of two vectors arent same")
        else:
            result = [1 for i in range(self.dimension)]
            for i in range(self.dimension):
                result[i] = self.list[i] * other.list[i]
            return result
    
    def __truediv__(self, other):
        if self.dimension != len(other):
            raise ValueError("Dimensions of two vectors arent same")
        else:
            result = [0] * self.dimension
            for i in range(self.dimension):
                if other.list[i] == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                else:
                    result[i] = self.list[i] / other.list[i]
            return result
    
    def __str__(self):
        return str(self.list)


v = Vector(5)
print("Vector V:", v)
print()

v[0] = 1
v[4] = 2
print("New Vector V:",v)
print()'''

'''class Vector:

    def __init__(self, val):
        if isinstance(val, int):
            self.dimension = val
            self.list = [0 for i in range(val)]
        if isinstance(val, list):
            self.dimension = len(val)
            self.list = val
    
    def __len__(self):
        return self.dimension

    def __getitem__(self, index):
        return self.list[index]

    def __setitem__(self,index, value):
        self.list[index] = value
        return self.list
    
    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions should be same")
        else:
            result = [0 for i in range(self.dimension)]
            for i in range(self.dimension):
                result[i] = self.list[i] + other.list[i]
            return result
    
    def __sub__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions should be same")
        else:
            result = [0 for i in range(self.dimension)]
            for i in range(self.dimension):
                result[i] = self.list[i] - other.list[i]
            return result
    
    def __mul__(self,other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions should be same")
        else:
            result = [0 for i in range(self.dimension)]
            for i in range(self.dimension):
                result[i] = self.list[i] * other.list[i]
            return result
    
    def __truediv__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimensions should be same")
        else:
            result = [0 for i in range(self.dimension)]
            for i in range(self.dimension):
                if other.list[i] == 0:
                    raise ZeroDivisionError("Cant divide with 0")
                else:
                    result[i] = self.list[i] / other.list[i]
            return result
    
    def __str__(self):
        return str(self.list)
    
V1 = Vector([1,2,3,4])
print("Vector V1:", V1)
print()

V2 = Vector(4)
print("Vector V2:", V2)
print()

for i in range(4):
    V2[i] = int(input("Enter value: "))
print("Vector V2:", V2)
print()

print("V1 / V2:", V1 / V2)
print()'''

'''from typing import Any


class Matrix:
    def __init__(self, row = 0, col = 0):
        self.row = row
        self.col = col
        self.order = (self.row, self.col)
        self.matrix = []
        for i in range(row):
            l1 = [0] * col
            self.matrix.append(l1)
    
    def __getitem__(self,index):
        return self.matrix[index[0]][index[1]]
    
    def __setitem__(self,index, value):
        self.matrix[index[0]][index[1]] = value
        return self.matrix
    
    def __add__(self,other):
        if self.order != other.order:
            raise ValueError("Dimensions of matrices arent same")
        else:
            result = [[0 for j in range(self.col)] for i in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
    
    def __sub__(self,other):
        if self.order != other.order:
            raise ValueError("Dimensions of matrices arent same")
        else:
            result = [[0 for j in range(self.col)] for i in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result
    
    def __mul__(self,other):
        if self.order != other.order:
            raise ValueError("Dimensions of matrices arent same")
        else:
            result = [[0 for j in range(self.col)] for i in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] = self.matrix[i][j] * other.matrix[i][j]
            return result

    def chanfe_values(self):
        for r in range(self.row):
            for c in range(self.col):
                self.matrix[r][c] += random.randint(0,10)
        return self.matrix

    def __str__(self):
        return str(self.matrix)

M1 = Matrix(3,3)
M2 = Matrix(3,3)

M1.chanfe_values()
M2.chanfe_values()
print("M1:", M1)
print("M2:", M2)
print("M1 + M2: ", M1 + M2)
print("M1 - M2:", M1 - M2)
print("M1 * M2:", M1 * M2)
'''

'''class Point:

    def __init__(self, a, b):
        self.x = a
        self.y = b
        return
    
    def distance(self,other):
        x_diff = (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        dist = (x_diff + y_diff) ** 0.5
        print(dist)
    
p1 = Point(2,3)
p2 = Point(3,4)
p1.distance(p2)'''

'''class Rational:

    def __init__(self, num: int = 0, den : int = 1):
        if not isinstance(num, int):
            raise TypeError("Numerator must be an integer")
        if not isinstance(den, int):
            raise TypeError("Denominator must be an integer")
        if (den == 0):
            raise ZeroDivisionError("Denominator cant be zero")
    
    def __add__(self, other):
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = (self.den * other.den)
        return Rational(new_num, new_den)
    
    def __sub__(self,other):
        new_num = (self.num * other.den) - (self.den * other.num)
        new_den = (self.den * other.den)
        return Rational(new_num, new_den)

    def __mul__(self,other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Rational(new_num, new_den)

    def __str__(self):
        return str(f"{self.num} / {self.den}")
    
    def __invert__(self):
        return Rational(self.den, self.num)

    def __truediv__(self, other):
        return self.__mul__(~other)
    
    def __float__(self, other):
        return (self.num / self.den)

    def __int__(self):
        return (self.num // self.den)
    
    def __eq__(self, other):
        return (self.num == other.num) and (self.den == other.den)
    
    def __ne__(self, other):
        return (self.num == other.num) or (self.den == other.den)
    
    def __lt__(self,other):
        return (self.__float__() < other.float())
    
    def __le__(self,other):
        return (self.__float__() <= other.float())
    
    def __gt__(self,other):
        return (self.__float__() > other.float())
    
    def __ge__(self,other):
        return (self.__float__() >= other.float())'''

'''class ComplexNumber:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

# Example usage:
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, -1)

print("c1:", c1)
print("c2:", c2)

add_result = c1 + c2
print("Addition:", add_result)

sub_result = c1 - c2
print("Subtraction:", sub_result)

mul_result = c1 * c2
print("Multiplication:", mul_result)

div_result = c1 / c2
print("Division:", div_result)

conjugate_c1 = c1.conjugate()
print("Conjugate of c1:", conjugate_c1)'''

def createList():
    n = int(input("Enter number of elements: "))
    seq = []
    for i in range(n):
        seq.append(random.randint(0,1000))
    print("Original List:", seq)
    return seq

def bubbleSort(seq):
    n = len(seq)
    fn = 0
    swap = 0
    start = timer()
    for i in range(n-1):
        fn += 1
        for j in range(n - i - 1):
            fn += 1
            if seq[j] > seq[j+1]:
                swap += 1
                seq[j], seq[j+1] = seq[j+1], seq[j]
    end = timer()
    print("F(n):", fn)
    print("No of comparisons:", swap)
    print("Total time:",end - start)
    return seq

#print("Sorted List:", bubbleSort(createList()))

def selectionSort(seq):
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    for i in range(n-1):
        fn += 1
        minIndex = i
        for j in range(i+1, n):
            fn += 1
            if seq[minIndex] > seq[j]:
                swap += 1
                minIndex = j
        seq[i], seq[minIndex] = seq[minIndex], seq[i]
    end = timer()
    print("F(n):", fn)
    print("No of comparisons:", swap)
    print("Total time:",end - start)   
    return seq

#print("Sorted List:", selectionSort(createList()))

def InsertionSort(seq):
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    for i in range(1,n):
        fn += 1
        temp = seq[i]
        j = i - 1
        while (j >= 0 and seq[j] > temp):
            fn += 1
            seq[j+1] = seq[j]
            j = j - 1
            swap += 1
        seq[j+1] = temp
    end = timer()
    print("F(n):", fn)
    print("No of comparisons:", swap)
    print("Total time:",end - start)
    return seq

#print("Sorted List:", InsertionSort(createList()))


def Merge(a, b, fn, swap):
    c = []
    m = len(a)
    n = len(b)
    i = j = 0
    while i < m and j < n:
        fn += 1
        if b[j] < a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
            swap += 1
    
    while i < m:
        c.append(a[i])
        i += 1

    while j < n:
        c.append(b[j])
        j += 1
    
    return c, fn, swap

def MergeSort(seq, fn = 0, swap = 0):
    n = len(seq)
    if n < 2:
        return seq, fn, swap
    else:
        mid = n // 2
        left,fn,swap = MergeSort(seq[:mid], fn, swap)
        right,fn,swap = MergeSort(seq[mid:], fn, swap)
        merged_seq, fn, swap = Merge(left,right,fn, swap)
        return merged_seq, fn, swap

def EmpiricalAnalysisMergeSort(seq):
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    sorted_seq, fn, swap = MergeSort(seq, fn, swap)
    end = timer()
    print("Sorted sequence:", sorted_seq)
    print("F(n):", fn)
    print("No of comparisons:", swap)
    print("Total time:", end - start)
    return sorted_seq

'''# Example usage:
seq = [4, 1, 7, 3, 8, 5, 2, 6]
print("Original sequence:", seq)'''

#EmpiricalAnalysisMergeSort(seq)

'''def median(L):
    n = len(L)
    low, mid,high = L[0], L[n//2], L[n-1]
    if low>high:
        L[0], L[n-1] = L[n-1], L[0]
    if high > mid:
        L[n-1], L[n//2] = L[n//2], L[n-1]
    if low > mid:
        L[0], L[n // 2] = L[n // 2], L[0]
    return L

def partition(L,begin,end):
    fn = 0
    swap = 0
    pivot = L[end]
    i, j = begin, end -1
    while (i <=j):
        while(L[i] <= pivot and i < end):
            fn += 1
            i += 1
        while (L[j] > pivot and j >= begin):
            fn += 1
            j -= 1
        if i < j:
            swap += 1
            L[i], L[j] = L[j], L[i]
    L[i], L[end] = L[end], L[i]
    return i, L[i:i+1], fn, swap

def quick_sort(L):
    if len(L) < 2:
        return L, 0, 0
    else:
        L = median(L)
        position, mid, fn1, swap1 = partition(L,0,len(L)-1)
        lhs, fn2, swap2 = quick_sort(L[:position])
        rhs, fn3, swap3 = quick_sort(L[position + 1:])
        return lhs + mid + rhs, fn1 + fn2 + fn3, swap1 + swap2 + swap3

start = timer()
list, fn, swap = quick_sort(createList())
print("Sorted List: ")
print(list)
print("Total Comparisons:", fn)
print("Total Swapings:", swap)
end = timer()
print("The time taken is", end - start)'''

def median(L):
    n = len(L)
    low, mid, high = L[0], L[n // 2], L[n-1]
    if low > high:
        L[0], L[n-1] = L[n-1], L[0]
    if high > mid:
        L[n-1], L[n//2] = L[n//2], L[n-1]
    if low > mid:
        L[0], L[n//2] = L[n//2], L[0]
    return L

def partition(L, begin, end):
    fn = 0
    swap = 0
    pivot = L[end]
    i,j = begin, end -1
    while ( i<=j):
        while(L[i]<= pivot and i < end):
            fn += 1
            i += 1
        while(L[j] > pivot and j >= begin):
            fn += 1
            j -= 1
        if (i < j):
            swap += 1
            L[i], L[j] =L[j], L[i]
    L[i], L[end] = L[end], L[i]
    return i, L[i:i+1], fn, swap

def quick_sort(L):
    n = len(L)
    if n < 2:
        return L, 0,0
    else:
        L = median(L)
        position, mid, fn1, swap1 = partition(L, 0, len(L)-1)
        lhs, fn2, swap2 = quick_sort(L[:position])
        rhs, fn3, swap3 = quick_sort(L[position+1:])
        return lhs + mid + rhs, fn1 + fn2 + fn3, swap1+swap2+swap3

'''start = timer()
list, fn, swap = quick_sort(createList())
print("Sorted List: ")
print(list)
print("F(n):", fn)
print("Swappings:", swap)
end = timer()
print("Time taken:", end - start)'''

'''def BinarySearch(list, low, high, srele):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if srele == list[mid]:
            return mid
        elif srele < list[mid]:
            return BinarySearch(list, low, mid -1, srele)
        elif srele > list[mid]:
            return BinarySearch(list, mid + 1, high, srele)
    
print(BinarySearch([1,2,3,4], 0, 3, 2))'''

class Product:
    __slots__ = ['name', 'price', 'quantity']
    def __init__(self, name, quantity):
        self.name = name
        self.price = data[name][0]
        self.quantity = quantity
    
    def display_information(self):
        print(f"Name: {self.name} \n Price: {self.price} \n Quantity: {self.quantity}", end = " ")


class ElectronicProduct(Product):
    def __init__(self,name,quantity,brand,model):
        super().__init__(name, quantity)
        self.brand = data[name][1]
        self.model = data[name][2]
    
    def display_information(self):
        super().display_information()
        print(f"\t\tBrand: {self.brand}\t\tModel: {self.model}")


data = {"Earpods":[5000, 'JBL', '250NC'], 
        "iPad":[60000,'Apple', 'Pro'], 
        "Shirt":[350, 'M', 'Black'], 
        "Pant":[2000, 'S', 'Dark Blue']}

'''        
output = [] 
operator = []
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^':3}
exp = input("Enter infix expression: ")
for ch in exp:
    if ch == '(':
        operator.append(ch)
    elif ch == ')':
        while (operator[-1] != '('):
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif ch == '^' or ch == '*' or ch == '/' or ch == '+' or ch == '-':
        if len(operator) != 0:
            while (priority[operator[-1]]>= priority[ch]):
                ele = operator.pop()
                output.append(ele)
                if len(operator) == 0:
                    break
        operator.append(ch)
    else:
        output.append(ch)
while (len(operator) != 0):
    ele = operator.pop()
    output.append(ele)

print("Infix exp:", exp)
print("Postfix exp:", end = " ")
for ele in output:
    print(ele, end = '')
'''
'''output = []
operator = []
priority = {'(':0, '+':1, '-':1, '*':2, '/':2, '^':2}
exp = input("Enter infix expression: ")

for ch in exp:
    if ch == '(':
        operator.append(ch)
    elif ch == ')':
        while (operator[-1] != '('):
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif ch == '^' or ch == '/' or ch == '*' or ch == '+' or ch == '-':
        if len(operator) != 0:
            while (priority[operator[-1]]>=priority[ch]):
                ele = operator.pop()
                output.append(ele)
                if len(operator) == 0:
                    break
        operator.append(ch)
    else:
        output.append(ch)

while (len(operator)!= 0):
    ele = operator.pop()
    output.append(ele)

print("Infix: ",exp)
print("Postfix exp: ", end = '')
for ele in output:
    print(ele, end = "")'''

'''output = []
operator = []
priority = {'(':2, '+':1, '-': 1, '*' :2, '/':2, '^':2}
exp = input("Enter infix: ")

for ch in exp:
    if ch == '(':
        operator.append(ch)
    elif ch == ')':
        while (operator[-1] != '('):
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif ch == '^' or ch == '/' or ch == '*' or ch == '-' or ch == '+':
        if len(operator) != 0:
            while (priority[operator[-1]]>= priority[ch]):
                ele = operator.pop()
                output.append(ele)
                if len(operator) == 0:
                    break
        operator.append(ch)
    else:
        output.append(ch)

while (len(operator)!= 0):
    ele = operator.pop()
    output.append(ele)

print("infix:", exp)
print("Postfix:", end ='')
for ele in output:
    print(ele, end='')'''
'''
output = []
operator = []
priority = {'(': 0, '+':1, '-':1, '*':2, '/':2,'^':2}
exp = input("enter infix: ")

for ch in exp:
    if ch == '(':
        operator.append(ch)
    elif ch == ')':
        while operator[-1] != '(':
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif ch == '^' or ch == '/' or ch == '*' or ch == '+' or ch == '-':
        if len(operator) != 0:
            while (priority[operator[-1]]>= priority[ch]):
                ele = operator.pop()
                output.append(ele)
                if len(operator) == 0:
                    break
        operator.append(ch)
    else:
        output.append(ch)
while len(operator) != 0:
    ele = operator.pop()
    output.append(ele)

'''

'''output = []
operator = []
priority = {'(':0, '+': 1, '-': 1, '*':2, '/':2, '^':2}
exp = input("enter infix: ")

for ch in exp:
    if ch == "(":
        operator.append(ch)
    elif ch == ')':
        while operator[-1] != '(':
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif ch == '^' or ch == '+' or ch == '-' or ch == '*' or ch == '/':
        if len(operator) == 0:
            while (priority[-1]>=priority[ch]):
                ele = operator.pop()
                output.append(ele)
        operator.append(ch)
    else:
        output.append(ch)

while len(operator) != 0:
    ele = operator.pop()
    output.append(ele)
'''


'''class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, ele):
        self.list.append(ele)
    
    def pop(self):
       return self.list.pop()
    
    def top(self):
        return self.list[-1]
    
    def __len__(self):
        return len(self.list)
    
    def __str__(self):
        return str(self.list)

    def __isempty__(self):
        return len(self.list) == 0
    
class Queue:
    def __init__(self):
        self.item = []
        self.front = 0
        self.rear = 0
    
    def isEmpty(self):
        return self.front == self.rear
    
    def enqueue(self,ele):
        self.item.insert(self.rear, ele)
        self.rear += 1
    
    def dequeue(self):
        return self.item.pop(0)

    def __len__(self):
        return self.rear - self.front

    def __str__(self):
        return str(self.item)

def isPalindrome():
    S = Stack()
    Q = Queue()

    num = input("Enter: ")
    for i in range(len(num)):
        S.push(num[i])
        Q.enqueue(num[i])
    
    while True:
        if S.pop() != Q.dequeue():
            print("Not a palindrome")
            break
        else:
            print("palindrome")
            break

isPalindrome()'''

import ctypes

'''class DynamicStack:

    def __init__(self, cap):
        self.top = 0
        self.cap = cap
        self.A = self.makearray(cap)
    
    def makearray(self, cap):
        temp = (cap * ctypes.py_object)()
        return temp
    
    def resize(self,cap):
        B = self.makearray(cap)
        for i in range(self.cap-1):
            B[i] = self.A[i]
        self.A = B
        self.cap = cap
    
    def isEmpty(self):
        return self.top == 0
    
    def push(self,ele):
        if self.top == self.cap:
            self.resize(2*self.cap)
        self.A[self.top] = ele
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        ele = self.A[self.top -1]
        self.A[self.top -1] =None
        self.top -= 1
        if (self.top < (self.cap) // 4):
            self.resize(self.cap // 2)
        return ele
    
    def __len__(self):
        return self.top
    
    def __str__(self):
        return str(self.A)
    

class Empty(Exception):
    pass'''

'''class DynamicArray:
    def __init__(self, val):
        if isinstance(val, int):
            self.n = 0
            self.cap = val
            self.A = self.makearay(self.cap)
        else:
            self.n = len(val)
            self.cap = 2 * self.n
            self.A = self.makearray(self.cap)
            for i in range(self.n):
                self.A[i] = val[i]
        
    def makearray(self, cap):
       
        temp = (cap * ctypes.py_object)()
        return temp
    
    def resize(self, cap):
    
        B = self.makearray(cap)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = cap

class Node:
    def __init__(self,item = None, next = None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0
    
    def append(self, val):
        temp = Node(val)
        self.tail.next = temp
        self.tail = temp
        self.size += 1
    
    def __str__(self):
        out = ''
        pos = self.head.next
        while (pos != None):
            out += str(pos.item) + " -> "
            pos = pos.next
        out += "END"
        return out
    
    def find_prev(self, pos):
        curr = self.head.next
        while curr != None:
            if curr.next == pos:
                return curr
            curr = curr.next

    def swap(self, index1, index2):
        if index1 == index2:
            # No need to swap if indices are the same
            return

        pos1 = self.head.next
        for i in range(index1):
            if not pos1:
                return  # Index out of range
            prev1 = pos1
            pos1 = pos1.next

        pos2 = self.head.next
        for i in range(index2):
            if not pos2:
                return  # Index out of range
            prev2 = pos2
            pos2 = pos2.next

        if not pos1 or not pos2:
            return  # Index out of range

        # Check if nodes to be swapped are adjacent
        if pos1.next == pos2:
            prev1.next = pos2
            pos1.next = pos2.next
            pos2.next = pos1
        elif pos2.next == pos1:
            prev2.next = pos1
            pos2.next = pos1.next
            pos1.next = pos2
        else:
            prev1.next = pos2
            temp = pos2.next
            pos2.next = pos1.next
            prev2.next = pos1
            pos1.next = temp
    
    def reverse(self):
        prev = None
        curr = self.head.next
        self.tail = curr

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        self.head.next = prev

s = SLL()
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
s.append(60)
print(s)
s.reverse()
print(s)'''

'''class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
        self.parent = None

class BinarySearchTree:
    def createNode(self,data):
        return Node(data)

    def insert(self,node,value):
        if node is None:
            return self.createNode(value)
        
        if value < node.data:
            node.left = self.insert(node.left,value)
            node.left.parent = node
        
        if value > node.data:
            node.right = self.insert(node.right, value)
            node.right.parent = node
        
        return node

    def traverse_inorder(self, root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data, end = " ")
            self.traverse_inorder(root.right)

    def traverse_preorder(self, root):
        if root is not None:
            print(root.data, end = " ")
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
    
    def traverse_postorder(self, root):
        if root is not None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data, end = " ")

    def level_order(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            root = q.pop(0)
            print(root.data, end = "")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
    
    def find_min(self,root):
        if root.left is None:
            return root.data
        return self.find_min(root.left)
    
    def find_max(self,root):
        if root.right is None:
            return root.data
        return self.find_max(root.right)
    
    def find_ele(self,root,ele):
        if root is None:
            return None
        
        if root.data == ele:
            return root
        
        left_result = self.find_ele(root.left, ele)
        if left_result is not None:
            return left_result
        
        right_result = self.find_ele(root.right, ele)
        if right_result is not None:
            return right_result
        
        return None

    def delete_value(self,root,ele):
        return self.delete_node(self.find_ele(root,ele))

    def delete_node(self,node):
        
        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current
        
        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        #CASE 1 - No children
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            if node_parent.right == node:
                node_parent.right = None
        
        #CASE 2 - 1 children
        if node_children == 1:
            if node.left != None:
                child = node.left
            if node.right != None:
                child = node.right
            
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child
            child.parent = node_parent
        
        #CASE 3 - 2 Children
        if node_children == 2:
            successor = min_value_node(node.right)

            node.data = successor.data

            self.delete_node(successor)

tree = BinarySearchTree()
root = tree.createNode(10)
tree.insert(root, 5)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 8)
tree.insert(root, 2)
tree.insert(root,1)
print("Inorder: ", end = "")
tree.traverse_inorder(root)
print()
print("Preorder: ", end = "")
tree.traverse_preorder(root)
print()
print("Postorder: ", end = "")
tree.traverse_postorder(root)
print()
minimum = tree.find_min(root)
print("Minimum element:", minimum)
maximum = tree.find_max(root)
print("Maximum Element:", maximum)
print("Deleting node(10):")
tree.delete_value(root,10)
tree.traverse_inorder(root)
print()
print("Deleting node(2):")
tree.delete_value(root,2)
tree.traverse_inorder(root)
print()
print("Deleting node(1):")
tree.delete_value(root,1)
tree.traverse_inorder(root)
print()'''

from linkedbinarytree import LinkedBinaryTree

'''class ExpressionTree(LinkedBinaryTree):
    def __init__(self, item = None, Tleft = None, Tright = None):
        super().__init__(item, Tleft, Tright)
    
    def construct(self,expr):
        S = []
        for ch in expr:
            if ch in '+*-/':
                rchild = S.pop()
                lchild = S.pop()
                S.append(ExpressionTree(ch, lchild, rchild))
            else:
                S.append(ExpressionTree(ch))
        return S.pop()
    
    def __str__(self):
        return str(self.inorder(self._root))

    def inorder(self, pos):
        res = ""
        if pos is None:
            return None
        if pos.left is not None:
            res += self.inorder(pos.left)
        res += str(pos.item)
        if pos.right is not None:
            res += self.inorder(pos.right)
        return res
    
    

e1 = ExpressionTree()
exp = input("Enter expression: ")
print("Postorder: ",exp)
e1.root = e1.construct(exp)
print("Inorder: ",e1.root)
'''

'''class Tree(LinkedBinaryTree):
    def __init__(self, item = None, Tleft = None, Tright = None):
        super().__init__(item, Tleft, Tright)
    
    def mirror(self, pos):
        if pos is None:
            return
        else:
            pos.left, pos.right = pos.right, pos.left
            self.mirror(pos.left)
            self.mirror(pos.right)
    
    def mirrorTree(self):
        return self.mirror(self._root)

T1 = Tree(10)
T2 = Tree(20, Tright= T1)
T3 = Tree(40, Tleft = T2)
T4 = Tree(10, T3)
T4.addRight(50, T4.root())

print("Original Tree (Preorder):", T4)
T4.mirrorTree()
print("Mirrored Tree (Preorder):", T4) '''

from abstracttree import AbstractTree

'''class TreeNode:
    def __init__(self,name):
        self.name = name
        self.children = []
    
class FamilyTree(AbstractTree):
    def __init__(self):
        self._root = None
        self._size = 0
    
    def root(self):
        return self._root
    
    def parent(self,pos):
        pass

    def num_children(self,pos):
        node = pos
        return len(node.children)
    
    def children(self,pos):
        node = pos
        return node.children
    
    def __len__(self):
        return self._size
    
    def add_child(self,parent,child_name):
        new_child = TreeNode(child_name)
        parent.children.append(new_child)
        self._size += 1
    
    def print_tree(self, node, level = 0):
        if node is not None:
            print(" "*level + node.name)
            for child in node.children:
                self.print_tree(child, level+1)

family_tree = FamilyTree()

family_tree._root = TreeNode("Sadagopan")

family_tree.add_child(family_tree._root, "Thothathiri")
family_tree.add_child(family_tree._root, "Suba")

thothathiri = family_tree.children(family_tree._root)[0]
suba = family_tree.children(family_tree._root)[1]

family_tree.add_child(thothathiri, "Sadakopa")
family_tree.add_child(thothathiri, "Barshana")

family_tree.add_child(suba, "Achu")
family_tree.add_child(suba, "Aravind")

print("Family Tree: ")
family_tree.print_tree(family_tree._root)'''



'''output = [] 
operator = []
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^':3}
exp = input("Enter infix expression: ")
for ch in exp:
    if ch == '(':
        operator.append(ch)
    elif ch == ')':
        while (operator[-1] != '('):
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif ch == '^' or ch == '*' or ch == '/' or ch == '+' or ch == '-':
        if len(operator) != 0:
            while (priority[operator[-1]]>= priority[ch]):
                ele = operator.pop()
                output.append(ele)
                if len(operator) == 0:
                    break
        operator.append(ch)
    else:
        output.append(ch)
while (len(operator) != 0):
    ele = operator.pop()
    output.append(ele)

print("Infix exp:", exp)
print("Postfix exp:", end = " ")
for ele in output:
    print(ele, end = '')'''

'''class TreeNode:
    def __init__(self,name):
        self.name = name
        self.children = []
        self.parent = None
    
class FamilyTree(AbstractTree):
    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._root
    
    def parent(self,pos):
        return pos.parent

    def num_children(self, pos):
        node = pos
        return len(node.children)
    
    def children(self,pos):
        node = pos
        return node.children
    
    def __len__(self):
        return self._size
    
    def add_child(self, parent, child_name):
        new_child = TreeNode(child_name)
        new_child.parent = parent
        parent.children.append(new_child)
        self._size += 1
    
    def print_tree(self, node, level = 0):
        if node is not None:
            print(" "*level + node.name)
            for child in node.children:
                self.print_tree(child, level+1)

    def ancestors(self, pos, ancestors_list = None):
        if ancestors_list == None:
            ancestors_list = []
        
        if pos != self.root():
            parent = self.parent(pos)
            ancestors_list.append(parent.name)
            self.ancestors(parent,ancestors_list)
        
        return ancestors_list

    def decendants(self,pos, decendants_list = None):
        if decendants_list is None:
            decendants_list = []
        
        decendants_list.append(pos.name)

        for child in self.children(pos):
            self.decendants(child, decendants_list)

        return decendants_list

    def subfamily(self, pos, sub_family_list = None):
        if sub_family_list is None:
            sub_family_list = []
        
        sub_family_list.append(pos.name)

        for child in self.children(pos):
            self.subfamily(child, sub_family_list)
        
        return sub_family_list

family_tree = FamilyTree()

family_tree._root = TreeNode("Sadagopan")

family_tree.add_child(family_tree._root, "Thothathiri")
family_tree.add_child(family_tree._root, "Suba")

thothathiri = family_tree.children(family_tree._root)[0]
suba = family_tree.children(family_tree._root)[1]

family_tree.add_child(thothathiri, "Sadakopa")
family_tree.add_child(thothathiri, "Barshana")

family_tree.add_child(suba, "Achu")
family_tree.add_child(suba, "Aravind")

print("Family Tree: ")
family_tree.print_tree(family_tree._root)

# Print the Family Tree
print("Family Tree:")
family_tree.print_tree(family_tree._root)

# Find ancestors of a particular node (e.g., "Aravind")
aravind = TreeNode("Aravind")
ancestors_of_aravind = family_tree.ancestors(aravind)
print("Ancestors of Aravind:", ancestors_of_aravind)

# Find descendants of a particular node (e.g., "Sadagopan")
sadagopan = TreeNode("Sadagopan")
descendants_of_sadagopan = family_tree.descendants(sadagopan)
print("Descendants of Sadagopan:", descendants_of_sadagopan)

# Find the sub-family rooted at a node (e.g., "Thothathiri")
thothathiri = TreeNode("Thothathiri")
sub_family_of_thothathiri = family_tree.subfamily(thothathiri)
print("Sub-Family of Thothathiri:", sub_family_of_thothathiri)

'''

def selectionsort(seq):
    n = len(seq)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if (seq[minIndex] > seq[j]):
                minIndex = j
        seq[i], seq[minIndex] = seq[minIndex], seq[i]
    return seq

def insertionSort(seq):
    n = len(seq)
    for i in range(1,n):
        temp = seq[i]
        j = i - 1
        while (j >= 0 and seq[j] > temp):
            seq[j+1] = seq[j]
            j = j - 1
        seq[j+1] = temp

  