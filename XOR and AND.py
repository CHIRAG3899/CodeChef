#Alice has an array A of length N. She is interested in finding the number of pairs (i,j) such that 1≤i<j≤N and Ai|Aj<Ai&Aj.
#| represents the Bitwise XOR operator. & represents the Bitwise AND operator.
#Input Format
#The first line of input will contain an integer T — number of test cases. Then the test cases follow.
#Each test case contains two lines of input.
#The first line of each test case contains an integer N, the length of the array A.
#The second line of each test case contains N space-separated integers A1,A2,…,AN.
#Output Format
#For each test case, output the number of pairs (i,j) such that 1≤i<j≤N and Ai|Aj<Ai&Aj.

#Sum of N over all test cases does not exceed 3⋅105.
#Sample Input 1 
#2
#4
#1 1 2 3
#4
#1 2 3 4
#Sample Output 1 
#2
#1
#Explanation
#Test case 1: The two pairs of indices satisfying the condition are (1,2) and (3,4), because
#A1|A2=0 and A1&A2=1
#A3|A4=1 and A3&A4=2
#Test case 2: The only pair of indices satisfying the condition is (2,3).

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    b=[0]*40
    for a in range(n):
        c=0
        m=arr[a]
        while(m>=2):
            m=m//2
            c+=1
        b[c]+=1 
    sum=0 
    for a in range(40):
        sum+=(b[a]*(b[a]-1))//2
    print(sum)
