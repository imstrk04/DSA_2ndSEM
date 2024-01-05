'''#List ADT - Dynamic Array
import ctypes
class DynamicArray:
    def __init__(self,val):
        if isinstance(val, int):
            self._n = 0
            self._capacity = val
            self._A = self.makearray(self._capacity)
        else:
            self.n = len(val)
            self._capacity = 2 * self._n
            self._A = self.makearray(self._capacity)
            for i in range(self._n):
                self._A[i] = val[i]
    
    def makearray(self,cap):
        temp = (cap * ctypes.py_object())
        return temp
    
    def resize(self,cap):
        B = self.makearray(cap)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = cap
    
    def append(self, ele):
        if self._n == self._capacity:
            self.resize(2 * self._capacity)
        self._A[self._n] = ele
        self._n += 1
    
    def insert(self,index,ele):
        if not (index <= self._n):
            raise IndexError("Index out of Range")
        
        if self.n == self._capacity:
            self.resize(2 * self._capacity)
        
        for i in range(self._n, index, -1):
            self._A[i] = self._A[i-1]
        
        self._A[index] = ele
        self._n += 1
    
    def __str__(self):
        return str([self._A[i] for i in range(self._n)])

    def __len__(self):
        return self._n
    
    def __setitem__(self,index,ele):
        self._A[index] = ele
        return self._A

    def delete(self, index):
        if not (index < self._n):
            raise IndexError("Index out of Range")
        
        for i in range(index, self._n - 1):
            self._A[i] = self._A[i+1]
        self._n -= 1

        if self._n < (self._capacity // 4):
            self.resize(self._capacity // 2)

    def __contains__(self,ele):
        for i in self._A:
            if ele == i:
                return True
        return False

    def extend(self, other_list):
        new_size = self._n + len(other_list)

        if new_size > self._capacity:
            self.resize(new_size)
        
        for item in other_list:
            self._A[self._n] = item
            self._n += 1
    
    def index(self,item):
        for i in range(self._n):
            if self._A[i] == item:
                return i
        raise ValueError(f"{item} not found in the list.")
    
    def count(self,item):
        count = 0
        for i in range(self._n):
            if self._A[i] == item:
                count += 1
        return count

#Stack - Wrapper Method
class WrapperStack:
    def __init__(self):
        self.item = []
        self.top = 0
    def isEmpty(self):
        return len(self.item) == 0

    def push(self,ele):
        self.item.append(ele)
    
    def pop(self):
        return self.item.pop()
        
    def __len__(self):
        return len(self.item)
    
    def __str__(self):
        return str(self.item)
    
    def topelement(self):
        return self.item[-1]
    
#Driver code for WrapperStack:
S = WrapperStack()
S.push(1)   
S.push(2)   
S.push(3)   
S.push(4)   
S.push(5)   
S.push(6)   
print("S:", S)
print("Top:",S.topelement())
print("Pop:", S.pop())
print("New S:", S)

#Queue - Wrapper Method
class WrapperQueue:
    def __init__(self):
        self.item = []
        self.front = 0
        self.rear = 0
    
    def isEmpty(self):
        return self.front == self.rear

    def enqueue(self, ele):
        self.item.insert(self.rear, ele)
        self.rear += 1
    
    def dequeue(self):
        return self.item.pop(0)

    def __len__(self):
        return self.rear - self.front
    
    def __str__(self):
        return str(self.item)

#Driver Code for WrapperQueue:
Q = WrapperQueue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.enqueue(6)
print("Q:", Q)
print("Dequeue:", Q.dequeue())
print("New Q:", Q)

'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_tree(self, string):
        S = Stack()

        for ch in string:
            if self.is_operand(ch):
                node = Node(ch)
                S.push(node)
            else:
                node = Node(ch)
                r_child = S.pop()
                l_child = S.pop()
                node.right = r_child
                node.left = l_child
                S.push(node)
        self.root = S.pop()

    def evaluate_tree(self):
        return self.evaluate_expression(self.root)

    def is_operand(self, ch):
        return ch.isdigit()

    def evaluate_expression(self, node):
        if self.is_operand(node.item):
            return int(node.item)

        left_value = self.evaluate_expression(node.left)
        right_value = self.evaluate_expression(node.right)

        operator = node.item

        if operator == '+':
            return left_value + right_value
        elif operator == '-':
            return left_value - right_value
        elif operator == '*':
            return left_value * right_value
        elif operator == '/':
            return left_value // right_value

# Example usage
string = input("Enter postfix expresion using [1,5,6,7] and [+,-,*,/]: ")
tree = ExpressionTree()
tree.build_tree(string)
result = tree.evaluate_tree()
print("Result:", result)
