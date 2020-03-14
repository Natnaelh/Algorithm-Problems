#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:26:06 2020

@author: natnem
"""
""" IMPLMENTATION OF AN UNSORTED DOUBLY LINKED LIST"""
class Node(object):
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None
    def getPrev(self):
        return self.prev
    def getNext(self):
        return self.next
    def getKey(self):
        return self.key
    def setPrev(self, newPrev):
        self.prev = newPrev
    def setNext(self , newNext):
        self.next = newNext
    def setKey(self, newKey):
        self.key = newKey
        
        
class DoublyLinked(Node):
    def __init__(self):
        self.head = None
#        self.first = None
#        self.Last = None
    def isEmpty(self):
        return self.head == None
    def search(self , k):
        """finds the first element with key k in list L
            by a simple linear search, returning a pointer to this element. 
            If no object with key k appears in the list, then the 
            procedure returns NIL"""
        cur = self.head
        while cur != None and cur.key != k:
            cur = cur.next
        if cur == None:
            raise Exception("Key not Found")
        else:
            return cur
    def insert(self, k):
        """Given an element k whose key attribute has already been set, 
        the NSERT procedure “splices” k onto the front of the linked list"""
        
        newNode = Node(k)
        newNode.setNext(self.head)
        if self.head != None:
            self.head.setPrev(newNode)
        self.head = newNode
#        self.first = newNode
        newNode.setPrev(None)
    def delete(self, x):
        """removes an element given its key x from a linked list"""
        if self.isEmpty():
            raise Exception("List is Empty")
        else:
            cur = self.search(x)
            if cur.prev != None:
                cur.prev.setNext(cur.next)
            else:
                self.head = cur.next
            if cur.next != None:
                cur.next.setPrev(cur.prev)
                
                
            
    
    def __str__(self):
        L = []
        cur = self.head
        while cur != None:
            L.append(cur.key)
            cur = cur.next
        
        return str(L)
        
    
#mydoublelist = DoublyLinked()
#mydoublelist.insert(5)
#mydoublelist.insert(0)
#mydoublelist.insert(3)
#mydoublelist.insert(10)
#mydoublelist.delete(5)
#print(mydoublelist)     
        