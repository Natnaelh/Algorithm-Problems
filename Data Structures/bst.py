#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:06:14 2020

@author: natnem
"""
class BstNode(object):    
    def __init__(self, t):
        self.key = t
        self.disconnect()
    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None
    
    

class BST(BstNode):
    def __init__(self):
        self.root = None
    
    def TreeInsert(self, t):
        new = BstNode(t)
        y = None
        x = self.root
        while x is not None:
            y = x
            if t < x.key:
                x = x.left
            else:
                x = x.right
        new.parent = y
        if y == None:
            self.root = new
        elif t < y.key:
            y.left = new
        else:
            y.right = new
	return new
    
    def InorderTreeWalk(self, node):
        if node is not None:
            self.InorderTreeWalk(node.left)
            print(node.key)
            self.InorderTreeWalk(node.right)
    def PreorderTreeWalk(self, node):
        if node is not None:
            print(node.key)
            self.PreorderTreeWalk(node.left)
            self.PreorderTreeWalk(node.right)
            
    def PostorderTreeWalk(self,node):
        if node is not None:
            self.PostorderTreeWalk(node.left)
            self.PostorderTreeWalk(node.right)
            print(node.key)
    
    def TreeSearch(self, k):
        t = self.root
        while t is not None and t.key != k:
            if k < t.key:
                t = t.left
            else:
                t = t.right
#        if t == None:
#            return False
#        else:
#            return True
        return t
    
    def TreeMinimum(self,node):
        t = node
        while t.left is not None:
            t = t.left
        return t
    def TreeMaximum(self,node):
        t = node
        while t.right is not None:
            t = t.right
        return t
    def TreeSuccessor(self, node):
        if node is None:
            return None
        if node.right is not None:
            return self.TreeMinimum(node.right)
        else:
            y = node.parent
            while y is not None and node == y.right:
                node = y
                y = y.parent
            return y.key
    def TreePredecessor(self,node):
        if node is None:
            return None
        if node.left is not None:
            return self.TreeMaximum(node.left)
        else:
            y = node.parent
            while y is not None and node == y.left:
                node = y
                y = y.parent
            return y.key
    
    def Transplant(self, u , v):
        if u.parent ==  None:
            self.root = v
        elif  u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        
        if v is not None:
            v.parent = u.parent
        
    def TreeeDelete(self,node):
        if node.left is None:
            self.Transplant(node,node.right)
        elif node.right is None:
            self.Transplant(node , node.left)
        else:
            y = self.TreeMinimum(node.right)
            if y is not node.right:
                self.Transplant(y, y.right)
                y.right  = node.right
                y.right.parent = y
            self.Transplant(node, y)
            y.left = node.left
            y.left.parent = y
            
            
            
            
            
            
            
            
            
    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])
    
    

mytree = BST()

mytree.TreeInsert(90)
mytree.TreeInsert(100)
mytree.TreeInsert(7)
mytree.TreeInsert(2)
#mytree.TreeInsert(4)
#mytree.TreeInsert(3)
mytree.TreeInsert(120)
mytree.TreeInsert(122)
mytree.TreeInsert(8)
mytree.TreeInsert(95)
mytree.TreeInsert(98)
mytree.TreeInsert(118)
print(mytree)


print(mytree.TreeeDelete(mytree.TreeMaximum(mytree.root)))
print(mytree)
#print(mytree.TreeSuccessor(mytree.root.left))
