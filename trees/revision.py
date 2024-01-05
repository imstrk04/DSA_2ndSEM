class Node:
    __slots__ = ['item', 'next']
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
class SinglyLinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        self.size = 0
    
    def isempty(self):
        return self.head == self.tail

    def append(self, ele):
        temp = Node(ele)
        self.tail.next = temp
        self.tail = temp
        self.size += 1
    
    def display(self):
        pos = self.head.next
        res = ""
        while pos is not None:
            res += str(pos.item) + " -> "
            pos = pos.next
        res += "END"
        return res
    
    def find(self, ele):
        pos = self.head.next
        while (pos != None):
            if pos.item == ele:
                return pos
            pos = pos.next
        return None

    def remove(self,ele):
        prev = self.find_prev(ele)
        delnode = prev.next
        prev.next = delnode.next

    def find_prev(self,ele):
        pos = self.head.next
        while (pos.next is not None):
            if pos.next.item == ele:
                return pos
            pos = pos.next
        return None
    
    def insert(self,position,ele):
        pos = self.head.next
        for i in range(position-1):
            pos = pos.next
        temp = Node(ele, pos.next)
        pos.next = temp
    
    def __str__(self):
        res = ""
        pos = self.head.next
        while pos != None:
            res += str(pos.item) + " -> "
            pos = pos.next
        res += "END"
        return res

class DNode(Node):
    __slots__ = ['prev']
    def __init__(self, item, next, prev = None):
        super().__init__(item, next)
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = DNode()
        self.size = 0
    
    def isEmpty(self):
        return self.head == self.tail

    def append(self, ele):
        temp = DNode(ele)
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.size += 1
    
    def display(self):
        res = ""
        pos = self.head.next
        while pos != None:
            res += str(pos.item) + " <-> "
            pos = pos.next
        res += "END"
        return res

    def reverse_display(self):
        res = ""
        pos = self.tail
        while pos != None:
            res += str(pos.item) + " <-> "
            pos = pos.prev
        res += "END"
        return res

    def find(self,ele):
        pos = self.head.next
        while (pos != None):
            if pos.item == ele:
                return pos
            pos = pos.next
        return None

    def insert(self, position, ele):
        pos = self.head.next
        if pos.next == None:
            self.append(ele)
            self.size += 1
        else:
            for i in range(position - 1):
                pos = pos.next
            temp = DNode(ele)
            temp.prev = pos
            temp.next = pos.next
            pos.next.prev = temp
            pos.next = temp
            self.size += 1
    
    def remove(self,ele):
        if self.isEmpty():
            raise Empty("List empty")
        else:
            if ele == self.head.next.item:
                delnode = self.head.next
                self.head.next = delnode.next
                delnode.next.prev = self.head
                self.size -= 1
            else:
                prev = self.find_prev(ele)
                if prev is None:
                    print("Element not present")
                    delnode = None
                else:
                    delnode = prev.next
                    prev.next = delnode.next
                    delnode.next.prev = prev
                    self.size -= 1
        return delnode


    def find_prev(self,ele):
        pos = self.head.next
        while pos.next != None:
            if pos.item == ele:
                return pos
        return None
       
class LinkedStack:
    __slots__ = ['top']
    def __init__(self):
        self.top = Node()
        self.size = 0
    
    def isempty(self):
        return self.top.next == None
    
    def top(self):
        if self.isempty():
            raise Empty("Stack Empty")
        else:
            return self.top.next.item

    def push(self,item):
        temp = Node(item)
        temp.next = self.top.next
        self.top.next = temp
        self.size +=1 
    
    def pop(self):
        delnode = self.top.next
        self.top.next = delnode.next
        self.size -= 1
    
    def __str__(self):
        res = ""
        pos = self.top.next
        while (pos != None):
            res += str(pos.item) + "->"
            pos = pos.next
        res += "END"
        return res

class Empty(Exception):
    pass

