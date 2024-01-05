# -*- coding: utf-8 -*-
'''This module generates a random sequence of n Points. Using a 
function that when given an integer k and a new Point PNew, k nearest
neighbouts of PNew is found.This is a part
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
    
    def pNew_distance(self,points):
        '''
        User defined method that returns distance between the
        pnew point and randomly generated n - number of points.
        '''
        distances = []
        for i in range(len(points)):
            distances.append(self.distance(points[i]))
        return distances
#End of class

#Importing random module to create random x and y coordinates.
import random


def nPoints():
    '''
    This function takes in number of points to generate and 
    lower limit and upper limit of each points as an input
    and returns a list of all the point object created
    using class Point.

    n - number of points to create
    a - lower limit of coordinate
    b - upper limit of coordinate

    Returns: List of point objects
    '''
    n = int(input("Enter the number of points to create: "))
    a = int(input("Enter the lower limit of coordinate: "))
    b = int(input("Enter the upper limit of coordintate: "))
    
    return [Point((random.randint(a,b)), (random.randint(a,b))) for i in range(n)]
#End of function nPoints

def knn(k, distances):
    '''
    This function takes in k value as an input and the distances
    list as input and sorts the distances list in ascending order
    and returns k number of points closest to Pnew point.
    '''
    for i in range(len(distances)-1):
        for j in range(i, len(distances)-1):
            if distances[j] > distances[j+1]:
                distances[j], distances[j+1] = distances[j+1], distances[j]
                points[j], points[j+1] = points[j+1], points[j]

    print("Nearest points are: ")
    for i in range(k):
        print('(', points[i]._x, ',', points[i]._y, ')' )
#End of function knn
      
#Test cases for this souce code:

if __name__ == "__main__":
    #This part of the program will not be executed when the file is imported.

    #Generating random n - number of points
    points = nPoints()
    print("The randomly generated points are: ")

    #Printing the points
    for point in points:
        print("(", point._x, ',', point._y, ")")
    
    #Finding the k - nearest neighbours to the Pnew point from 
    #the randomly generated set of points.
    pNew = Point((int(input("Enter x coord: "))), (int(input("Enter y coord: "))))
    knn(int(input("Enter k: ")), pNew.pNew_distance(points))
    print