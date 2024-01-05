# -*- coding: utf-8 -*-
"""
This module checks if the entered string is a palindrome
or not using both stack and queue. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 31 2023

Revised on Tue June 6 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""



from stack import Stack
from queue import Queue

def ispalindrome(): 
    S = Stack()
    Q = Queue()

    num = input("Enter something to check if its palindrome: ")
    for i in range(len(num)):
        S.push(num[i]) 
        Q.enqueue(num[i])

    while True:
        if S.pop() != Q.dequeue():
            print("Not a palindrome")
            break
        else:
            print("Palindrome")
            break

ispalindrome()