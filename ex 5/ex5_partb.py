# -*- coding: utf-8 -*-
'''This module provides the sorting algorithm, 
Insertion Sort. The empirical Analysis is
done with Bubble Sort and Selection Sort.The
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

def InsertionSort(seq):
    '''
    This function sorts the entered sequence using Insertion Sort
    which has time complexity of O(n^2)
    '''
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
            j = j-1
            swap += 1
        seq[j+1] = temp
    end = timer()
    print("f(n) =", fn)
    print("No of swapings:", swap)
    print("Exact time:",end - start )
    return seq

#Test cases for this source code:

if __name__ == "__main__":

    #Insertion Sort
    print("Using Insertion Sort: ")
    print(InsertionSort([10,6,4,100,22,44,223,4433]))
    print()