#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:40:11 2020

@author: natnem
"""

class OpenAddressing(object):
    def __init__(self):
        self.m = 29         #good choice should a prime number
        self.mprime = 28    #good choice should be a number less m by 1
        self.base = 256     #ASCII base
        self.Table = self.BuildTable() #Builds a hash table with size m
    def KeysToNaturalNumber(self , key):
        """Maps given strings to its correspoding integer(pre hash)"""
        h = 0
        if type(key) == int:
            return key
        else:
            for k in key:
                power = len(key)-1
                h += ord(k) * (self.base ** power)
                power -= 1
#            print(h)
            return h
    def BuildTable(self):       #Builds a hash table with size m
        return [None]*self.m    
    def FirstHash(self,key):
        hashvalue = key % self.m
        return hashvalue
    def SecondHash(self,key):
        hashvalue = 1 + (key % self.mprime)
        return hashvalue
    def DoubleHashing(self, key, i):
        hashed = (self.FirstHash(key) + (i * self.SecondHash(key))) % self.m
        return hashed
    
    def HashInsert(self, value):
        i = 0
        key = self.KeysToNaturalNumber(value)
        while i <= self.m:
            j = self.DoubleHashing(key, i)
            if self.Table[j] == None or self.Table[j] == "Deleted" :
                self.Table[j] = value
                return (j,self.Table[j])
            else:
                i += 1
        return "Hash Table is Full"
   
    def HashSearch(self,value):
        i = 0
        j = 0
        key = self.KeysToNaturalNumber(value)
        while i <= self.m or self.Table[j] is None or self.Table[j] != "Deleted":
            j = self.DoubleHashing(key , i)
            if self.Table[j] == value:
                return (j,self.Table[j])
            else:
                i += 1
        return None
    
    def HashDelete(self,value):
        i = 0
        key = self.KeysToNaturalNumber(value)
        while i <= self.m:
            j = self.DoubleHashing(key,i)
            if self.Table[j] == value:
                self.Table[j] = "Deleted"
                return value + " deleted"
            else:
                i = i+1
        return "Item not Found"
               

 
            
       
#openadd = OpenAddressing()
#print(openadd.HashInsert("Abebe"))
#print(openadd.HashInsert("Belay"))
#print(openadd.HashInsert("Abeb"))
#print(openadd.HashInsert("Bela"))
#print(openadd.HashInsert("Abeba"))
#print(openadd.HashInsert("Belat"))
#print(openadd.HashInsert("Abea"))
#print(openadd.HashInsert("Belt"))
#print(openadd.Table)
#print(openadd.HashDelete("Abe"))
#print(openadd.Table)
#print(openadd.HashSearch("Abebe"))
#print(openadd.HashInsert("Abe"))
#print(openadd.Table)
#print(openadd.HashInsert("Abebe"))
#print(openadd.HashInsert("Belay"))
#print(openadd.HashInsert("Abeb"))
#print(openadd.HashInsert("Bela"))
#print(openadd.HashInsert("Abeba"))
#print(openadd.HashInsert("Belat"))
#print(openadd.HashInsert("Abea"))
#print(openadd.HashInsert("Belt"))
    