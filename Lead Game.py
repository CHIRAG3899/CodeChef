#The game of billiards involves two players knocking 3 balls around on
#a green baize table. Well, there is more to it, but for our purposes
#this is sufficient.

#The game consists of several rounds and in each round both players
#obtain a score, based on how well they played. Once all the rounds have
#been played, the total score of each player is determined by adding up the
#scores in all the rounds and the player with the higher total score is
#declared the winner.

#The Siruseri Sports Club organises an annual billiards game
#where the top two players of Siruseri play against each other. The
#Manager of Siruseri Sports Club decided to add his own twist to the game
#by changing the rules for determining the winner. In his version, at the
#end of each round the leader and her current lead are calculated. Once all
#the rounds are over the player who had the maximum lead at the end of any
#round in the game is declared the winner.

#Consider the following score sheet for a game with 5 rounds:

#Round     Player 1       Player 2

#  1         140             82
#  2          89            134 
#  3          90            110 
#  4         112            106
#  5          88             90 
#The total scores of both players, the leader and the lead after
#each round for this game is given below:

#Round      Player 1       Player 2     Leader     Lead

#  1          140             82       Player 1     58
#  2          229            216       Player 1     13
#  3          319            326       Player 2      7
#  4          431            432       Player 2      1
#  5          519            522       Player 2      3
#The winner of this game is Player 1 as he had the maximum lead (58 at
#the end of round 1) during the game.

#Your task is to help the Manager find the winner and the winning lead.
#You may assume that the scores will be such that there will always be a
#single winner. That is, there are no ties.

n=int(input())
le1=[]
s1=0
s2=0
s=0
for i in range(n):
    x=list(map(int,input().split()))
    s1=s1+x[0]
    s2=s2+x[1]
    le1.append(s1-s2)
m1=max(le1)
m2=min(le1)*(-1)
if(m1>m2):
    print(1, m1)
else:
    print(2 ,m2)
