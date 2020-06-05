#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:40:21 2020

@author: natnem
"""

def bfs(Adj,source):     #uses Adjacency rep of a graph 
    """assumes Adj as a nested List or dictionary and the indexes(keys) are 
    label of vertex and the sublist in each index contains the lables of 
    other vertexes which are connected to the indexed node"""
    
    
    parent = {source: None}  #parent of starting node is None
    level = {source: 0}      #parent of starting node is 0
    i = 1               # used for assigning the level for each visit
    frontier = [source]     #those in frontier are already visited nodes(previous levels)
    
    while frontier:
        Next = []  #used for  level i(next levels)
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    Next.append(v)
        frontier = Next
        i = i + 1

    #returns the bfs tree of each node visited from a given source 
    return parent

    
def ShortestPath(Adj,source,des):     # shortes path from source to des
    shortest = [des]  #used for finding the shortes path between two given nodes
    while des != source:
        shortest.append(bfs(Adj,source)[des])
        des = bfs(Adj,source)[des]
    shortest.reverse()
    return shortest
    


#adj = {"a":["s","z"], "s":["x","a"],"z":["a"],"x":["s","d","c"],
#       "d":["x","c","f"],"c":["x","d","f","v"],"f":["c","d","v"],
#       "v":["f","c"]}
#source = "z"
#des = "f"
#print(bfs(adj,source))
#print(ShortestPath(adj,source,des))
