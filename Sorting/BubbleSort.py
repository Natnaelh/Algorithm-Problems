#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:38:36 2020

@author: natnem
"""

def bubbleSort(lst):  #Order of n square where n == len(lst)
    swap = False
    
    while not swap:  #O(len(lst))
        swap = True
        print("Bubble Sort: " , lst)
        for i in range(1,len(lst)):     #O(len(lst))
            if lst[i] < lst[i-1]:
                swap = False
                temp = lst[i]
                lst[i] = lst[i-1]
                lst[i-1] = temp
                
    return lst
        
mylist = [x for x in range(10,-1,-2)]
print(bubbleSort(mylist))

def bubble(A):
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            if A[j] < A[j-1]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
              
    return A


print(bubble(mylist))