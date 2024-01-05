# -*- coding: utf-8 -*-
"""
This module provides a data structure to maintain
two stacks in a single array . This is a part
of the exercises given under the course UIT2201w (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 31 2023

Revised on Tue June 6 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


import ctypes

class Stack:
    def __init__(self, cap):
        '''
            Constructor to initialise variables.
        '''
        self.capacity = cap
        self.top1 = 0
        self.top2 = self.capacity - 1
        self.item = self.makearray(self.capacity)
    
    def makearray(self, cap):
        '''
            Method to create compact arrays
        '''
        temp = (cap * ctypes.py_object)()
        return temp
    
    def isempty(self):
        '''
            Method to check if the data structure is empty or not.
        '''
        if self.top1 == 0 & self.top2 == self.capacity - 1:
            return True
        else:
            return False
        
    
    def push(self,n, ele):
        '''
            Method to push into stack depending on the position 1 or 0.
        '''
        if n == 0:
            self.item[self.top1] = ele
            self.top1 += 1
        elif n == 1:
            self.item[self.top2] = ele
            self.top2 -= 1
        else:
            raise ValueError("ENter only 0 or 1")
    
    def pop(self,n):
        '''
            Method to pop from stack depending the position 1 or 0.
        '''
        if n == 0:
            self.top1 -= 1
            return self.item[self.top1]
        elif n == 1:
            self.top2 += 1
            return self.item[self.top2]
        else:
            raise ValueError("ENter only 0 or 1")
        
    def __str__(self):
        '''
            Overiding to print string value of the object
        '''
        return str([self.item[i] for i in range(self.top1)]) \
        +str([self.item[i] for i in range(self.capacity-1, self.top2, -1)])
    
    def len(self,n):
        '''
            Returns the length of the data structure
        '''
        if n == 0:
            print(self.top1)
        elif n == 1:
            print(self.capacity - self.top2-1) 
        else:
            raise ValueError("enter 1 or 0")
    
    def isfull(self):
        '''
            Method to check if the data structure is full or not.
        '''
        if self.top1 > self.top2:
            return True
        else:
            return False
        
if __name__ == "__main__":
    S = Stack(5)

    S.push(0, 1)
    S.push(0,3)
    S.push(0,4)

    S.push(1,5)
    S.push(1,4)

    S.len(1)
    S.len(0)

    print(S)

    print(S.isfull())