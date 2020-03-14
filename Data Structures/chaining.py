#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:25:05 2020

@author: natnem
"""

import DoublyLinkedList as link
import random

class hashchaining(object):
    """Uses universal hashing method, assumes ASCII base(256),
        some random constants are defined in the constructor."""
    def __init__(self):
        self.base = 256
        self.m = 8
        self.p = 11
        self.a = random.randint(0,self.p - 1)
        self.b = random.randint(0,self.p - 1)
        self.table = self.BuildTable()
    
    
    def BuildTable(self):
        return [None]*self.m
    def Hashfunction(self, key):
        hashed = key%self.m
#        hashed = ((((self.a * key)) + self.b) % self.p) % self.m
        return hashed
    def KeysToNumbers(self, key):
        result = 0
        if type(key)==int:
            return key
        else:
            power = len(key) -1 
            for x in key:
                result += ord(x) * (self.base ** power)
                power -= 1
        return result
    
    def Insert(self, key):
        keyInt = self.KeysToNumbers(key)
        hashIndex = self.Hashfunction(keyInt)
        
        if self.table[hashIndex] == None:
            linkedlist = link.DoublyLinked()
            linkedlist.insert(key)
            self.table[hashIndex] = linkedlist
        else:
            self.table[hashIndex].insert(key)
    
    def Search(self , key):
        keyInt = self.KeysToNumbers(key)
        hashIndex = self.Hashfunction(keyInt)
        
        if self.table[hashIndex] == None:
            return "key Not Found"
        else:
            return self.table[hashIndex].search(key)
        
    
    def Delete(self, key):
        keyInt = self.KeysToNumbers(key)
        hashIndex = self.Hashfunction(keyInt)
        
        if self.table[hashIndex] == None:
            return "Key Not Found"
        else:
           return self.table[hashIndex].delete(key)
       


myhash = hashchaining()
myhash.Insert("AA")
myhash.Insert("hashed")  
myhash.Insert("CFD")
myhash.Insert("D") 
myhash.Insert("Hash here")
myhash.Insert("Natty") 
#print(myhash.Search("fikadu1"))
print(myhash.KeysToNumbers("A"))
for i in range(8):
    print(myhash.table[i].__str__())   
        
            
        
            
    
                
        
    
        
