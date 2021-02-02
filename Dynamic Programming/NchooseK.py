#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:57:50 2020

@author: natnem
"""

memo = {}
def N_choose_K(n , k):
    if (n,k) in memo:
        return memo[(n,k)]
    elif (k == 0 or n <= k):
        return 1
    else:
        value =  N_choose_K(n-1,k) +  N_choose_K(n-1,k-1)
        memo[(n,k)] = value
        return value
    

print(N_choose_K(4,2))