#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:01:45 2020

@author: natnem
"""

class Graph(object): 
    def __init__(self,adj):
        self.adj = adj
    def itervertices(self):
        return self.adj.keys()
    def neighbors(self,v):
        return self.adj[v]


class dfsResult(object):
    """Object Oriented way"""
    def __init__(self):
        self.parent = {}
        self.order = []
    
def dfs(g):
    results = dfsResult()
    for vertex in g.itervertices():
        if vertex not in results.parent:
            dfsVisit(g,vertex,results)
    return results
def dfsVisit(g,v,results,parent =None):
    results.parent[v] = parent
    if v in g.adj.keys():
        for n in g.neighbors(v):
            if n not in results.parent:
                dfsVisit(g,n,results,v)
    results.order.append(v)
    
def TopologicalSort(adj):
    Topsort = dfs(adj)
    Topsort = Topsort.order
    Topsort.reverse()
    return Topsort

#G = {"shorts":["pants","shoes"],"pants":["belt","shoes"],
#         "belt":["jacket"],"shirt":["tie","belt"],
#         "socks":["shoes"],"watch":[],"tie":["jacket"]}
#g = Graph(G)
#print(TopologicalSort(g))