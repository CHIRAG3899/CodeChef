#A famous student of AESC MSU, as you know, comes from Kostomuksha. Kostomuksha has a popular game called Doka.
#The essence of Doka is as follows:
#You are given an array A and an integer X. You want to calculate how many subarrays of this array have a geometric mean of X.
#Formally, calculate the number of pairs of integers (L,R) such that 1≤L≤R≤N and
#AL⋅AL+1⋅…⋅AR−−−−−−−−−−−−−−−√R−L+1=X

#Input Format
#The first line of input contains an integer T, denoting the number of test cases. The description of T test cases follows.
#Each test case consists of two lines of input.
#The first line of each test case contains two space-separated integers N,X — the size of the array A and the required geometric mean.
#The second line of each test case contains N space-separated integers A1,A2,…,AN.
#Output Format
#For each test case, on a new line print the number of subarrays that satisfy the condition.

#Subtasks
#Subtask #1 (100 points): Original constraints
#
#Sample Input 1 
#3
#3 3
#3 3 3
#4 4
#1 2 3 4
#4 54
#36 81 54 54
#Sample Output 1 
#6
#1
#6
#Explanation
#Test case 1: Every subarray has a geometric mean of 3, and there are 6 subarrays in total so the answer is 6.
#Test case 2: The only subarray with a geometric mean of 4 is the singleton array [4], obtained with L=R=4.
#Test case 3: The 6 pairs of (L,R) which have a geometric mean of 54 are:
#(1,2), giving the subarray [36,81]
#(1,3), giving the subarray [36,81,54]
#(1,4), giving the subarray [36,81,54,54]
#(3,3), giving the subarray [54]
#(3,4), giving the subarray [54,54]
#(4,4), giving the subarray [54]

# cook your dish here
import numpy

def gcd(n, d):
    while d != 0:
        t = d
        d = n%d
        n = t
    return n  
    
def reduce(n,d):
     greatest=gcd(n,d)
     n/=greatest
     d/=greatest
     return int(n), int(d)      
    
T= int(input())
for numTests in range(T):
    N, X = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    A = numpy.array(A,dtype=float)
    data = numpy.log(A/X)
    data = numpy.cumsum(data)
    
    data = data.round(decimals=10)
    t = numpy.unique(data)
    #print(t)
    total =0
    for i in range(len(t)):
        tmp = numpy.where((data == t[i]))[0]
        #print(len(tmp),t[0,i],t[1,i])
        if t[i]==0:
            total+=len(tmp) * (len(tmp)+1)//2
        else:
            total+= len(tmp) * (len(tmp)-1)//2  
    print(total)
