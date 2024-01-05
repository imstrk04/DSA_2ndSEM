# -*- coding: utf-8 -*-
"""
This module provides a function that sorts the 
given elements in ascending order using merge sort which
has the time complexity of nlogn. This module also contains
binary search that takes in the sorted list from
merge sort and then search for the search element. It has
time complexity of logn. This is a part
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

def Merge(a,b):
    '''
    Merge function takes in two lists a and b and then 
    merges the two lists into one with the elements
    arranged in ascending order.

    Input : 2 lists
    Returns : a merged list
    '''
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
    '''
    This function splits the input list into two and
    calls the merge() function to merge the two lists
    with elements arranged in ascending order by using
    recursion.
    '''
    n = len(list)
    if n < 2:
        return list[:]
    else:
        mid = n // 2
        return Merge(MergeSort(list[:mid]), MergeSort(list[mid:]))

def BinarySearch(list, low, high, srele):
    '''
    Takes in a sorted list and searches for a search
    element by dividing the list into two for every iteration
    '''
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if srele == list[mid]:
            return mid
        elif srele < list[mid]:
            return BinarySearch(list,low, mid-1, srele)
        elif srele > list[mid]:
            return BinarySearch(list, mid+1, high, srele)

start = timer()
print("Sorted List: ", MergeSort(createLIST(10)))
end = timer()
print("Time taken is", end - start)

print("The search element is present at",BinarySearch(MergeSort(createLIST(10)),0,9,15))