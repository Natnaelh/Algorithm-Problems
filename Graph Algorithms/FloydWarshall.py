#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 15:21:41 2020

@author: natnem
"""

def FloydWarshall(dist): #assumes vertices are numbered from 0 to n
    n = len(G)
    for k in range(1,n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
              
#        print(dist)
    return dist

inf = float('inf')
G = [[0,3,8,inf,-4],  #intial matrix representation of directed weighted graph
     [inf,0,inf,1,7],
     [inf,4,0,inf,inf],
     [2,inf,-5,0,inf], 
     [inf, inf, inf, 6, 0]]


#def TransitiveClosure(G): # 0 if path do not exist, 1 if path exists
#    n = len(G)
#    P = FloydWarshall(G)
#    for i in range(n):
#        for j in range(n):
#            if P[i][j] == float('inf'):
#                P[i][j] = 0
#            else:
#                P[i][j] = 1
#    return P

print(FloydWarshall(G))
#print()
#print(TransitiveClosure(G))