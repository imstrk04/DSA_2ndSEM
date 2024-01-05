'''This module creates vectors of vector class and
performs addition, subtraction, multiplication of two
vectors.This is a part of the exercises given
 under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 19 2023

Revised on Wed Apr 22 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
'''


class Vector:

  def __init__(self, val):
    if isinstance(val, int):
      self.dimension = val
      self.list = [0 for i in range(val)]
    elif isinstance(val, list):
      self.dimension = len(val)
      self.list = val
    else:
      raise TypeError("Enter only an integer or list.")

  def __len__(self):
    return self.dimension

  def __getitem__(self, index):
    return self.list[index]

  def __setitem__(self, index, val):
    self.list[index] = val
    return self.list

  def __add__(self, other):
    if self.dimension != len(other):
      raise ValueError("Dimensions of two lists do not match")
    else:
      result = [0 for i in range(self.dimension)]
      for i in range(self.dimension):
        result[i] = self.list[i] + other.list[i]
      return result

  def __sub__(self, other):
    if self.dimension != len(other):
      raise ValueError("Dimensions of two lists do not match")
    else:
      result = [0 for i in range(self.dimension)]
      for i in range(self.dimension):
        result[i] = self.list[i] - other.list[i]
      return result

  def __mul__(self, other):
    if self.dimension != len(other):
      raise ValueError("Dimensions of two lists do not match")
    else:
      result = [0 for i in range(self.dimension)]
      for i in range(self.dimension):
        result[i] = self.list[i] * other.list[i]
      return result

  def __truediv__(self, other):
    if self.dimension != other.dimension:
      raise ValueError("Dimensions of two lists do not match")
    else:
      result = [0] * self.dimension
      for iteration in range(self.dimension):
        if other.list[iteration] == 0:
          raise ZeroDivisionError("Cannot divide with 0")
        else:
          result[iteration] = self.list[iteration] / other.list[iteration]
      return result

  def __str__(self):
    return str(self.list)


if __name__ == "__main__":
    #Creating an empty Vector
    v = Vector(5)
    print("Vector V: ", v)
    print()
  
    #Assigning two values to the vector
    v[0] = 1
    v[4] = 2
    print("New vector V: ", v)
    print()
  
    #Creating a new vector V1
    v1 = Vector([1, 2, 3, 4])
    print("V1 Vector: ", v1)
    print()
  
    #Printing out the value in index 2
    print("Second index in V1: ", v1[2])
    print()
  
    #Assigning a value to 0th index
    v1[0] = 5
    print("New V1 vector: ", v1)
    print()
  
    #Creatinf a new vector V2
    v2 = Vector([1, 2, 3, 4])
    print("V2: ", v2)
    print()
  
    #Adding two vectors
    print("v1+v2:", v1 + v2)
    print()
  
    #Subtracting two vectors
    print("v1 - v2: ", v1 - v2)
    print()
  
    #Multiplying two vectors
    print("v1*v2: ", v1 * v2)
    print()
  
    #Dividing two vectors
    print("v1 / v2:", v1 / v2)
    print()
  