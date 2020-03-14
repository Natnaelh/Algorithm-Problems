#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:36:50 2020

@author: natnem
"""
d = [1,2,3,4,5]
n = 14
parent = []
def coinchange(l,n):
    if n<0:
        return 0
    sh = float('inf')
    parent.append(float('inf'))
    for i in l:
        x = 1+coinchange(l,n-i)
        sh = min(sh,x)
        if sh == x and x < parent[len(parent)-1]:
            parent.pop()
            parent.append(i)
    print(parent)
    return sh
print(coinchange(d,n))