class LinkedQueue:
    __slots__ = ['front', 'rear']
    def __init__(self):
        self.rear = self.front = Node()
        self.size = 0

    def isEmpty(self):
        return self.rear == self.front
    
    def enqueue(self,ele):
        temp = Node(ele)
        temp.next = self.rear.next
        self.rear.next = temp
        self.size += 1
    
    def dequeue(self):
        delnode = self.front.next
        self.front.next = delnode.next
        self.size -= 1

    def front(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        else:
            return self.front.item
    
    def __str__(self):
        res = ""
        pos = self.front.next
        while (pos != None):
            res += str(pos.item) + " -> "
            pos = pos.next
        res += "END"
        return res

class CircularLinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        self.tail.next = self.head
        self.size = 0
    
    def isEmpty(self):
        return self.head.next == self.head

    def append(self, ele):
        temp = Node(ele)
        temp.next = self.head
        self.tail.next = temp
        self.size += 1
    
    def display(self):
        pos = self.head.next
        first = str(pos.item)
        out = ""
        while (pos != self.head):
            out += str(pos.item) + " <-> "
            pos = pos.next
        out += first
        return out

    def delete(self, val):
        curr = self.head.next
        n = curr.next
        if curr.item == val:
            self.head = self.head.next
            self.tail.next = self.head
            return
        for i in range(self.size):
            if curr.item == val:
                curr
from abc import ABC, abstractmethod

class AbstractTree(ABC):
    @abstractmethod
    def getRoot(self):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def getParent(self):
        raise Exception("Not Implemented")

    @abstractmethod
    def getChildren(self):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def getNum_Children(self):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def __len__(self):
        raise Exception("Not Implemented")
    
    def isRoot(self, pos):
        return self.getRoot() == pos
    
    def isLeaf(self,pos):
        return self.getNum_Children(pos) == 0
    
    def isEmpty(self):
        return len(self) == 0
    
    def depthN(self,pos):
        if pos is None:
            return 0
        else:
            return 1 + self.depthN(self.getParent(pos))
    
    def heightN(self,pos):
        if pos is None:
            return 0
        else:
            return 1 + max([self.heightN(child) for child in self.getChildren(pos)])
    
    def height(self):
        return self.heightN(self.getRoot())
    
class AbstractBinaryTree(AbstractTree):
    @abstractmethod
    def getLeft(self):
        raise Exception("Not Implemented")
    
    @abstractmethod
    def getRight(self):
        raise Exception("Not Implemented")
    
    def getChildren(self, pos):
        if pos is None:
            return None
        if self.getLeft(pos) is not None:
            yield self.getLeft(pos)
        if self.getRight(pos) is not None:
            yield self.getRight(pos)

    def sibling(self,pos):
        parent = self.getParent(pos)
        if parent is None:
            return None
        if pos == self.getRight(parent):
            return self.getLeft(parent)
        else:
            return self.getRight(parent)

class LinkedBinaryTree(AbstractBinaryTree):
    class BTNode():
        __slots__ = ['item', 'left', 'right', 'parent']
        def __init__(self,item, left = None, right = None, parent = None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent
        
        def __getitem__(self):
            return self.item
        
        def __setitem__(self,item):
            self.item = item
    
    __slots__ = ['root', 'size']
    def __init__(self, item = None, t_left= None, t_right = None):
        self.root = None
        self.size = 0
        if item is not None:
            self.root = self.addRoot(item)
        if t_left is not None:
            if t_left.root is not None:
                t_left.root.parent = self.root
                self.root.left = t_left.root
                self.size += t_left.size
                t_left.root = None
        if t_right is not None:
            if t_right.root is not None:
                t_right.root.parent = self.root
                self.root.right = t_right.root
                self.size += t_right.size
                t_right.root = None

    def addRoot(self,item):
        if self.root is not None:
            raise ValueError("Root already exists")
        else:
            self.root = self.BTNode(item)
            self.size += 1
            return self.root
    
    def __len__(self):
        return self.size
    
    def getParent(self,pos):
        return pos.parent
    
    def getLeft(self,pos):
        return pos.left
    
    def getRight(self,pos):
        return pos.right

    def getSize(self):
        return self.size
    
    def getNum_Children(self,pos):
        if pos is None:
            return 0
        else:
            return 1 + self.getNum_Children(pos.left) + self.getNum_Children(pos.right)
    
    def addLeft(self,item,pos = None):
        if pos is None:
            pos = self.root
        if self.getLeft(pos) is not None:
            raise ValueError("Left child Already exist")
        else:
            pos.left = self.BTNode(item, parent = pos)
            self.size += 1
            return pos.left
    
    def addRight(self,item,pos = None):
        if pos is None:
            pos = self.root
        if self.getRight(pos) is not None:
            raise ValueError("Right child already exist")
        else:
            pos.right = self.BTNode(item, parent = pos)
            self.size += 1
            return pos.right
    
    def preorder(self, pos):
        self.string += str(pos.item) + ","
        if pos.left is not None:
            self.preorder(pos.left)
        if pos.right is not None:
            self.preorder(pos.right)
    
    def postorder(self,pos):
        if pos.left is not None:
            self.postorder(pos.left)
        if pos.right is not None:
            self.postorder(pos.right)
        self.string += str(pos.item) + ","
    
    def inorder(self,pos):
        if pos.left is not None:
            self.postorder(pos.left)
        self.string += str(pos.item) + ","
        if pos.right is not None:
            self.postorder(pos.right)
    
    def __str__(self):
        self.string = "The preorder is: "
        self.preorder(self.root)
        self.string = self.string[:-1]
        self.string = "The postorder is: "
        self.postorder(self.root)
        self.string = self.string[:-1]
        self.string = "The inorder is: "
        self.inorder(self.root)
        self.string = self.string[:-1]
        return self.string

    def mirror(self,pos):
        if pos is None:
            return 
        else:
            pos.left, pos.right = pos.right, pos.left
            self.mirror(pos.left)
            self.mirror(pos.right)
    
    def mirrorTree(self):
        return self.mirror(self.root)

'''class ExpressionTree(LinkedBinaryTree):
    def __init__(self, item = None, t_left = None, t_right = None):
        super().__init__(item, t_left, t_right)
    
    def construct(self, expr):
        S = LinkedStack()
        for ch in expr:
            if ch in '+*-/':
                rchild = S.pop()
                lchild = S.pop()
                S.push(ExpressionTree(ch,lchild,rchild))
            else:
                S.push(ExpressionTree(ch))
        return S.pop()'''
    
'''    def inorder(self, pos):
        if pos.left is not None:
            self.postorder(pos.left)
        self.string += str(pos.item) + ","
        if pos.right is not None:
            self.postorder(pos.right)
    
    def __str__(self):
        return str(self.inorder(self.root))'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)  # Dummy header node

    def append(self, value):
        new_node = Node(value)
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node

    def display(self):
        curr = self.head.next

        while curr:
            print(curr.value, end=" ")
            curr = curr.next

        print()
    
    def swapAdjacentNodes(dummy_header):
        prev_node1 = dummy_header
        node1 = dummy_header.next
        new_head = node1.next

        while node1 and node1.next:
            node2 = node1.next

            prev_node1.next = node2
            node1.next = node2.next
            node2.next = node1

            prev_node1 = node1
            node1 = node1.next

        return new_head

# Creating a linked list with dummy header
linked_list = LinkedList()

# Appending elements to the linked list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# Displaying the initial linked list
print("Initial Linked List:")
linked_list.display()

# Swapping adjacent nodes
new_head = swapAdjacentNodes(linked_list.head)

# Displaying the modified linked list
print("Modified Linked List:")
linked_list.display()



