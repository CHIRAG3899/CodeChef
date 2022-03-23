#Initially, Chef is at coordinate 0 on X-axis. For each i=1,2,…,N in order, Chef does the following:

#If Chef is at a non-negative coordinate, he moves i steps backward (i.e, his position's coordinate decreases by i), otherwise he moves i steps forward (i.e, his position's coordinate increases by i).
#You are given the integer N. Find the final position of Chef on the X-axis after N operations.

#Input Format
#The first line of input contains an integer T, denoting the number of test cases. The T test cases then follow:
#The first and only line of each test case contains an integer N.
#Output Format
#For each test case, output in a single line the final position of Chef on the X-axis after N operations.

#Sample Input 1 
#3
#1
#2
#3
#Sample Output 1 
#-1
#1
#-2

#Explanation
#Test case 1: Initially, Chef is at coordinate 0 on X-axis. As 0 is non-negative, during the first operation Chef moves 1 step backward and reaches the coordinate −1.
#Test case 2: Chef is at coordinate −1 on X-axis after the first operation. As −1 is negative, during the second operation Chef moves 2 steps forward and reaches the coordinate 1.

d=[]
for _ in range(int(input())):
    n=int(input())
    if n&1:
        a=(-1*((n+1)//2))
        d.append(a)
    else:
        a=(n//2)
        d.append(a)

for x in range(len(d)):
    print(d[x])
        