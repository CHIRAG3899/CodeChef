#Chef has N friends. Chef promised that he would gift a pair of shoes (consisting of one left shoe and one right shoe) to each of his N friends. Chef was about to go to the marketplace to buy shoes, but he suddenly remembers that he already had M left shoes.
#What is the minimum number of extra shoes that Chef will have to buy to ensure that he is able to gift a pair of shoes to each of his N friends?
#For example, if N=2, M=4, then Chef already has 4 left shoes, so he must buy 2 extra right shoes to form 2 pairs of shoes.
#Therefore Chef must buy at least 2 extra shoes to ensure that he is able to get N=2 pairs of shoes.
#
#Input Format
#The first line contains a single integer T - the number of test cases. Then the test cases follow.
#The first line of each test case contains two integers N and M - the number of Chef's friends and the number of left shoes Chef has.
#Output Format
#For each test case, output the minimum number of extra shoes that Chef will have to buy to ensure that he is able to get N pairs of shoes.
#
#Sample Input 1 
#3
#2 4
#6 0
#4 3
#Sample Output 1 
#2
#12
#5
#Explanation
#Test Case 1: Discussed in the problem statement
#Test Case 2: Chef initially has no left shoes. He must buy 6 more left shoes and 6 more right shoes to form 6 pairs of shoes.
#Test Case 3: Chef initially has 3 left shoes. He must buy 1 more left shoe and 4 more right shoes to form 4 pairs of shoes.

sho = int(input())

for i in range(sho):
    n,m = map(int,input().split(" "))
    
    if m>n:
        print(n)
        
    else:
        h = n+(n-m)
        print(h)