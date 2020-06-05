#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:07:28 2020

@author: natnem
"""
def bellmanford(G,s):
    d = {}
    parent = {}
    for v in G:
        d[v] = float("inf")
        parent[v] = None
    d[s] = 0
    for i in range(len(G.keys())-1):
        for u in G:
            for v in G[u]:
                if d[v] > d[u] + G[u][v]:
                    d[v] = d[u] + G[u][v]
                    parent[v] = u
    for u in G:
        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                return False
    
    return parent,d

# G is a Directed Weighted graph with negative weights and 
#there are no negative weight cycles
G= {"s":{"t":6,"y":7},
    "t":{"x":5,"y":8,"z":-4},
    "x":{"t":-2},
    "y":{"x":-3,"z":9},
    "z":{"s":2,"x":7,"s":2}}
source = "t" 
print(bellmanford(G,source))
# H is a graph with negative weight cycles. Bellman ford returns False
H= {"s":{"t":6,"y":7},
    "t":{"x":-5,"y":8,"z":-4},
    "x":{"t":-2},
    "y":{"x":-3,"z":9},
    "z":{"s":2,"x":7,"s":2}}
print(bellmanford(H,source))      
        
        
        