#A despotic king decided that his kingdom needed to be rid of corruption
#and disparity. He called his prime minister and ordered that all corrupt
#citizens be put to death. Moreover, he wanted this done quickly.

#The wily prime minister realised that investigating every citizen to decide
#who was corrupt and who was not was rather difficult. So he decided on the
#following plan: He ordered all the citizens to appear in the court one by
#one and declare their wealth.

#The king does not sit in the court all the time (he has other important
#business to attend to - for instance, meet dignitaries from neighbouring
#kingdoms, spend time with his family …) Whenever the king walks into the
#court, the prime minister pulls out the richest man who has appeared before
#the court so far and is still alive and beheads him for being corrupt.
#Since the rich are more likely to be corrupt, he hopes to get rid of most
#of the corrupt and the king is happy as he sees his policy being implemented
#enthusiastically.

#Suppose the wealth of the citizens trooping into the court is
#1 3 7 6 5 18 9 11 2 4
#and the king walked in three times: the first time after the first four
#persons have seen the minister, the second time after the first five persons
#have seen the minister and, finally after the first nine persons have seen
#the minister.

#At the king's first visit the richest person to have met the minister has
#wealth 7 and he would be beheaded. At the second visit, the wealth of the
#richest person who has met the minister and is still alive has wealth 6 and
#so he would be beheaded. At the third visit the richest person to have met
#the minister who is still alive has wealth 18 and so he would be beheaded.

#You may assume that the input is such that whenever the king walks in,
#it is always possible to behead someone.

#Your aim is to write a program that will enable the prime minister to
#identify the richest man to have met the minister and who is still alive
#quickly. You may assume that no two citizens have the same wealth.

#Input:
#The first line of the input consists of two numbers N and M, where N is the
#number of citizens in the kingdom and M is the number of visits to the court
#by the king.

#The next N+M lines describe the order in which the N citizens' appearances
#are interleaved with the M visits by the king. A citizen's visit is denoted
#by a positive integer, signifying his wealth. You may assume that no two
#citizens have the same wealth. A visit by the king is denoted by −1.

a,b=input().split()
z=[]
l=[]
for _ in range(int(a)+int(b)):
    n=int(input())
    if(n==-1):
        if(len(l)!=0):
            l=sorted(l)
            z.append(l)
        k=0
        while(len(z[k])==0):
            k+=1
        for j in range(len(z)):
            if(len(z[j])!=0 and z[j][-1]>z[k][-1]):
                k=j
        if(len(z)!=0):
            print(z[k].pop())
        l=[]
    else:
        l.append(n)
