#Nathan is preparing for the Dash marathon. He has N training plans. The i-th plan has an effectiveness of Ai, but requires that at least Bi other training plans must be performed before it. A training plan cannot be repeated.
#
#If he performs some K>0 distinct trainings - P1,P2,…,PK (1≤Pi≤N,Pi≠Pj) then his training score is ∑Kj=1APjK. If Nathan does not perform any training plan (K=0), then his score is 0.
#
#What is the highest score that Nathan can get by performing zero or more training plans, if he can perform them in any order?
#
#Input Format
#The first line of the input contains a single integer T - the number of test cases. The description of T test cases follows.
#The first line of each test case contains N - the number of training plans.
#The second line contains N integers A1,A2,…,AN where Ai is the effectiveness of the i-th training plan.
#The third line contains N integers B1,B2,…,BN where Bi is the number of pre-requisite training plans for the i-th training plan.
#Output Format
#For each test case, output a single real number - the highest score that Nathan can get by performing zero or more training plans.
#Your answer is considered correct if its absolute or relative error does not exceed 10−6. Formally, let your answer be X, and the jury's answer be Y. Your answer is accepted if and only if |X−Y|max(1,|Y|)≤10−6.
#
#Sum of N over all test cases does not exceed 5⋅105.
#Sample Input 1 
#3
#4
#-9 -21 -4 -43
#0 0 0 0
#5
#10 14 5 9 1
#4 1 3 0 0
#7
#-1 101 5 63 -7 -88 59
#0 1 6 2 3 4 5
#Sample Output 1 
#0.000000
#11.500000
#54.333333
#Explanation
#Test case 1: It is optimal for Nathan to not perform any training plans as all the plans have negative Ai value.
#
#Test case 2: It is optimal for Nathan to:
#
#First, perform the 4-th training plan (for which Bi=0).
#Then perform the 2-nd training plan (for which Bi=1 which is satisfied as he has already performed 1 training plan)
#Test case 3: It is optimal for Nathan to:
#
#First, perform the 1-st training plan (for which Bi=0).
#Then perform the 2-nd training plan (for which Bi=1 which is satisfied as he has already performed 1 training plan)
#Then perform the 4-th training plan (for which Bi=2 which is satisfied as he has already performed 2 training plans)

#!/usr/bin/env PyPy3
from collections import Counter, defaultdict, deque
import itertools
import re
import math
from functools import reduce
import operator
import bisect
import heapq
import functools
mod=10**9+7

import sys
input=sys.stdin.readline
t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    tr = [[] for _ in range(n)]
    for i in range(n):
        tr[b[i]].append(a[i])
    ans = 0
    su = 0
    heap = []
    for i in range(n):
        for j in tr[i]:
            heapq.heappush(heap,-j)
        if not heap:
            break
        su += -heapq.heappop(heap)
        ans = max(ans,su/(i+1))
    print(ans)


import heapq
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    req = list(map(int,input().split()))
    ans = 0
   
    dit = {}
    for i in range(n):
        if req[i] in dit:
            dit[req[i]].append(arr[i])
        else:
            dit[req[i]] = [arr[i]]
    
    hp = []        
    i = 0
    count=0
    s=0
    while True:
        if i not in dit:
            if not hp:
                break
            else:
                s+= -(heapq.heappop(hp))
                
        else:
            m = max(dit[i])
            if not hp or ( hp and -(hp[0])<m):
                s+=m
                dit[i].remove(m)
                
                for e in dit[i]:
                    heapq.heappush(hp,-e)
            
            else:
                s+= -(heapq.heappop(hp))
                
                for e in dit[i]:
                    heapq.heappush(hp,-e)
                    
        count+=1
        curr = s/count
        ans = max(ans,curr)
                    
        i+=1
        
    print("%.6f" %ans)  
                
        
        
            
            
    
            

    
