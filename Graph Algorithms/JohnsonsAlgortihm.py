#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:09:17 2020

@author: natnem
"""


class Graph(object):
    def __init__(self):
        self.vertices = {}
    
    def addVertex(self, key):
        vertex = Vertex(key)
        self.vertices[key] = vertex
        
    def getVertex(self,key):
        return self.vertices[key]
    
    def __contains__(self,key):
        return key in self.vertices
    
    def addEdge(self,sourceKey,destKey,weight = 1):
        self.vertices[sourceKey].addNeighbour(self.vertices[destKey],weight)
    def EdgeExists(self,sourceKey , destKey):
        return self.vertices[sourceKey].pointsTo(self.vertices[destKey])
    
    def __len__(self):
        return len(self.vertices)
    def __iter__(self):
        return iter(self.vertices.values())
    
class Vertex:
    def __init__(self,key):
        self.key = key
        self.point_to = {}
    
    def getKey(self):
        return self.key
    def addNeighbour(self, dest,weight):
        self.point_to[dest] = weight
    def getNeighbours(self):
        return self.point_to.keys()
    def getWeight(self,dest):
        return self.point_to[dest]
    def setWeight(self, dest,weight):
        self.point_to[dest] = weight
    def pointsTo(self, dest):
        return dest in self.point_to
    
        


def BellmanFord(g , s):
    d = dict.fromkeys(g , float('inf'))
    d[s] = 0
    
    for i in range(len(g)-1):
        for u in g:
            for v in u.getNeighbours():
                d[v] = min(d[v] , d[u] + u.getWeight(v))
    return d


def Dijkstra(g, s):
    d = dict.fromkeys(g , float('inf'))
    d[s] = 0
    unvisited = set(g)
    
    while (unvisited != set()):
        u  = min(unvisited, key = lambda v: d[v])
        unvisited.remove(u)
        
        for v in u.getNeighbours():
            if v in unvisited:
                new_d_value = d[u] + u.getWeight(v)
                if  d[v] > new_d_value:
                    d[v] = new_d_value
    return d


def Johnson(graph):
    graph.addVertex("s")
    for v in graph:
        graph.addEdge("s",v.getKey(),0)
        
    BFordDistanceFrom_s = BellmanFord(graph , graph.getVertex('s'))
    
    for u in graph:
        for v in u.getNeighbours():
            w = u.getWeight(v)
            u.setWeight(v , w + BFordDistanceFrom_s[u] - BFordDistanceFrom_s[v])
    
    del graph.vertices["s"]
    
    distance = {}
    for u in graph:
        distance[u] = Dijkstra(graph, u)
    
    for u in graph:
        for v in graph:
            distance[u][v] += BFordDistanceFrom_s[v] - BFordDistanceFrom_s[u]
    
    return distance

        
G = Graph()
G.addVertex("a")
G.addVertex("b")
G.addVertex("c")
G.addVertex("d")
G.addVertex("e")
G.addEdge('a','b',3)
G.addEdge('a','e',-4)
G.addEdge('a','c',8)
G.addEdge('b','d',1)
G.addEdge('b','e',7)
G.addEdge('c','b',4)
G.addEdge('d','c',-5)
G.addEdge('d','a',2)
G.addEdge('e','d',6)

Paths = (Johnson(G))
for u in G:
    print(Paths[u])