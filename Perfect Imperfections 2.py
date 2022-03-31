#An array of integers is called good if all its elements are perfect squares.
#You are given an array A of N integers. In one move, you can do the following:
#Pick a subset of indices of the array, say {i1,i2,…,ik} where 1≤i1<i2<…<ik≤N
#Next, pick an integer X>0
#Finally, multiply the value at each chosen index by X, i.e, set Aij to Aij⋅X for each 1≤j≤k
#Find the minimum number of moves required to make the array good.
#Note: The value of X is fixed for a given move, but can vary between moves.

#Input Format
#The first line of input contains an integer T, denoting the number of test cases. The description of T test cases follows.
#Each test case contains two lines of input.
#The first line of each test case contains N, the size of the array.
#The second line contains N space-separated integers A1,A2,…,AN.
#Output Format
#For each testcase, output in a single line the minimum number of moves required to make the array good.

#Subtasks
#Subtask #1 (100 points): Original constraints
#
#Sample Input 1 
#5
#3
#15 2 4
#4
#15 14 4 9
#3
#10 3 6
#2
#4 9
#2
#2 8
#Sample Output 1 
#2
#2
#3
#0
#1
#Explanation
#Test case 1: One possible sequence of moves is:
#Multiply the first element by 15
#Multiply the second element by 2
#The array is now [225,4,4]=[152,22,22], which is good.
#Test case 3: One possible sequence of moves is:
#Multiply the first and third elements by 8
#Multiply the second and third elements by 3
#Multiply the first element by 20
#The array is now [1600,9,144]=[402,32,122], which is good.
#Test case 4: The array is already good, since [4,9]=[22,32], so no moves need to be made.

from collections import defaultdict
from math import sqrt


# determines the prime factors of n and their exponents modulo 2
def prime_factors(n):
    p_fs = dict()

    if n % 2 == 0:
        p_fs[2] = 0
        while n % 2 == 0:
            p_fs[2] = (1 - p_fs[2])
            n //= 2

    for ii in range(3, int(sqrt(n)) + 1, 2):
        if n % ii == 0:
            p_fs[ii] = 0
            while n % ii == 0:
                n //= ii
                p_fs[ii] = (1 - p_fs[ii])

    if n != 1:
        p_fs[n] = 1

    return p_fs


# performs additions of two binary arrays (which are represented by nonzero indices)
def add(v1: list, v2: list):
    ans = list(set(v1).symmetric_difference(set(v2)))
    ans.sort()
    if ans:
        return ans, ans[0]
    else:
        # If the sum is the zero vector
        return ans, -1


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        A = list(map(int, input().split()))

        # Obtains the set of primes that occurs in the prime factorization of all A[i]
        # Note: The answer is the rank of the matrix formed by binary vectors that are 
        #       formed by the exponents of the prime factorization of A[i] in F_2.
        primes = set()
        p_factors = defaultdict(list)
        n_rows = 0  # Counts the number of non-zero vectors = number of rows
        for i in range(N):
            pfs = prime_factors(A[i])

            for p in pfs:
                if pfs[p] & 1:
                    p_factors[i].append(p)
                    if p not in primes:
                        primes.add(p)
            p_factors[i].sort()

            # only consider none perfect squares
            if p_factors[i]:
                n_rows += 1

        # order primes from smallest to highest
        # Note: Ordering is very important for Gaussian elimination
        primes = sorted(list(primes))

        # creates a map of prime to its column index
        # i.e. Given columns 1,...,k corresponding to p1, ..., pk: this maps pi -> i
        p_to_id = defaultdict(int)
        m = 0  # will be number of columns = number of distinct primes
        for p in primes:
            p_to_id[p] = m
            m += 1

        # Let w_i denote the set of binary vectors whose leading nonzero term corresponds to column i
        # Creates the w_i sets to perform efficient sparse gaussian elimination
        n_vs = 0  # number of nonzero binary vectors (number of rows)
        w = defaultdict(list)
        for i in p_factors:
            if p_factors[i]:
                p = p_factors[i][0]
                # leading index
                k = p_to_id[p]

                # Creates the sparse vector of A[i] represented by indices
                v = [p_to_id[p] for p in p_factors[i]]
                v.sort()

                # v belongs to wk
                w[k].append(v)

        # sparse gaussian elimination to binary matrix to determine rank
        # Starting rank = number of rows
        for i in range(m):
            if len(w[i]) > 1:
                f = w[i].pop()
                while w[i]:
                    e = w[i].pop()
                    dif, ll = add(f, e)
                    if ll > i:
                        w[ll].append(dif)
                    elif ll == -1:
                        # Decrement rank because we have eliminated a vector
                        n_rows -= 1
                    else:
                        # This should not happen
                        raise RuntimeError('FUCK')

        # answer is the rank
        print(n_rows)
