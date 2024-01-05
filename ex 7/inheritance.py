# -*- coding: utf-8 -*-
"""
This module contains a program applying the concept
of Inheritance of Classes. This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed May 17 2023

Revised on Wed May 28 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


class Product:
    '''
    This the parent class.
    '''
    def __init__(self,name, quantity):
        '''
        Constructor to initialise variables
        '''
        self._name = name
        self._price= data[name][0]
        self._quantity = quantity

    def display_information(self):
        '''
        Method to display information
        '''
        print(f"Name: {self._name} \nPrice: {self._price} \nQuantity: {self._quantity}", end = '')

class ElectronicProduct(Product):
    '''
    Child Class of the Parent class Product
    '''
    def __init__(self,name,quantity,brand,model):
        '''
        Constructor to initialise the variables
        '''
        super().__init__(name,quantity)
        self._brand = data[name][1]
        self._model = data[name][2]

    def display_information(self):
        '''
        Overriding the display_information() method from Parent class
        '''
        super().display_information()
        print(f"\t\tBrand: {self._brand}\t\tModel: {self._model}")

    def __add__(self, other):
        '''
        Method to create Combo Products
        '''
        name = self._name + " and " + other._name
        price = self._price + other._price
        quantity = self._quantity + other._quantity
        total_price = price * quantity
        brand = self._brand +" and "+ other._brand
        model = self._model + " and "+ other._model
        data[name] = [total_price, brand, model]
        return ElectronicProduct(name, quantity,brand,model)

class ClothingProduct(Product):
    '''
    Child class of the Parent class
    '''
    def __init__(self,name,quantity, size, color):
        '''
        Constructor to initialise variables
        '''
        super().__init__(name, quantity)
        self._size = data[name][1]
        self._color = data[name][1]

    def display_information(self):
        '''
        Method to display information
        '''
        super().display_information()
        print(f"\t\tSize: {self._size}\t\tColor: {self._color}")

    def __add__(self, other):
        '''
        Method to create combo products
        '''
        name = self._name + " and " + other._name
        price = self._price + other._price
        quantity = self._quantity + other._quantity
        total_price = price * quantity
        size = self._size +" and " +other._size
        color = self._color +" and "+ other._color
        data[name] = [total_price, size, color]
        return ClothingProduct(name, quantity,size,color)
    
#DataBase
data = {"Earpods":[5000, 'JBL', '250NC'], 
        "iPad":[60000,'Apple', 'Pro'], 
        "Shirt":[350, 'M', 'Black'], 
        "Pant":[2000, 'S', 'Dark Blue']}

#Test cases for the above code
if __name__ == "__main__":
    #This part of the program will not be executed when the file is imported.

    #Creating Electronic product object 1
    e1 = ElectronicProduct('Earpods', 5,'JBL','250NC')
    e1.display_information()
    print()

    #Creating Electronic product object 2
    e2 = ElectronicProduct('iPad', 10, 'Apple', 'Pro')
    e2.display_information()
    print()

    #Combo product object
    e3 = e1 + e2
    e3.display_information()
    print()

    #Creating clothing product object 1
    c1 = ClothingProduct("Shirt", 100, 'XL', "Red")
    c1.display_information()
    print()

    #Creating clothing product object 2
    c2 = ClothingProduct("Pant", 50, "L", "Black")
    c2.display_information()
    print()

    #Combo Product object
    c3 = c1 + c2
    c3.display_information()
    print()