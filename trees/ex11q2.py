# -*- coding: utf-8 -*-
"""
This module provides the mirroring of tree code . This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

In this source code I've executed my own logic and may contain bugs.
The source code has followed good coding practices.

Your comments and suggestions are welcome.

Created on Wed Jun 21 2023

Revised on Wed Jul 01 2023

Original Author: T. Sadakopa Ramakrishnan <sadakopa2210221@ssn.edu.in>
"""


from linkedbinarytree import LinkedBinaryTree

class Tree(LinkedBinaryTree):
    def __init__(self, item=None, Tleft=None, Tright=None):
        super().__init__(item, Tleft, Tright)
    
    def mirror(self, pos):
        if pos is None:
            return
        else:
            pos.left, pos.right = pos.right, pos.left #swapping right and left child
            self.mirror(pos.left) #swapping left subtree
            self.mirror(pos.right) #swapping right subtree
    
    def mirrorTree(self):
        return self.mirror(self._root)

T1 = Tree(10)
T2 = Tree(20, Tright=T1)
T3 = Tree(40, Tleft=T2)
T4 = Tree(10, T3)
T4.addRight(50, T4.root())

print("Original Tree (Preorder):", T4)
T4.mirrorTree()
print("Mirrored Tree (Preorder):", T4) 