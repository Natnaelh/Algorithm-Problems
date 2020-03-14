#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:36:41 2020

@author: natnem
"""

class BSTNode(object):
    def __init__(self, parent , key):
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None
    def getKey(self):
        return self.key
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.right
    def setKey(self, key):
        self.key = key
    def setLeft(self,newLeft):
        self.left = newLeft
    def setRight(self, newRight):
        self.right = newRight
    def recursiveFind(self, key):
        
        if self.key == key:
            return self
        elif self.key < key:
            if self.left == None:
                return None
            else:
                return self.left.recursiveFind(key)
        else:
            if self.right == None:
                return None
            else:
                return self.right.recursiveFind(key)
            
    def iterativeSearch(self, key):
        cur = self
        while cur != None and cur.key != key:
            if cur.key < key:
                cur = cur.left
            else:
                cur = cur.right
        return cur
    
    def findmin(self):
        cur = self
        while cur != None:
            cur = cur.left
        return cur
    def findmax(self):
        cur = self
        while cur != None:
            cur = cur.right
        return cur
    def successor(self):
        if self.right != None:
            return self.right.findmin()
        else:
            cur = self
            while cur.parent != None and cur is cur.parent.right:
                cur = cur.parent
            return cur.parent
    def predeccesor(self):
        if self.left != None:
            return self.left.findmax()
        else:
            cur = self
            while cur != None and cur is cur.parent.left:
                cur = cur.parent
            return cur.parent
    def insert(self, newNode):
        
        if newNode == None:
            return 
        if self.key < newNode.key:
            if self.left is None:
                self.left = newNode
            else:
                self.left.insert(newNode)
        else:
            if self.right is None:
                self.right = newNode
            else:
                self.right.insert(newNode)
    
    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.right or self.left
                if self.parent.right  is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.successor()
            self.key , s.key = s.key , self.key
            return s.delete()
    
                    
#Below are Tree Traversals
    
    def inorder(self):
        if self is not None:
            self.left.inorder()
            print(self.key)
            self.right.indorder()
        else:
            return
    def preorder(self):
        if self is not None:
            print(self.key)
            self.left.preorder()
            self.right.preorder()
    def postorder(self):
        if self is not None:
            self.left.postorder()
            self.right.postorder()
            print(self.key)
            

            

        