#According to the new tax scheme, a new tax called the binary string tax was introduced! JJ has a binary string S of length N. According to the tax scheme, for every occurrence of 01 in S, a tax of X rupees will be charged, while for every occurrence of 10 in S, a tax of Y rupees will be charged.
#
#For example, if X=5, Y=7 and S=11010, then S has 1 occurrence of 01 and 2 occurrences of 10, so the tax charged =5⋅1+7⋅2=19
#
#JJ can rearrange the string S in any way he wants. He wants to minimize the amount of tax he has to pay. Can you help him do so?
#
#Input Format
#The first line contains a single integer T - the number of test cases. Then the test cases follow.
#The first line of each test case contains three integers N, X and Y - the length of the binary string S, the tax charged on an occurrence of 01 and the tax charged on an occurrence of 10.
#The second line of each test case contains a binary string S of length N containing 0s and 1s only.
#Output Format
#For each test case, output the minimum amount of tax that JJ has to pay.
#
#Sample Input 1 
#2
#4 7 3
#1101
#5 3 4
#00000
#Sample Output 1 
#3
#0
#Explanation
#Test Case 1: JJ can rearrange S to 1110 for which the tax charged will be 3 which is the minimum value of tax.
#Test Case 2: The tax charged for the string S=00000 is 0 which can not be reduced further.

try:
    t=int(input())
    for i in range(t):
        N,X,Y=map(int,input().split())
        s=input()[:N]
        if s.count("0")==0 or s.count("1")==0:
            print("0")
        else:
            print(min(X,Y))
except:
    pass
	
t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    st=input()
    count1=0
    for i in range(n):
        if st[i]=='1':
            count1+=1
    if count1==0 or count1==n:
        print(0)
    else:
        print(min(x,y))