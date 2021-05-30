#Chef knows about two languages spoken in Chefland, but he is not
#proficient in any of them. The first language containslowercase English
#letters between 'a' and 'm' inclusive and the second language contains only
#uppercase English letters between 'N' and 'Z' inclusive.

#Due to Chef's limited vocabulary, he sometimes mixes the languages when
#forming a sentence — each word of Chef's sentence contains only characters
#from one of the languages, but different words may come from different languages.

#You are given a sentence as a sequence of K words S1,S2,…,SK. Determine
#whether it could be a sentence formed by Chef, i.e. if it contains only the
#characters from the two given languages and each word contains only
#characters from a single language.

#Input
#The first line of the input contains a single integer T denoting the number
#of test cases. The description of T test cases follows.
#The first and only line of each test case contains an integer K followed by a
#space and K space-separated strings S1,S2,…,SK.
#Output
#For each test case, print a single line containing the string "YES" if the
#given sentence can be formed by Chef or "NO" if it cannot.

#You may print each character of the string in uppercase or lowercase (for
#example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as iden0tical).

t=int(input())
for i in range(0,t):
    inp=input()
    ls=inp.split(" ")
    flag=0
    for k in range(1,int(ls[0])+1):
        if ord(ls[k][0])<91:
            x,y=78,91
        else:
            x,y=97,110
        if not(all(ord(j) in range(x,y) for j in ls[k])):
            flag=1
            break
    if flag==0:
        print("YES")
    else:
        print("NO")
