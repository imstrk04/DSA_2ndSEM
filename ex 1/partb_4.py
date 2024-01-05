# -*- coding: utf-8 -*-
"""
This module provides a function that returns a list in which
elements would be shuffled from main list without using the 
random module shuffle funciton. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 08 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


import random #importing random module to create elements in shuffle list
              #between the range of the the min and max value of entered sequence.


def mySHUFFLE(data ,n):
  '''
        This functions takes in an input tuple that has
        original list and number of elements and
        returns a list containing the same number of
        elements and same elements from the original list
        but shuffled without using shuffle function of 
        random module.

        tup : contains original list and length of original list as elements

        Returns : A shuffled list with elements shuffled from original list
        '''
  shuffle_list = []
  print("Original list:",data)
  if len(data) == 0:
      return shuffle_list
  for ele in data:
        if data.count(ele) == len(data):
            shuffle_list = data
            return shuffle_list
        else:
            a = min(data) #1
            b = max(data) #100
            while len(shuffle_list) != n:
                x = random.randint(a,b)
                if x in data:
                    if shuffle_list.count(x) < data.count(x):
                        shuffle_list.append(x)
                else:
                    continue
  if shuffle_list != data:
        print("Shuffled list:", shuffle_list)
  else:
        mySHUFFLE(data,n)


#Getting input from user
def user_input(n, low, high):
    '''
            This function gets 3 parameters
            n : no of elements in original sequence
            low : lower value for randint range
            high: higher value for randint range
            and returns a sequence which can be used in main function to perform
            the necessary operation.

            Returns: tuple of original list and length of original list
    '''
    data = []
    for i in range(n):
        data.append(random.randint(low, high))
    return data, n
#End of function user_input()

#Test cases for this souce code:

if __name__ == '__main__':
    #This part of the program will not be executed when the file is imported.

    #Shuffling of n elements
    mySHUFFLE([1,2,3,4,5,6], 6)
    print()

    #shuffling of empty list
    empty_list = []
    print(mySHUFFLE((empty_list),0)) #Returns an empty list
    print()

    #shiffling a list with same elements
    print(mySHUFFLE([5,5,5,5,5,5], 6)) #Returns the same original list
    print()

    #Shuffling with one elements
    print(mySHUFFLE([1],1)) #Returns the one element as a list
    print()