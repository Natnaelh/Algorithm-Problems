#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:56:51 2020

@author: natnem
"""

class RollingHash(object):
    def __init__(self,string):
        self.Base = 100
        self.p = 997
        self.stingLength = len(string)-1
        
        # calculate the hash value of the string typed
        power = self.stingLength
        hashS = 0
        for x in string:
            hashS += ord(x) * (self.Base ** power)
            power -= 1
        self.hashValue = hashS % self.p
        
    def hashed(self):
        return self.hashValue
    def slide(self, prev, nex):
        self.hashValue -=  (ord(prev)*(self.Base**self.stingLength)) % self.p
        self.hashValue = ((self.hashValue*self.Base) + ord(nex)) % self.p
        return self.hashValue
#    def append(self,item):
#        self.hashValue = ((self.hashValue*self.Base)+ ord(item)) % self.p
#    def skip(self,prev):
#        self.hashValue -=  (ord(prev)*(self.Base**self.stingLength)) % self.p

def KarpRabin(string, longtext):
    rs = RollingHash(string)
#   print(len(longtext))
    rt = RollingHash(longtext[:len(string)])
    if rs.hashed() == rt.hashed():
        if string == longtext[0:len(string)]:
            print("Match Found")
    collisions = 0
    for i in range(len(string),len(longtext)):
        rt.slide(longtext[i-len(string)] , longtext[i])
#        rt.skip(longtext[i-len(string)])
#        rt.append(longtext[i])
        if rt.hashed() == rs.hashed():
#            print(rt.hashed() , rs.hashed(),longtext[i-len(string)+1:i+1],i)
            if string == longtext[i-len(string)+1:i+1]:
                print("Found Match","string: ",longtext[i-len(string)+1:i+1])
            collisions += 1
    print("Collisions: ",collisions)
        
string = "lines"
wordListFileName = "KarpRabinTest.txt"
inFile = open(wordListFileName,"r")
line = inFile.readline()

        
KarpRabin(string,line)
    
    
        
    
    

        
        
        