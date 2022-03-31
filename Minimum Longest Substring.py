#You are given a binary string A of length N. Rearrange the binary string to form binary strings S and T such that the length of the longest common substring between S and T is minimum.
#Print both strings S and T.
#Note that both S and T must be anagrams of A — see the examples below for more clarity.

#Input Format
#The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
#Each test case consists of two lines.
#The first line of each test case contains a single integer N — the length of the binary string A.
#The second line of each test case contains a binary string A of length N.
#Output Format
#For each test case, output two lines. The first line contains string S while the second line contains string T. Both strings S and T must be anagrams of string A and thus, have length N.

#Subtasks
#Subtask #1 (100 points): Original constraints
#
#Sample Input 1 
#3
#3
#101
#4
#1111
#4
#0111
#Sample Output 1 
#110
#011
#1111
#1111
#1101
#0111
#Explanation
#Test case 1: The given string is A=101. Two rearrangements of A such that the length of longest common substring is minimum are S=110 and T=011. The longest common substring between strings S and T is 11, having length 2. It can be proved that for no other pair of rearrangements of string A, the LCS has a length less than 2.
#Test case 2: The given string is A=1111. Here, all rearrangements of A are the same. Two rearrangements of A such that the length of longest common substring is minimum are S=1111 and T=1111. The longest common substring between strings S and T is 1111, having length 4.
#Test case 3: The given string is A=0111. Two rearrangements of A such that the length of longest common substring is minimum are S=1101 and T=0111. The longest common substring between strings S and T is 01 having length 2. It can be proved that for no other pair of rearrangements of string A, the LCS has a length less than 2.

def generate(maxchar, minchar, ones, zero, quot, rem, x):
    res = ""
    while x:
        res += maxchar*quot
        if rem > 0:
            res += maxchar
            rem -= 1
        res += minchar
        x -= 1
    res += maxchar*quot
    if rem > 0:
        res += maxchar
        rem -= 1
    
    return res
        
def solve(st, n):
    ones = 0
    zero = 0
    for d in st:
        if d == '0':
            zero += 1
        else:
            ones += 1
    
    if ones > zero:
        s = "0"*zero
        s += '1'*ones

        quot = ones//(zero + 1)
        rem = ones % (zero+1)
        t = generate("1", "0", ones, zero, quot, rem, zero)
    
    else:
        s = "1"*ones
        s += "0"*zero

        quot = zero//(ones+1)
        rem = zero % (ones + 1)
        t = generate("0", "1", ones, zero, quot, rem, ones)

    print(s)
    print(t)
            

t = int(input())
for i in range(t):
    n = int(input())
    string = input()
    solve(string, n)