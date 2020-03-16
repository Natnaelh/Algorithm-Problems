#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:43:46 2020

@author: natnem
"""

def linearSearch(lst , e):  #returns the index of item if it exists , if not None
    for i in range(len(lst)):
        if lst[i]==e:
            return i
    return None

mylist = [1,5,87,5,13,1,8,4,6,7,4,5,8,5,4,7,79,6,78]
print(linearSearch(mylist,1))