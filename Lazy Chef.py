#Chef is a very lazy person. Whatever work is supposed to be finished
#in x units of time, he finishes it in m∗x units of time. But there is
#always a limit to laziness, so he delays the work by at max d units of time.
#Given x,m,d, find the maximum time taken by Chef to complete the work.

#Input:
#First line will contain T, number of testcases. Then the testcases follow.
#Each testcase contains a single line of input, three integers x,m,d.




n=int(input())
while(n>0):
    x, y,z =[int(x) for x in input().split()] 
    e=x*y
    f=x+z
    if (e>f):
        print(f)
    else:
        print(e)
    n-=1 
