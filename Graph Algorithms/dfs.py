#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:50:34 2020

@author: natnem
"""



#class graph(object): 
#    def __init__(self):
#        self.adj =  {"a":["s","z"], "s":["x"],"z":["a"],"x":["d","c"],
#         "d":["c","f"],"c":["f","v"],"f":["v"],"v":["g"],"n":["m"]}
#    def itervertices(self):
#        return self.adj.keys()
#    def neighbors(self,v):
#        return self.adj[v]
#
#
#class dfsResult(object):
#    """Object Oriented way"""
#    def __init__(self):
#        self.parent = {}
#        self.order = []
#    
#def dfs(g):
#    results = dfsResult()
#    for vertex in g.itervertices():
#        if vertex not in results.parent:
#            dfsVisit(g,vertex,results)
#    return results.parent
#def dfsVisit(g,v,results,parent =None):
#    results.parent[v] = parent
#    if v in g.adj.keys():
#        for n in g.neighbors(v):
#            if n not in results.parent:
#                dfsVisit(g,n,results,v)
#    results.order.append(v)

#    
#g = graph()
#print(dfs(g))  

  










#def DfsVisit(Adj , s , parent):
#    if s in Adj.keys():
#        for neighbours in Adj[s]:
#            if neighbours not in parent:
#                parent[neighbours] = s
#                DfsVisit( Adj , neighbours, parent)
#    return parent
#def dfs(V, Adj):
#    parent = {}
#    for vertex in V:
#        if vertex not in parent:
#            parent[vertex] = None
#            DfsVisit( Adj, vertex, parent)
#    return parent
#
#Adj = {"a":["s","z"], "s":["x"],"z":["a"],"x":["d","c"],
#       "d":["c","f"],"c":["f","v"],"f":["v"],
#       "v":["g"],
#       "n":["m"]} 
#V = [keys for keys in Adj.keys()]
#parent =  {"a": None}
#print(dfs(V,Adj))
















parent = {}
def dfsvisit(adj, s):
    if s in adj.keys():
        for v in adj[s]:
            if v not in parent: 
                parent[v] = s
                dfsvisit(adj,v)

def dfs(adj):
    order = []
    for v in adj.keys():
        if v not in parent:
            parent[v] = None
            dfsvisit(adj,v)
        order.append(v)
    return parent




Adj = {"a":["s","z"], "s":["x"],"z":["a"],"x":["d","c"],
       "d":["c","f"],"c":["f","v"],"f":["v"],
       "v":["g"],
       "n":["m"]}
print(dfs(Adj))