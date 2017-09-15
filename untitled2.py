# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:14:11 2017

@author: Kaushik_PC
"""
File_name = raw_input("File Name: ")


List = open(File_name).readlines()

print List

with open(File_name) as fp:
    List = fp.read().split("\n")

print List

no_server=int(List[0])

s_nextavail = [0 for i in range(0, no_server)]

s_efficiency = List[1:6]

print s_efficiency

for index in range(len(List[6:])):
   print 'Customer Arrival :', List[index]
   
   class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
q=Queue()

for index in range(len(List[6:])):
   print 'Customer Arrival :', List[index]
   q.enqueue(List[index])


q.size()

q.enqueue(True)

s_nextavail = List[0]

s_nextavail = [ 0 for i in range(0,no_server) ]

efficiency_at_hand = [ s_efficiency[i] if s_nextavail[i] == 0 else 9999for i in range(0,len(s_nextavail)-1)]

server_to_assign = efficiency_at_hand.index(min(efficiency_at_hand))

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                     
bubbleSort(s_efficiency)
print(s_efficiency)


