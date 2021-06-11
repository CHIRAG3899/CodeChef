#It is an interesting exercise to write a program to print out all permutations
#of 1,2,…,n. However, since there are 6227020800 permutations of 1,2,…,13, it
#is unlikely that we would ever run this program on an input of size more than 10.
#However, here is another interesting problem whose solution can also be used
#to generate permutations. We can order the permutations of 1,2,…,n under the
#lexicographic (or dictionary) order. Here are the permutations of 1,2,3 in
#lexicographic order:123132213231312321
#The problem we have is the following: given a permutation of 1,2,…,n, generate
#the next permutation in lexicographic order. For example, for 2314 the answer
#is 2341.
#Input:
#The first line of the input contains two integers, N and K. This is followed
#by K lines, each of which contains one permutation of 1,2,…,N.
#Output:
#The output should consist of K lines. Line i should contain the lexicographical
#ly next permutation correponding to the permutation on line i+1 in the input.
#Sample input
#3 2
#3 1 2
#2 3 1
#Sample output
#3 2 1
#3 1 2

def solve(arr):
    sarr=[]
    p=0
    for j in range(len(arr)-1,0,-1):
        if(arr[j]>arr[j-1]):
            sarr.append(arr[j-1])
            sarr.append(arr[j])
            p=j-1
            v=arr[j-1]
            break
        else:
            sarr.append(arr[j])
    
    sarr.sort()
    arr[p]=sarr[sarr.index(v)+1]
    sarr.pop(sarr.index(v)+1)
    arr[p+1:]=sarr
    for i in arr:
        print(i,end=" ")
        

t=[int(x) for x in input().split()]
n=t[0]
k=t[1]

for i in range(k):
    arr=[int(x) for x in input().split()]
    solve(arr)
    print()
