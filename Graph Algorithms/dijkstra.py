#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:08:03 2020

@author: natnem
"""


class PriorityQueue(object):
    def __init__(self):
        self.Heap = {}
    
    def insert(self, Label , key):
        self.Heap[Label] = key
    
    def extractMin(self):
        minlabel = None
        for label in self.Heap:
            if minlabel is None or self.Heap[label] < self.Heap[minlabel]:
                minlabel = label
        del self.Heap[minlabel]
        return minlabel
    def decreaseKey(self, Label , key):
        if key < self.Heap[Label]:
            self.Heap[Label] = key
#            print(self.displ())
    def displ(self):
        return self.Heap
    
def Dijkstra(G,s):
    d = {}
    parent = {}
    for v in G:
        d[v] = float("inf")
        parent[v] = None
    d[s] = 0
   
    Q = PriorityQueue()
    for v in G:
        Q.insert(v,d[v])
    while Q.Heap:
        u = Q.extractMin()
        for v in G[u]:
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v] = u
                Q.decreaseKey(v,d[v])
#                print(parent)
    return parent , d


G= {"s":{"t":10,"y":5},
    "t":{"x":1,"y":2},
    "x":{"z":4},
    "y":{"t":3,"z":2,"x":9},
    "z":{"x":6,"s":7}}
print(Dijkstra(G,"s"))


    
