#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:20:19 2019

@author: niclas
"""

import numpy as np

def chase(A):
    n = len(A)
    for y in range(n-1):
        for x in range(n):
            if A[y,x] == 0.:
                change_state(A,y+1,x)
    return A
                
def change_state(A,y,x):
    n = len(A)
    A[y,x] = abs(A[y,x]-1)
    if y > 0 :
        A[y-1,x] = abs(A[y-1,x]-1)
    if x < n-1:
        A[y,x+1] = abs(A[y,x+1]-1)   
    if x > 0:
        A[y,x-1] = abs(A[y,x-1]-1)
    if y < n-1 :  
        A[y+1,x] = abs(A[y+1,x]-1)

def binary_combinations(n):
    combinations = [[0],[1]]
    zero = 0
    one = 1
    newcombi = []
    for x in range (n-1):
            for sublist in combinations:
                new = sublist[:]
                new.append(one)
                sublist.append(zero)
                newcombi.append(new)
            combinations += newcombi
            newcombi = []
    return combinations

#for n in range(3,10):
#    combinations = binary_combinations(n)
#        
#    A = np.zeros((n,n))
#    
#    Initial = chase(A)
#    lower = Initial[n-1]
#    
#    for seq in combinations:
#        A = np.copy(Initial)
#        for i in range(len(seq)):
#            if seq[i] == 1:
#               change_state(A,0,i)
#        A = chase(A)
#        row = A[n-1]
#        solved = True
#        for i in row:
#            if i == 0:
#                solved = False
#        if solved:
#            print("Number",n, "results in",lower)
#            print("Solved with sequence: ", seq, "\n")
#            break

#for n in range(3320,3322):
#    A = np.zeros((n,n))
#    A = chase(A)
#    lower = A[n-1]
#    solved = True
#    for i in lower:
#        if i == 0:
#            solved = False
#    if solved:
#        print(n)
#    if n%10 == 0:
#        print("reached",n)

#find minimum number of moves
n = 4

comb_5 = binary_combinations(n**2)
print("Generated combinations")
best = n**2
best_seq = None

for seq in comb_5:
    if sum(seq) < best and sum(seq) > (n**2/5):
        A = np.zeros((n,n))
        for h in range(n**2):
            x = h%n
            y = h//n
            if seq[h] == 1:
                change_state(A,y,x)
        solved = True
        for line in A:
            for tile in line:
                if tile == 0:
                    solved = False
                    break
            if not solved:
                break
        if solved:
            if sum(seq) < best:
                best_seq = seq
            best = min(best,sum(seq))

print(best, best_seq)
        
            
            
            
