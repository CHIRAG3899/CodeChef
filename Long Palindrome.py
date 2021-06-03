#As we all know, a palindrome is a word that equals its reverse.
#Here are some examples of palindromes: malayalam, gag, appa, amma.

#We consider any sequence consisting of the letters of the
#English alphabet to be a word. So axxb,abbba and bbbccddx are words for
#our purpose. And aaabbaaa, abbba and bbb are examples of palindromes.

#By a subword of a word, we mean a contiguous subsequence of the word.
#For example the subwords of the word abbba are a, b, ab, bb, ba, abb, bbb,
#bba, abbb, bbba and abbba.

#In this task you will given a word and you must find the longest
#subword of this word that is also a palindrome.

#For example if the given word is abbba then the answer is abbba.
#If the given word is abcbcabbacba then the answer is bcabbacb.

#Input:
#The first line of the input contains a single integer N
#indicating the length of the word. The following line contains a
#single word of length N, made up of the letters a,b,…, z.

#Output:
#The first line of the output must contain a single integer
#indicating the length of the longest subword of the given word that
#is a palindrome. The second line must contain a subword that is a
#palindrome and which of maximum length. If there is more than one subword
#palindrome of maximum length, it suffices to print out any one.

n = int(input())
s = input('')
def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
def substring():
    for i in range(n):
        for j in range(i+1):
            p = s[j:j+n-i]
            if palindrome(p):
                print(n-i)
                print(p)
                return
substring()
