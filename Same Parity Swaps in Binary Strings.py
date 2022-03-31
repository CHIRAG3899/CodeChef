#You are given a binary string S of length N (i.e. every character of S is either 0 or 1).
#You can perform the following operation on S:
#select any two indices i,j of the same parity, i.e. either both i,j are odd or both i,j are even
#swap Si and Sj
#For example, in the string 1110, we can swap the second and the fourth characters to get 1011. However, we can never obtain 1101 from 1110 by performing such swaps.
#Find the maximum possible number of occurrences of the string 01 as a substring of S after performing the above operation any number of times (it is also allowed to not perform any operation).
#For example, the string 1110 has no occurrence of the string 01 as a substring, whereas we can swap the second and fourth characters to obtain 1011 which has exactly one occurrence of 01 (colored red).

#Input Format
#The first line of input contains an integer T, denoting the number of testcases. The description of the T testcases follow.
#Each testcase consists of two lines.
#The first line contains a single integer N, the length of the string S.
#The second line contains a binary string of length N.
#Output Format
#For each testcase, print in a single line, an integer — the answer as per the problem statement.

#Subtasks
#Subtask #1 (100 points): Original constraints

#Sample Input 1 
#3
#5
#00100
#5
#01010
#5
#10001
#Sample Output 1 
#1
#2
#2
#Explanation
#Test case 1: The only strings that can be obtained by performing the given operations are {10000,00100,00001}. Of these the two strings 00100 and 00001 contain exactly one occurrence of 01.
#Test case 2: The given string S cannot be changed by performing the given operation and contains 2 occurrences of the string 01, i.e. 01010.
#Test case 3: The only strings that can be obtained by performing the given operations are {00101,10001,10100}. The string 00101 contains two occurrences of 01.

# cook your dish here
try:
    for _ in range(int(input())):
        N=int(input())
        S=input()
        x2,x1=0,0
        ans=True
        if N%2==0:
            for i in range(0,N-1,2):
                if S[i]!='0' or S[i+1]!='1':
                    ans=False
                    break
            if ans:
                print(N//2)
                continue
                
        for i in S:
            if i=='0':
                x1+=1
            else:
                x2+=1
        if x1==x2:
            print(x1-1)
            continue
        print(min(x1,x2))
except:
    pass
        
    
            
            
    

