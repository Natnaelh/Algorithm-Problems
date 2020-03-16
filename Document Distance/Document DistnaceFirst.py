#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:42:39 2019

@author: natnem
"""

import math
D1 = ["the" , "cat" , "was" , "outside"]
D2 = ["the" , "cat" , "is" , "outside"]

def CountFreq(l):
    count = {}
    for word in l:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

#print(CountFreq(D1))
    
def dotProd(l1, l2):
    freqL1 = CountFreq(l1)
    freqL2 = CountFreq(l2)
    
    Prod = 0
    for word in freqL1:
        if word in freqL2:
            Prod += freqL1[word] + freqL2[word]
    return Prod

def arcCos(D1,D2):
    
    thing = dotProd(D1,D2) / math.sqrt((dotProd(D1,D1)*dotProd(D2,D2)))
    return math.acos(thing)

def main():
    print("The First List: \n" , D1)
    print("The Second List: \n" , D2)
    
    print("Distance between them in radian = " ,arcCos(D1 , D2 ))
    
    
main()