#Chef was recently studying the Bitwise OR operation, and stumbled upon the following problem:
#Let F(i)=1 | 2 | 3 | … | i, where | denotes bitwise OR.
#You are given an integer N. Find the number of distinct i such that 2≤i≤N and F(i)=F(i−1).
#Input Format
#The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
#The first and only line of each test case contains an integer N.
#Output Format
#For each test case, output the number of distinct i such that 2≤i≤N and F(i)=F(i−1).

#Sample Input 1 
#3
#2
#3
#4
#Sample Output 1 
#0
#1
#1
#Explanation
#We have:
#F(1)=1
#F(2)=3
#F(3)=3
#F(4)=7
#Test case 1: F(2)≠F(1). Hence the answer is 0.
#Test case 2: For i=3, F(i)=F(i−1). Hence the answer is 1.
#Test case 3: For i=3, F(i)=F(i−1). For i=2,4, F(i)≠F(i−1). Hence the answer is 1.

import math
t=int(input())
for tc in range(t):
    n=int(input())
    x=math.floor(math.log(n,2))
    s=0
    for i in range(1,x):
        s+=pow(2,i)-1
    s+=n-pow(2,x)    
    print(s)