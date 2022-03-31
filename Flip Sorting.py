#Chef has a binary string S of length N. Chef can perform the following operation on S any number of times (possibly zero):
#
#Choose a number X (1≤X≤N) that hasn't been chosen in any previous operation and flip any substring of S having length X (i.e. change all 0s to 1s and all 1s to 0s in any substring of S having length X).
#Chef wants to transform S into a non-decreasing string using any sequence of operations. Can you help Chef find such a sequence of operations?
#
#If there are multiple answers, print any.
#
#Input Format
#The first line contains a single integer T - the number of test cases. Then the test cases follow.
#The first line of each test case contains an integer N - the length of the binary string S.
#The second line of each test case contains a binary string S of length N containing 0s and 1s only.
#Output Format
#For each test case,
#
#Output in the first line K - the number of operations applied.
#In each of the following K lines, output two integers i and X - the starting index of the substring selected and the length of the substring. (Note that X selected should not be used in any of the previous operations)

#Sample Input 1 
#3
#6
#110111
#9
#110110111
#5
#00111
#Sample Output 1 
#1
#1 2
#2
#1 2
#4 3
#0
#Explanation
#Test Case 1: The operations applied are as follows: 11–––0111→000111.
#
#Test Case 2: The operations applied are as follows: 11–––0110111→000110––––111→000001111.

tc = int(input())
for _ in range(tc):
    s = int(input())
    st = list(input())
    res = []
    for i in range(s - 1, -1, -1):
        if st[i] == '0':
            x = i + 1
            for j in range(i + 1):
                if st[j] == "1":
                    st[j] = "0"
                else:
                    st[j] = "1"
            res.append([1, x])
    print(len(res))
    for k in res:
        print(k[0], k[1])
        

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
    s=list(map(int,input().rstrip()))
    ans = []
    now = 0
    for i in range(n):
        if s[i] != now:
            ans.append([i+1,n-i])
            now = 1 - now
    print(len(ans))
    for x,y in ans:
        print(x,y)