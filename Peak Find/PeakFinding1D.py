#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:02:10 2019

@author: natnem
"""
import time 
#   list contains a list of strictly increasing values, so all
#   functions must return the last item, ,which is a worst case cenario

def Algorithm1(lst):  #O(n), where n == len(lst) complexity
    for x in range(1,len(lst)-2):
        if lst[x-1] <= lst[x] and lst[x+1] <= lst[x]:
            return lst[x]
    if lst[-1] >= lst[-2]:
        return lst[-1]
    
    return None

##mylist = [4,45,6,4,1,7,2,8,8,22,47,13,56,89,10,17,45,78,2,19,45,56,2,7,8,4,1,2,87,54,1,6,7,9]
mylist  = [x for x in range(9999999)]
t0 = time.time()
print(Algorithm1(mylist))
t = time.time()
print("Algorithm 1: " , t-t0)

#
#            




# takes logn
def Algorithm2(lst, low, high ):
    if low == high:
        return lst[high]
    mid = (low + high)//2
    if lst[mid-1] > lst[mid]:
        return Algorithm2(lst , low , mid-1)
    elif lst[mid+1] > lst[mid]:
        return Algorithm2(lst , mid+1 , high)
    else:
        return lst[mid]
t0 = time.time()
print(Algorithm2(mylist,0,len(mylist)-1))
t = time.time()
print("Algorithm 2: " , t - t0)
#
#
#
#
#
#



# Takes nlogn
def Algorithm3(lst):
    if len(lst)== 2:
        if lst[0] > lst[1]:
            return lst[0]
        else:
            return lst[1]
    elif len(lst) < 2:
        return lst[0]
    m = len(lst)//2
    if lst[m-1] > lst[m]:
        return Algorithm3(lst[:m])
    elif lst[m+1] > lst[m]:
        return Algorithm3(lst[m+1:])
    else:
        return lst[m]
t0 = time.time()   
print(Algorithm3(mylist))
t = time.time()
print("Algorithm 3: " , t - t0)
