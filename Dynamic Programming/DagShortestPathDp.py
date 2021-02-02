#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:05:41 2020

@author: natnem
"""

class Graph(object):
    def __init__(self,G):
        self.graph = G
    def itervertices(self):
        return self.graph.keys()
    def Inverse_neighbors(self,u):
        neighbors = []
        for x in self.itervertices():
            for y in self.graph[x]:
                if y == u:
                    neighbors.append(x)
        return neighbors
                    
    def weight(self,u,v):
        return self.graph[u][v]

class ShortestPathResult(object):
    def __init__(self):
        self.d = {}
        self.parent = {}
def shortest_path(graph,s):
    result  = ShortestPathResult()
    result.d[s] = 0
    result.parent[s] = None
    
    for v in graph.itervertices():
        sp_dp(graph,v,result)
    return result

def sp_dp(graph, v , result):
    
    if v in result.d:
        return result.d[v]
    else:
        result.d[v] = float("inf")
        result.parent[v] = None
        
        for u in graph.Inverse_neighbors(v):
            newdistance = sp_dp(graph,u,result) + graph.weight(u,v)
            if newdistance < result.d[v]:
                result.d[v] = newdistance
                result.parent[v] = u
        return result.d[v]
            
    
    



G= {"s":{"t":10,"y":5},
    "t":{"x":1,"y":2},
    "x":{"z":4},
    "y":{"t":3,"z":2,"x":9},
    "z":{"x":6,"s":7}}            
mygraph = Graph(G)
s = "s"
print(shortest_path(mygraph,s).d)