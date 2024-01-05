# -*- coding: utf-8 -*-
"""
This module provides a function that returns distinct pairs of
numbers whose product is an odd number. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 08 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


import random #importing random module for creating a list to be given as input

def distinctPAIR(seq):
  '''
    This function takes in a sequence as input and 
    returns a list of tuple having distinct pairs of 
    numbers whose product is odd.
    
    The input sequence may be empty, in which case 'None' is 
    returned.

    seq : input list that can be used to find distinct pairs
    
    Returns : A list of tuple having distinct pairs of numbers 
                whose product is an odd
  '''

  count = 0  
  print("Orginal seq:", seq) #printing orginal sequence

  odd_seq = [] #creating an empty list to store only odd numbers from the given seq


  #iterating through given sequence to find odd numbers and appending to empty list

  for num in seq:
    if num % 2 != 0:
      count += 1
      odd_seq.append(num)
    
  odd_seq.sort() #useful for one extreme test case

  prod_list = [] #creating an empty list to store the cartesian product between 
                 # next next numbers in the odd seq


  #two for loops to get the cartesian product and appending it to the empty list

  for i in range(len(odd_seq)):
    for j in range(i+1,len(odd_seq)):
        prod_list.append((odd_seq[i], odd_seq[j]))
  
  pairs = [] #creating an empty to list to store the non repeating pairs

  #for loop followed by an if statement to remove the repeating pairs
  #and appending to a new list

  for i in prod_list:
    if i not in pairs:
      count += 1
      pairs.append(i)

  #checking if number of pairs is 0, if it is then printing no distinct pairs
  #else printing out the pairs

  if len(pairs) == 0:
    count += 1
    print("Number of comparisons:", count)
    return "No distinct pairs"
  else:
    count += 1
    print("Number of comparisons:", count)
    return pairs
#End of function distinctPAIR()


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

#Test cases for the following source code:

if __name__ == '__main__':
    #This part of the program will not be executed when the file is imported.

    #Finding distinct pairs for positive numbers
    print("Distinct pairs:", distinctPAIR(createLIST(5,10,100)))
    print()

    #Finding distinct pairs for negative numbers
    print("Distinct pairs:", distinctPAIR(createLIST(10,-100,-10)))
    print()

    #Finding distinct pairs for repeating case
    print("Distinct pairs:", distinctPAIR([1,2,1]))
    print()

    #Finding distinct pairs for both positive numbers and negative numbers
    print("Distinct pairs:", distinctPAIR(createLIST(5,-10,10)))
    print()

    #Finding distinct pairs for one extreme case
    print("Distinct pairs:", distinctPAIR([3,4,7,5,3]))
    print()