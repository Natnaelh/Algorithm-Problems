#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:31:37 2020

@author: natnem
"""
import math
def countingSort(array, exp):
    n = len(array)
    out = [0]*n
    count = [0]*10
    for i in range(n):
        index = (array[i]//exp) % 10
        count[index] += 1
    for i in range(1,10):
        count[i]  += count[i-1]
    for x in range(n-1,-1,-1):
        index = (array[x]//exp)%10
        out[count[index]-1] = array[x]
        count[index] -= 1
    return out

def RadixSort(A,base):
    d = math.ceil(math.log(max(A),base))
#    print(d)
    for i in range(d):
        A = countingSort(A,10**i)
    return A
        
        
        
        
mylist = [329,
          457,
          657,
          839,
          436,
          720,
          355]
print(RadixSort(mylist,10))   