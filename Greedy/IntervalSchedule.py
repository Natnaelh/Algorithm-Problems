#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:36:05 2020

@author: natnem
"""

#refer to CLRS 3rd ed, chapter 16 for detail 
def ActivitySelectorRecursive(s,f,k,n):  #recursive approach , greedy 
    m = k + 1
    while m <= n and s[m] < f[k]:  #selects the next optimal activity 
        m = m + 1
    if m <= n:
#        print(m)  #prints the optimal activity number selected
        return {m}.union(ActivitySelectorRecursive(s,f,m,n))  
    else:
        return {0}
    
s = [0,1,3,0,5,3,5,6,8,8,2,12]   #start time of each activity
f = [0,4,5,6,7,9,9,10,11,12,14,16]  #finish times of each activity, assumes they are monotomically increasing order
n = len(s) - 1  #total activities
k = 0  #assume a fictious activity 0 finishes first with f[0] = 0
#print(ActivitySelectorRecursive(s,f,k,n))




def ActivitySelectorIterative(s,f):  #greedy approach
    n = len(s)
    k = 0
    optimalactivities = []
    for i in range(1,n):
        if s[i] >= f[k]:
            k = i
            optimalactivities.append(k)
            #print(k)  #prints the optimal activity number selected
    
    return optimalactivities
    
print(ActivitySelectorIterative(s,f))
            
