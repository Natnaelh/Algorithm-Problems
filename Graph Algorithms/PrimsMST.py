#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:54:46 2020

@author: natnem
"""

class PriorityQueque(object):
    def __init__(self):
        self.heap = {}
    
    def Insert(self,Label, key):
        self.heap[Label] = key
    
    def ExtractMin(self):
        minLabel = None
        for label in self.heap:
            if minLabel is None or self.heap[label] < self.heap[minLabel]:
                minLabel = label
        del self.heap[minLabel]
        return minLabel
    
    def DecreaseKey(self, label, newKey):
        if newKey < self.heap[label]:
            self.heap[label] = newKey
    def display(self):
        print(self.heap)
    


def Prims(graph,MstRoot):
    parent = {}
    d = {}
    for v in graph:
        d[v] = float("inf")
        parent[v] = None
    d[MstRoot] = 0
    Q = PriorityQueque()
    for v in graph:
        Q.Insert(v,d[v])
    while(Q.heap):
        u = Q.ExtractMin()
        for v in graph[u]:
            if v in Q.heap and graph[u][v] < Q.heap[v]:
                parent[v] = u
                d[v] = graph[u][v]
                Q.DecreaseKey(v,graph[u][v])
    return d

UndirectedAdj = {"a":{"b":4,"h":8},"b":{"a":4,"h":11,"c":8},
                 "c":{"b":8,"d":7,"i":2,"f":4},"d":{"c":7,"f":14,"e":9},
                 "e":{"d":9,"f":10},"f":{"e":10,"d":14,"c":4,"g":2},
                 "g":{"f":2,"h":1,"i":6},"h":{"g":1,"i":7,"b":11,"a":4},
                 "i":{"g":6,"c":2,"h":7}}


source  =   "a"
print(Prims(UndirectedAdj,source))
    