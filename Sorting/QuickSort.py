#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:17:46 2020

@author: natnem
"""

import random

def quicksort(A, p , r):
    if p < r:
        q = partition(A, p , r)
        quicksort(A, p , q-1)
        quicksort(A, q+1 , r)
        
def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            print(A)
    t = A[i+1]
    A[i+1] = A[r]
    A[r] = t
    return i+1


def Randomized_QuickSort(A,p,r):
    if p < r:
        q = RandomizedPartition(A,p,r)
        Randomized_QuickSort(A, p , q-1)
        Randomized_QuickSort(A, q+1 , r)
        
            
def RandomizedPartition(A,p,r):
    i  = random.randint(p,r-1)
    temp = A[i]
    A[i] = A[r]
    A[r] = temp
    return partition(A,p,r)
    
        
        
        






A = [0,8,2,4,5,7]
r = len(A)-1
print(Randomized_QuickSort(A, 0 ,r))