# -*- coding: utf-8 -*-
"""
This module provides a function that returns all possible
arithmetic operations for the given inputs. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 08 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


def checkOPERATION(a,b,c): #defining an user defined function
    '''
        This function takes in three integer inputs a,b and c
        and returns all the possible arithmetic formulas following
        a particular order.

        a,b,c : three integers as input

        Returns : All possible arithmetical operations possible
    ''' 
    
    #Initialising sum, diff, prod, div, floor_div, exponent in a variable
    #to compare using if-else conditonal statements

    sum = a + b    
    diff = b - c   
    prod = a * b   
    div = a / b    
    floor_div = a // b  
    expo = a ** b  
    
    #Initialising output in a variable to append it to a final ans_list
    #and only print out the elements of ans_list

    sum_output = "a + b = c is possible"
    diff_ouput = "a - b = c is possible"
    prod_output = "a * b = c is possible"
    div_ouptut = "a / b = c is possible"
    floor_div_output = "a // b = c is possible"
    expo_output = "a ** b = c is possible"

    #creating an empty ans_list to append output message
    ans_list = []


    #if statements to check the possible operations
    if sum == c: 
        ans_list.append(sum_output)
    if diff == a:
        ans_list.append(diff_ouput)
    if prod == c: 
        ans_list.append(prod_output)
    if div == c: 
        ans_list.append(div_ouptut)
    if floor_div == c: 
        ans_list.append(floor_div_output)
    if expo == c: 
        ans_list.append(expo_output)
    
    if len(ans_list) > 0:
        for output in ans_list:
            print(output)
    else:
        print("None of the case is possible")

#End of function checkOPERATION()

#Testcases for the following source code:

if __name__ == "__main__":
    #This part of the program will not be executed when the file is imported.

    #Checking for same value of a,b and c
    checkOPERATION(1,1,1)
    print()

    #Checking for consecutive numbers
    checkOPERATION(5,4,7)
    print()

    #Checking for negative numbers
    checkOPERATION(-1,-5,-6)
    print()

    checkOPERATION(1,2,3)
    print()

    #Checking for all zeroes
    checkOPERATION(0,0,0) #Returns error, ZeroDivisionError: division by zero
    print()