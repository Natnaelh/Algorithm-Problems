#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:06:53 2020

@author: natnem
"""

class BSTNode(object):
    def __init__(self, parent , k): #creates a node
        self.key = k         #nodes key
        self.parent = parent        #nodes parent
        self.left = None
        self.right = None
    
    def find(self , k):
        if self.key == k :
            return self
        if k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)
    
    def IterativeFind(self, k):
        
        while (self.right is not None or self.left is not None) and (self.key != k):
            if k < self.key:
                self = self.left
            else:
                self = self.right
                
        return self
    
    def findMin(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    def findMax(self):
        current = self
        while current.right is not None:
            current = current.right
        return current
    
    def NextLarger(self):
        if self.right is not None:
            return self.right.findMin()
        
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent
    
    def NextSmaller(self):
        if self.left is not None:
            return self.left.findMax()
        current  = self
        while current.parent is not None and current is current.parent.left:
            current = current.parent
        return current.parent
    
    
    def InorderTreeWalk(self):
        cur = self
        if cur is not None:
            cur.left.InorderTreeWalk()
            print(self.key)
            cur.right.InorderTreeWalk()
            
    def PreorderTreeWalk(self):
        if self is not None:
            print(self.key)
            self.left.PreorderTreeWalk()
            self.right.PreorderTreeWalk()
    def PostOrderTreeWalk(self):
        if self is not None:
            self.left.PostOrderTreeWalk()
            self.right.PostOrderTreeWalk()
            print(self.key)
    
    
            
    
    
    def InsertNode(self, node):
        if node is None:
            return 
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.InsertNode(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.InsertNode(node)
        
        return
            
    
    
    
    
    
    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.right or self.left
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
    
    
        else:
            s = self.NextLarger()
            self.key , s.key  = s.key , self.key
            return s.delete()
        
                
    

    
    

tree = BSTNode(0,5)
tree.InsertNode(BSTNode(1,7))
tree.InsertNode(BSTNode(2,3))
tree.InsertNode(BSTNode(3,12))
tree.InsertNode(BSTNode(4,1))
tree.InsertNode(BSTNode(5,8))
tree.InsertNode(BSTNode(6,10))




    
    
    
    
    
    
    
    
    
#    def recursiveFindMin(self):
#        if self.left is None and self.right is None:
#            return self
#        else:
#            return self.left.recursiveFindMin()
#    
#    def recursiveFindMax(self):
#        if self.left == None and self.right is None:
#            return self
#        else:
#            return self.right.recursiveFindMax()
        
    
    
            
            
        