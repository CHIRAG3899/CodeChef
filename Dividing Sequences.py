#This problem is about sequences of positive integers a1,a2,...,aN. A subsequence
#of a sequence is anything obtained by dropping some of the elements. For
#example, 3,7,11,3 is a subsequence of 6,3,11,5,7,4,3,11,5,3 , but 3,3,7 is
#not a subsequence of 6,3,11,5,7,4,3,11,5,3 .
#A fully dividing sequence is a sequence a1,a2,...,aN where ai divides aj
#whenever i<j. For example, 3,15,60,720 is a fully dividing sequence.
#Given a sequence of integers your aim is to find the length of the longest
#fully dividing subsequence of this sequence.
#Consider the sequence 2,3,7,8,14,39,145,76,320
#It has a fully dividing sequence of length 3, namely 2,8,320, but none of
#length 4 or greater.
#Consider the sequence 2,11,16,12,36,60,71,17,29,144,288,129,432,993.
#It has two fully dividing subsequences of length 5,
#2,11,16,12,36,60,71,17,29,144,288,129,432,993 and
#2,11,16,12,36,60,71,17,29,144,288,129,432,993 and none of length 6 or greater.
#Input:
#The first line of input contains a single positive integer N indicating the
#length of the input sequence. Lines 2,...,N+1 contain one integer each. The
#integer on line i+1 is ai.
#Output:
#Your output should consist of a single integer indicating the length of the
#longest fully dividing subsequence of the input sequence.
#Sample input 1:
#9
#2 
#3 
#7 
#8 
#14 
#39 
#145 
#76 
#320
#Sample output 1:
#3

list1=[]
n=int(input())
dp=[1]*n
for i in range(n):
    list1.append(int(input()))
max1=0
for i in range(n-1):
    for j in range(i+1,n):
        if list1[j] % list1[i]==0:
            prev=dp[j]
            curr=dp[i]+1
            if curr > prev:
                dp[j]=curr
                if curr > max1:
                    max1=curr
print(max1)

