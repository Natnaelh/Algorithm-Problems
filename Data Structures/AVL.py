#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:06:44 2020

@author: natnem
"""

import bst

def height(node):
    if node is None:
        return -1
    else:
        return node.height
def update_height(node):
    node.height = max(height(node.left) , height(node.right)) + 1

class AVL(bst.BST):
    
    
    def leftRotate(self, x):
        y = x.right
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        else:
            if x is y.parent.left:
                x.parent.left = y
            elif x is y.parent.right:
                x.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)
    def rightRotate(self, x):
        y = x.left
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x is y.parent.left:
                x.parent.left = y
            elif x is y.parent.right:
                x.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)
    
    
    def rebalance(self,node):
        while node is not None:
            
    
    
    
    
#    def insertAVL(self, t):
#        node = bst.BST.Insert(t)
##        self.     
            
        
                