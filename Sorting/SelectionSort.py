#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:38:36 2020

@author: natnem
"""

def selectionSort(lst): #order (n square) times , n == len(lst)
    suffix = 0
    while suffix != len(lst): #order n times
        for x in range(suffix , len(lst)): #order n times
            if lst[x] < lst[suffix]:
                print(lst)
                lst[x], lst[suffix] = lst[suffix] , lst[x]
        
        suffix += 1
    return lst
mylist = [2,7,1,2,3,6]
print(selectionSort(mylist))



def Select(L):
    if L == []:
        return []
    i = L.index(min(L))
    
    return [min(L)]+ Select(L[:i] + L[i+1:])

print(Select(mylist))
    








                
            
    
