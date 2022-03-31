#JJ has an array A of size N. He can perform the following operations on the array at most K times:
#
#Set Ai:=Ai+1 where 1≤i≤N−1
#Set Ai:=Ai−1 where 2≤i≤N
#He wants to maximize the value of the minimum element of the array A. Formally, he wants to maximize the value of min1≤i≤NAi.
#
#Can you help him do so?
#
#Input Format
#The first line contains a single integer T - the number of test cases. Then the test cases follow.
#The first line of each test case contains two integers N and K - the size of the array A and the maximum number of operations allowed respectively.
#The second line of each test case contains N space-separated integers A1,A2,…,AN denoting the array A.
#Output Format
#For each test case, output the maximum value of the minimum element of the array A that can be obtained after applying the given operation at most K times.
#
#Sum of N over all test cases does not exceed 2⋅105
#Sample Input 1 
#4
#5 4
#5 4 3 2 1
#6 1
#8 2 3 9 6 10
#5 2
#4 3 4 3 5
#5 1000
#4 3 4 3 5
#Sample Output 1 
#5
#3
#4
#5
#Explanation
#Test Case 1: We can perform the following operations (in the following order):
#
#Set A2:=A1. Array A becomes [5,5,3,2,1]
#Set A3:=A2. Array A becomes [5,5,5,2,1]
#Set A4:=A3. Array A becomes [5,5,5,5,1]
#Set A5:=A4. Array A becomes [5,5,5,5,5]
#Therefore the answer is 5.
#
#Test Case 2: We can perform the following operations (in the following order):
#
#Set A2:=A3. Array A becomes [8,3,3,9,6,10]
#Therefore the answer is 3.
#
#Test Case 3: We can perform the following operations (in the following order):
#
#Set A2:=A3. Array A becomes [4,4,4,3,5]
#Set A4:=A3. Array A becomes [4,4,4,4,5]
#Therefore the answer is 4.

def solve():
    c,d = map(int,input().split())
    a = list(map(int,input().strip().split()))
    
    a.sort()
    print(a[min(d,c-1)])

for _ in range(int(input())):
    solve()


t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split())) 
    l.sort()
    if(m>=n):
        m=n-1
    print(l[m])
