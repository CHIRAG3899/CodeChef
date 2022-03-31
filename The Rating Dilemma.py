#Chef really likes to compete on Codechef, and he has gained an impressive rating of X, where X>0. There is also a parallel universe, where ratings on Codechef are negative instead. The only thing that remains unchanged in the parallel universe is Chef's love for competing on Codechef. Chef's rating on Codechef in the parallel universe is Y, where Y<0.
#Due to some cosmic event, the parallel universe has been destroyed, resulting in Chef forgetting both X and Y. He only remembers the sum S=X+Y. He wonders what the maximum possible product of his ratings is, given that he knows the sum of his ratings.
#
#Input Format
#The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
#The first and only line of each test case contains an integer S, the sum of Chef's ratings.
#Output Format
#For each test case, output the maximum possible product of Chef's ratings, given that he knows the sum of his ratings.
#
#Subtasks
#Subtask #1 (100 points): Original constraints
#
#Sample Input 1 
#2
#0
#1
#Sample Output 1 
#-1
#-2
#Explanation
#Test case 1: We have X>0 and X+Y=0. This implies that Y=−X. The product of ratings is −X2, and the maximum possible product is −1.

s=int(input())
while (s):
    m=int(input())
    k=m-(-1)
    s-=1
    print(k*-1)