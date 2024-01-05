# -*- coding: utf-8 -*-
"""
This module provides a food delivery system accepts a maximum 
of M orders and uses circular queue concept.This is a part of the exercises given under 
the course UIT2201 (Programming and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 31 2023

Revised on Tue June 6 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


from circularqueue import CircularQueue

number_of_orders = int(input("Enter the number of orders: "))
food_delivery = CircularQueue(number_of_orders)


for i in range(number_of_orders):
    food_delivery.enqueue(f"Order {i+1}")

for i in range(number_of_orders):
    food_delivery.dequeue()