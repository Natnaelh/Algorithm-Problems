#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:06:44 2020

@author: natnem
"""
import bst

def height(node):
    if node == None:
        return -1
    else:
        return node.height
    
def updateheight(node):
    node.height= max((height(node.left)),(height(node.right)) + 1)

class AVL(bst.BST):
    
    def leftRotate(self,x):
        y = x.right
        y.parent = x.parent
        if y.parent == None:
            self.root = y
        else:
            if x is y.parent.left:
                y.parent.left = y
            elif x is y.parent.right:
                y.parent.right = y
        
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        updateheight(x)
        updateheight(y)
    
    def rightRotate(self,x):
        y = x.left
        y.parent = x.parent
        if y.parent == None:
            self.root = y
        else:
            if x is y.parent.left:
                y.parent.left = y
            elif x is y.parent.right:
                y.parent.right = y
            
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        
        y.right = x
        x.parent = y
        updateheight(x)
        updateheight(y)
    
    def Insert(self,t):
        node = bst.BST.TreeInsert(t)
        self.rebalance(node)
    def rebalance(self,node):
        while node is not None:
            updateheight(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.rightRotate(node)
                else:
                    self.leftRotate(node.left)
                    self.rightRotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.leftRotate(node)
                else:
                    self.rightRotate(node.left)
                    self.leftRotate(node)
        node = node.parent
        
