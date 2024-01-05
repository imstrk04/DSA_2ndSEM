# -*- coding: utf-8 -*-
'''This module provides the sorting algorithms,
namely Bubble Sort and Selection Sort. The empirical
analysis is done for both the algorithms and
O(n^2) complexity is verified.The
module provides the total run time of the algorithm
along with the sorted list. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 3 2023

Revised on Wed May 7 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
'''


import random
from timeit import default_timer as timer

def createLIST():
    '''
    This function creates a sequence of integer using random module
    '''
    n = int(input("Enter the number of elements: "))
    seq = []
    for i in range(n):
        seq.append(random.randint(-5,1500))
    print("Original List:", seq)
    return seq

def BubbleSort(seq):
    '''
    This function sorts the entered sequence using BubbleSort which has time complexity of O(n^2)
    '''
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    for i in range(0,n-1):
        fn += 1
        for j in range(0,n-i-1):
            fn += 1
            if seq[j] > seq[j+1]:
                swap += 1
                seq[j] , seq[j+1] = seq[j+1], seq[j]
    end = timer()
    print("f(n) =", fn)
    print("No of swapings:", swap)
    print("Exact time:",end - start )
    return seq

def SelectionSort(seq):
    '''
    This function sorts the entered sequence using Selection Sort which has time complexity of O(n^2)
    '''
    fn = 0
    swap = 0
    n = len(seq)
    start = timer()
    for i in range(n):
        fn += 1
        minIndex = i
        for j in range(i+1, n):
            fn += 1
            if seq[minIndex] > seq[j]:
                swap += 1
                minIndex = j

        seq[i], seq[minIndex] = seq[minIndex], seq[i]
    end = timer()
    print("f(n) =", fn)
    print("No of swapings:", swap)
    print("Exact time:",end - start )
    return seq

#Test cases for this source code:

if __name__ == "__main__":

    #Bubble Sort
    print("Using Bubble Sort: ")
    print(BubbleSort(createLIST()))
    print()

    #Selection Sort
    print("Using Selection Sort: ")
    print(SelectionSort(createLIST()))
    print()