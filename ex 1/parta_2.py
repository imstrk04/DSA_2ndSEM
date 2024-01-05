# -*- coding: utf-8 -*-
"""
This module provides a function that returns a tuple
containing the minimum and maximum value of a sequence
without using the inbuilt pyton functions. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 09 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""



def minmax(data):
    '''
    This function takes in a sequence of objects and
    returns a tuple having minimum value and maximum value 
    of the given sequence without using inbuilt functions.
    The input sequence must have indices for the elements
    to be defined. Further, we assume that all elements in the
    sequence can be compared using the python operators.

    The input sequence maybe empty, in that case None is returned.

    data : input sequence

    Returns : a tuple containing min and max value of the input sequence
    '''
    count = 0
    #finding size of the given sequence
    size = len(data)

    #Returing None for empty input sequence
    if size == 0:
        count += 1
        return None

    #Returning the only element present in a single element sequence
    if size == 1:
        count += 1
        return (data[0], data[0])
    
    #Returning tuple using basic if-else statement when only 2 elements are input
    if size == 2:
        count += 1
        if data[0] < data[1]:
            count += 1
            return (data[0], data[1])
        else:
            count += 1
            return (data[1], data[0])
        
    #For size of input sequence greater than  2
    else:
        count += 1
        #assigning first element of list as maximum value
        MAXM = data[0] 

        #assigning first element of list as minimum value
        MINM = data[0] 

        #iterating through data
        for maxm in data: 
            #checking if each element is greater than previously assigned max value
            if maxm > MAXM: 
                count += 1
                MAXM = maxm  #if condition holds good


        #iterating through data
        for minm in data: 
            #checking if each element is lesser than previously assigned min value
            if minm < MINM:
                count += 1 
                MINM = minm #if condition holds good

        #packing of tuple with minm and maxm value of input sequence        
        tup = (MINM,MAXM)
        print("Number of comparisons:", count)
        #Returning the tuple
        return tup
#End of function minmax()  


# We will use the random module to generate an integer within
# a given range under uniform distribution

import random
def createLIST(n,low,high):
  '''
    This function gets 3 parameters
    n : no of elements in original sequence
    low : lower value for randint range
    high: higher value for randint range
    and returns a sequence which can be used in main function to perform
    the necessary operation.
  '''
  seq = []
  for i in range(n):
    seq.append(random.randint(low,high))
  return seq
#End of function createLIST()

if __name__ == "__main__":
     #This part of the program will not be executed when the file is imported.

    data = [] #Empty list test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print()

    data = () #Empty tuple test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print()

    data = [1] #Single element test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print()

    data = createLIST(5,-10,10) #Both positive and negative numbers test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print()

    data = createLIST(10,0,10)  #only positive numbers test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print()

    data = createLIST(5,5,5) #same elements test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print()
    
    data = tuple(createLIST(10,-100,100)) #tuple of random numbers test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print()

    data = ['A', 'B', 'C', 'D', 'E'] #A list of characters test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print()

    data = {x for x in range(1,11)} #A set of numbers test case
    print("Test case is:", data)
    print("Output of the function", minmax(data))
    print() #set cannot be indexed, thus it needs to be converted to a list