#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:03:18 2020

@author: natnem
"""

b = {}
c = {}
def LCS(X,Y):
    m = len(X)
    n = len(Y)
    for i in range(0,m+1):
        c[i,0] = 0
    for j in range(0,n+1):
        c[0,j] = 0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i,j] = c[i-1,j-1] + 1
                b[i,j] = "NW"
            elif (c[i-1,j] >= c[i,j-1]):
                c[i,j] = c[i-1,j]
                b[i,j] = "N"
            else:
                c[i,j] = c[i,j-1]
                b[i,j] = "W"
    
    return c,b

def PrintLCS(b,X,i,j):
    if i == 0 or j == 0:
        return 0
    elif b[i,j] == "NW":
        PrintLCS(b,X,i-1,j-1)
        print(X[i])
    elif b[i,j] == "N":
        PrintLCS(b,X,i-1,j)
    else:
        PrintLCS(b,X,i,j-1)


X = "ABCBDAB"
Y = "BDCABA"
c,b = LCS(X,Y)
i = len(X)
j = len(Y)
PrintLCS(b,X,i,j)