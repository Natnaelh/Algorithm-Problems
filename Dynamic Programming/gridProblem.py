#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:54:58 2020

@author: natnem
"""

#def gridDp(n,m):
#    d = {}
#    for i in range(1,n+1):
#        for j in range(1,m+1):
#            if i == 1 and  j == 1:
#                d[(i,j)] = 0
#            else:
#                if i == 1:
#                    d[(i,j)] = d[(i,j-1)] + 1
#                elif j == 1:
#                    d[(i,j)] = d[(i-1,j)] + 1
#                else:
#                    d[(i,j)] = min(d[(i-1,j)] + 1 , d[(i,j-1)] + 1)
#                
#    return d
#
#n = 6
#m = 4
#print(gridDp(n,m))