# -*- coding: utf-8 -*-
"""
This module provides a function that sorts the 
given elements in ascending order using quick sort which
has the time complexity of nlogn. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 10 2023

Revised on Wed May 24 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


import random
from timeit import default_timer as timer

def createLIST(n):
    '''
    This function creates a sequence of integer using random module
    '''
    seq = []
    for i in range(n):
        seq.append(random.randint(-100,100))
    print("Original List:", seq)
    return seq

def median(L):
    '''
    This function returns the median index to use that 
    as the pivot element. It swaps the median element to the
    last position.
    '''
    n = len(L)
    low, mid, high = L[0], L[n//2], L[n-1]
    if low > high:
        L[0], L[n-1], L[n-1], L[0]
    if high > mid:
        L[n-1], L[n//2] = L[n//2], L[n-1]
    if low > mid:
        L[0], L[n//2] = L[n//2], L[0]
    return L


def partition(L, begin, end):
    '''
    This function partition the given list using in such a way
    the elements to the left of the pivot element are lesser than
    pivot element and elements to the right of the pivot elements
    are greater than the pivot elements.
    '''
    comparisons = 0
    swappings = 0
    pivot = L[end]
    i, j = begin, end - 1
    while(i<=j): 
        while(L[i]<=pivot and i<end):
            comparisons += 1
            i += 1
        while(L[j]>pivot and j>=begin):
            comparisons += 1
            j -= 1
        if i<j:
            swappings += 1
            L[i], L[j] = L[j], L[i]
    swappings += 1
    L[i], L[end] = L[end], L[i]
    return i, L[i: i+1], comparisons, swappings


def quick_sort(L):
    '''
    This function takes the partition list and then
    sort it in ascending order.
    '''
    if len(L) < 2:
        return L, 0, 0
    else:
        L = median(L)
        postion, mid, comparisons1,swappings1 = partition(L, 0, len(L) - 1)
        lhs, comparisons2, swappings2 = quick_sort(L[:postion])
        rhs, comparisons3,swappings3 = quick_sort(L[postion + 1:])
        return lhs + mid + rhs, comparisons1 + comparisons2 + comparisons3,swappings1 + swappings2+ swappings3


start = timer()
list,comparisons, swappings = quick_sort([10,9,8,7,6,5,4,3,2,1])
print("Sorted List: ")
print(list)
print("Total Comparisons:", comparisons)
print("Total Swapings:", swappings)
end = timer()
print("The time taken is", end - start)