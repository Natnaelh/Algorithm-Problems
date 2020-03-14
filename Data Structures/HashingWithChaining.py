#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:11:04 2020

@author: natnem
"""

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable(object):
    def __init__(self):
         self.capacity = 111
         self.size = 0
         self.buckets = [None]*self.capacity
    
    def HashFunction(self,key):
        hashsum = 0
        for index , c in enumerate(key):
            hashsum += (index + len(key))^(ord(c))
#            print(index , ord(c) , hashsum)
            hashsum = hashsum % self.capacity
#            print(hashsum)
        return hashsum
    def insert(self,key,value):
        self.size += 1
        index = self.HashFunction(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return self.buckets[index]
        
        prev = node
        while node is not None:
            prev = node
            node = node.next
        
        prev.next = Node(key,value)
        return self.buckets[index]
    def find(self, key):
        index = self.HashFunction(key)
        node = self.buckets[index]
        
        while node is not None:
            if node.key == key:
                return node.value
            else:
                node = node.next
        return "Key Not Found"
    def delete(self,key):
        index = self.HashFunction(key)
        node = self.buckets[index]
        prev = None
        
        while node is not None:
            if node.key == key:
                break
            else:
                prev = node
                node = node.next
        if node is None:
            raise Exception("Key Not Found")
        if prev == None:
            return None
        else:
            result = node
            prev.next = node.next
        return result
        
        
        
        
        
#        while node is not None and node.key != key:
#            prev = node
#            node = node.next
#        if node is None:
#            return None
#        else:
#            self.size -= 1
#            result = node
#        if prev is None:
#            node = None
#        else:
#            prev.next = prev.next.next
                
            

            
    def __str__(self):
        dic = []
        for i in range(len(self.buckets)):
            node = self.buckets[i]
            while node is not None:
                dic.append([[i],[node.key,node.value]])
                node = node.next
        return dic
myhash = HashTable()
(myhash.insert("", 22))
(myhash.insert("Fike" , 20))
(myhash.insert("Nat" , 24))
(myhash.insert("F" , 23))
(myhash.insert("G" , 30))
print(myhash.__str__())
print(myhash.find(''))
#(myhash.delete("f"))
print(myhash.__str__())
