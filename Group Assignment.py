#Chef's professor is planning to give his class a group assignment. There are 2N students in the class, with distinct roll numbers ranging from 1 to 2N. Chef's roll number is X.
#The professor decided to create N groups of 2 students each. The groups were created as follows: the first group consists of roll numbers 1 and 2N, the second group of roll numbers 2 and 2Nā1, and so on, with the final group consisting of roll numbers N and N+1.
#Chef wonders who his partner will be. Can you help Chef by telling him the roll number of his partner?
#Input Format
#The first line of input will contain an integer T ā the number of test cases. The description of T test cases follows.
#The first and only line of each test case contains two integers N and X, denoting the number of groups that will be formed, and Chef's roll number.
#Output Format
#For each test case, output the roll number of the student that will be Chef's partner.

#Sample Input 1 
#3
#2 2
#3 1
#3 4

#Sample Output 1 
#3
#6
#3

#Explanation
#Test case 1: The groups will be {(1,4),(2,3)}. Chef's roll number is 2, so his partner's roll number will be 3.
#Test case 2: The groups will be {(1,6),(2,5),(3,4)}. Chef's roll number is 1, so his partner's roll number will be 6.
#Test case 3: The groups will be {(1,6),(2,5),(3,4)}. Chef's roll number is 4, so his partner's roll number will be 3.

def GROUPASSGN(N,X):
    f=2*N
    for e in range(1,N+1):
        y=e
        z=f-e + 1 
        if y== X:
            return z 
        if z==X:
            return y

n=int(input())
d=[]
for i in range(n):
    a,b=map(int,input().split())
    c=GROUPASSGN(a,b)
    d.append(c)
    
for x in range(len(d)):
    print(d[x])  
    
    
    
Sol

for _ in range(int(input())):
    n,x=map(int,input().split())
    if x>n:
        print(n-abs(n-x)+1)
    else:
        print(n+n-x+1)