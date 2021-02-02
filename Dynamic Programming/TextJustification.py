#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 23:41:59 2020

@author: natnem
"""

mytext = 'helo there this'
words  = mytext.split(" ")
n = len(words)

memo = {}
parent = {}

def textjust(i):
    if i >= n:
        return 0
    elif i in memo:
        return memo[i]
    else:
        bad = float("inf")
        for j in range(i+1, n+1):
            newval = textjust(j) + badness(i,j)
            if newval < bad:
                bad = newval
                parent[i] = j
        print(j,memo)
        memo[i] = bad
        return bad
    
def badness(i , j):
    pagewidth = 10
    totalwidth = 0
    for chars in words[i:j+1]:
        totalwidth += len(chars)
    totalwidth += (j-i)
    print("tot = "+ str(totalwidth))
    
    if totalwidth > pagewidth:
        return float('inf')
    else:
        return pow(pagewidth - totalwidth,3)
    

print(textjust(0))

        

