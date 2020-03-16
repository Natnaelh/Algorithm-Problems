#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:10:28 2020

@author: natnem
"""
## FUNCTION RETURNS INDEX OF THE ITEM IF FOUND, ELSE RETURNS -1
def BinarySearch1(List , item): #with recursion
    if len(List) == 0:
        return -1
    mid = len(List)//2
    if List[mid]==item:
        return mid
    if List[mid] > item:
        return BinarySearch1(List[:mid], item)
    res =  BinarySearch1(List[mid+1:], item)
    if res == -1:
        return -1
    return res + mid + 1

mylist = [1,2,4,8,10,12,25,30]
#print(BinarySearch1(mylist, 25))



def BinarySearch2(List, item): #with out Recursion
    left = 0
    right = len(List)
    
    while right - left > 0:
        m = (right+left)//2
        if List[m]==item:
            return m
        if List[m] > item:
            right = m
        else:
            left = m + 1
#print(BinarySearch2(mylist,30))
            
    
    