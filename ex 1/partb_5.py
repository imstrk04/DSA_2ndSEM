# -*- coding: utf-8 -*-
"""
This module provides a function that returns p - norm value when
function is called in certain way and Euclidean value when
function is called in the other way. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 08 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""



def norm(v,p=2):
    '''
        This function takes in a tuple of values as v - vector
        and returns the p-norm value.

        v : tuple containing vectors
        p = 2 : default argument is p = 2, euclidean norm

        Returns: p-norm value when function norm(v,p) is called
                 euclidean norm when function norm(v) is called
    '''

    sum = 0 #initiallising sum = 0

    #iterating through the vectors and summing up according to value
    # of p
    for num in v:
        sum = sum + num**p
    
    #root value is 1 / p
    root = 1 / p

    #finally answer is sum power root
    ans = sum ** root

    #returning the function
    return ans

#End of function norm

#Test cases for this source code

if __name__ == "__main__":
    #This part of the program will not be executed when the file is imported.

    #Finding Euclidean norm value
    print("Euclidean norm value", norm((1,2,3,4)))
    print()

    #Finding p - norm value
    print("p - norm value", norm((1,2,3,4,5), 5))
    print()

    #Finding p - norm value for negative value of p
    print("p - norm value", norm((1,2,3,4,5), -2))
    print()

    #Finding p - norm value for p = 0
    print("p - norm value", norm((1,2,3,4,5), 0)) #Returns ZeroDivisionError: division by zero
    print()
