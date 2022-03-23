#Given N points in a 2D space, find the minimum sum of areas of rectangles required to cover all the points given that we can use at most 2 non-overlapping rectangles whose sides can touch. The rectangles must be axis-aligned, meaning the sides are vertical and horizontal.
#Input
#The first line contains an integer T, the number of test cases. Then the test cases follow.
#Each test case contains N+1 lines of input.
#The first line contains a single integer N, the number of points.
#The next N lines each contains two integers xi, yi, the coordinates of the i-th point.
#Note: Points need not be distinct.
#Output
#For each test case, output in a single line the answer to the problem.
#Sample Input
#3
#1
#100 100
#4
#1 100
#100 100
#100 1
#1 1
#5
#1 100
#100 100
#100 1
#1 1
#50 50
#Sample Output
#0
#0
#4851
#Explanation
#Case 1: Since there is only one point, the minimum area of a rectangle to cover this point is 0.
#Case 2: We can have rectangles as 2 opposite sides of the square. Since the width of the rectangles is 0, the total area is also 0.
#Case 3: The optimal solution is with the rectangles having endpoints {(1,1),(100,1),(1,50),(100,50)} and {(1,100),(1,100),(100,100),(100,100)}. Therefore the total area is  49⋅99+0⋅99=4851

def height(A,n):
    a=[]
    mn=1e9+1
    mx=-1
    
    for i in range(n-1):
        if A[i]<mn:
            mn=A[i]
       
        if A[i]>mx:
            mx=A[i]
        a.append(mx-mn)
    return a

def sort(L):
    return sorted(L, key=lambda x: x[0])

def fun(A,n):
    l2=[]
    for i in range(n):
        l2.append(A[i][1])
   
    h1=height(l2,n)
    h2=height(l2[::-1],n)
    h2=h2[::-1]
    area=1e19+1
  
    for i in range(n-1):
        temp=(h1[i]*(A[i][0]-A[0][0]))+(h2[i]*(A[-1][0]-A[i+1][0]))
        if(temp<area):
            area=temp
            
    if area==1e19:
        return 0 
    else:
        return area
    
for i in range(int(input())):
    n=int(input())
    Lx,Ly=[],[]
    for i in range(n):
        a,b=map(int,input().split())
        Lx.append([a,b])
        Ly.append([b,a])
    Lx=sort(Lx)
    Ly=sort(Ly)
    
    area1=fun(Lx,n)
    area2=fun(Ly,n)
    print(min(area1,area2))
