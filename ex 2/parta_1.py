# -*- coding: utf-8 -*-
'''This module returns the distance between
two points given by user.This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 12 2023

Revised on Wed Apr 14 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
'''


class Point:
    '''
    
    '''
    _x = 0
    _y = 0
    def __init__(self, a, b):
        '''Constructor to initialize the datamembers'''
        self._x = a
        self._y = b
        return

    def distance(self, other):
        '''User defined method that returns the distance between two points'''
        x_diff = (self._x - other._x) ** 2
        y_diff = (self._y - other._y) ** 2
        dist = (x_diff + y_diff) ** 0.5
        return dist
#End of class Point

def user_input():
    '''
    This function takes in x coordinate and y coordinate
    as input from user and creates two point objects of
    class point and returns the distance between two points
    using user defined distance() method.
    '''
    n = 2
    points_lst = [] 
    for i in range(n):
        x_coord = int(input("Enter x coord: "))
        y_coord = int(input("Enter y coord: "))
        p = Point(x_coord, y_coord)
        print((p._x, p._y))
        points_lst.append(p)

    p1 = Point(points_lst[0]._x, points_lst[0]._y)
    p2 = Point(points_lst[1]._x, points_lst[1]._y)
    d = p1.distance(p2)
    return d
#End of function user_input()


#Test cases for this souce code:

if __name__ == "__main__":
    #This part of the program will not be executed when the file is imported.

    #Calculating distance between two points
    print(user_input()) 
    print()