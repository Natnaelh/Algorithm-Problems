#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:42:48 2019

@author: natnem
"""

def InsertionSort(lst):
    for j in range(1,len(lst)):
        key = lst[j]
        i = j - 1
        while i >=0 and key < lst[i]:
            lst[i+1] = lst[i]
            i -= 1
        lst[i+1] = key
    return lst

mylist = [10,2,5,8,46,2]
print(InsertionSort(mylist))           
            
            
 




       

















