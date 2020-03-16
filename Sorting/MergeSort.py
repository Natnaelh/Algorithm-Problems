#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:35:36 2020

@author: natnem
"""

def Merge(left , right):
    result = []
    i,j = 0 , 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    print("Merge: " + str(left) + " and " + str(right))
    return result

#left = [12,15,18,19,20,23]
#right = [2,3,4,6,8,7,9,10,12]
#print(Merge(left , right))
    
def MergeSort(lst):
    print("Merge sort: " + str(lst))
    if len(lst) < 2:
        return lst[:]
    else:
        mid = len(lst)//2
        left = MergeSort(lst[:mid])
        right = MergeSort(lst[mid:])
        
    return Merge(left , right)


mylist = [1,3,5,7,2,6,25,18,13]
print(MergeSort(mylist))



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        