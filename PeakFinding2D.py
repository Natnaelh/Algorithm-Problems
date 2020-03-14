#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 13:02:14 2019

@author: natnem
"""

def algorithm1(array, startcol, endcol):
    mid = (startcol+endcol)//2
    maxmum = 0
    rowindex = 0
    for i in range(len(array)):
        if array[i][mid] > maxmum:
            maxmum = array[i][mid]
            rowindex = i
    if startcol == endcol:
        #print(array[:len(array)][startcol])
        return array[rowindex][endcol]
    else:
        if array[rowindex][mid-1] > array[rowindex][mid]:
            return algorithm1(array, 0, mid-1)
        elif array[rowindex][mid+1] > array[rowindex][mid]:
            return algorithm1(array, mid+1, endcol)
        else:
          #  print((rowindex,mid))
            return (array[rowindex][mid])
        
    
    
    
    
problemMatrix = [
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 8,  9, 10, 20, 15, 11, 10,  9,  8,  7,  6],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
	[ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
]
print(algorithm1(problemMatrix,0,len(problemMatrix)))
