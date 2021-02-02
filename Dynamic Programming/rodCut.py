#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:51:38 2020

@author: natnem
"""


def rodCut(p,n):
    if n == 0:
        return 0
    q = float("-inf")
    for i in range(1,n+1):
        q = max(q , p[i] + rodCut(p,n-i))
    
    return q

#print(rodCut([10,30],1))


memo = {}
def rodCutDP(p , n):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    else:
        q = float("-inf")
        for i in range(1,n+1):
            q = max(q , p[i] + rodCutDP(p , n -i ))
        memo[i] = q
        return q
    
#print(rodCutDP([0,1,5,8,9,10,17,17,20,24,30],10),memo.values())


def rodCutBottomUp(p , n):
    r = [0]
    s = []
    for j in range(1,n+1):
        q = float("-inf")
        for i in range(1,j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s.append(i)
        r.append(q)
    return r , s

n = 10
r , s = rodCutBottomUp([0,1,5,8,9,10,17,17,20,24,30],n)
  
    
    
    

    
    





