#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:47:48 2020

@author: natnem
"""

### The algorithms returns True if item is in lst, else False
def BisectionSearch1(lst , item): #with list slicing
    if lst == []:
        return False
    elif len(lst) == 1:
        return lst[0] == item
    else:
        half = len(lst)//2
        
        if lst[half] > item:
            return BisectionSearch1(lst[:half] , item)
        else:
            return BisectionSearch1(lst[half:] , item)
        

mylist = [x for x in range(100000)]
print(BisectionSearch1(mylist , 2))



def BisectionSearch2(lst , item , low , high): #with pointers 
    if lst == []:
        return False
    elif len(lst) == 1:
        return lst[0] == item
    else:
        mid = (low + high)//2
        
        if lst[mid] == item:
            return True
        elif lst[mid] < item:
            if mid == high:
                return False
            else:
                 return BisectionSearch2(lst , item , mid+1 , high)
                
        else:
           
            return BisectionSearch2(lst , item , low , mid-1)
    
print(BisectionSearch2(mylist , 2 , 0 , len(mylist)))










