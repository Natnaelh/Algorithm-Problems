
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:00:00 2020

@author: natnem
"""

def CountingSort(A):

    k = max(A) + 1
    C = [0]*(k) #Auxillary array to keep track of the key appearances
    B = [0]*(len(A)) #To hold the output 
    for i in A:
        C[i] = C[i] + 1   #0 i if key(Index) is in A else, increment for each apperance of keys
    
    for x in range(1,k):
        C[x] = C[x] + C[x-1] #to keep track of how many keys are before the key in C
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]    #place the key in sorted place 
        C[A[j]] = C[A[j]] - 1  #decrement key appearance from auxillary array
    
    return B
A = [2,5,3,0,1,1]
print(CountingSort(A))
        