#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:30:49 2020

@author: natnem
"""

def Max_Heapify(A, i): 
    l = Left(i)
    r = Right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
#        print(A , "Largest: l ",l)
    else:
        largest = i
#        print(A, "Largest: i ",i)
    if r < len(A) and A[r] > A[largest]:
        largest = r
#        print(A , "Largest: r ",r)
    if  i != largest:
        A[i] , A[largest] = A[largest] , A[i]
        Max_Heapify(A,largest)
    return A

def Build_Max_Heap(Unsorted_List):
        n = (len(Unsorted_List)//2)-1
        for i in range(n,-1,-1):
            newList = Max_Heapify(Unsorted_List, i)
        return newList

#print(Build_Max_Heap(List))

def HeapSort(A):
    A = Build_Max_Heap(A)
    mysortedList = []
    for i in range(len(A)-1,-1,-1):
        A[0] , A[i] = A[i] , A[0]
        n = A.pop()
        mysortedList.append(n)
        Max_Heapify(A,0)
    return mysortedList
#helper Functions
def Left(i):
    return (2*i) + 1
def Right(i):
    return (2*i) + 2
def Parent(i):
    return i//2
        






### BELOW IS AN IMPLMENTATION OF A PRIORITY QUEUE
def Max(A):  #RETURNS THE MAXIMUM PRIORITY
    return A[0]

def Extract_Max(A): #RETURNS THE MAX ITEM AND DELETES IT FROM THE HEAP
    if len(A) < 1:
        return "Error: Underflow"
    Max = A[0]
    A.pop()
    A = Max_Heapify(A,0)
    return Max

def HeapIncreaseKey(A,i,key):
    if key < A[i]:
        return "Error: New key smaller than current key"
    A[i] = key
    while i > 0 and A[Parent(i)] < A[i]:
        A[i] , A[Parent(i)] = A[Parent(i)] , A[i]
        i = Parent(i)
        
    return A
def MaxHeapInsert(Heap,new):
    Heap.append(-10^15)
    i = len(Heap)-1
    Heap =  HeapIncreaseKey(Heap,i,new)

    return Heap

List = [4,57,2,1,0,43,51,79,13,446,98,59,9,5]    
myheap = (HeapSort(List))
print(myheap)
print(HeapIncreaseKey(myheap,5,100))  
print(MaxHeapInsert(myheap,600))