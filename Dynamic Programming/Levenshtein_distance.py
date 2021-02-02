#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:59:35 2020

@author: natnem
"""

def LevenshteinDistance(firstString , secondString):
    m = len(firstString)
    n = len(secondString)
    distance = {}
    
    for i in range(m+1):
        distance[i,0] = i
    for j in range(n+1):
        distance[0,j] = j
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if firstString[i]==secondString[j]:
                replaceCost = 0
            else:
                replaceCost = 1
                distance[i,j]=min(replaceCost + distance[i-1,j-1],
                                    distance[i,j-1]+ 1 , distance[i-1,j]+ 1 )
            
        return distance[m+1,n+1]
                
    
    
#    return distance
        
    
    
    
    
   
print(LevenshteinDistance("kitten", "sitting"))

