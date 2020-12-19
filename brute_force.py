R,S,P = map(int,input().split())
 
l=list()
l=[0]*R + [1]*S +[2]*P
# i marked rocks as 0 , scissor as 1 and paper as 2
 
from itertools import permutations
 
k= list(permutations(l))
 
rock_wins = 0
scissor_wins = 0
paper_wins = 0
 
for i in k:
    winner = i[0] # i took the first player as winner
    for j in range(1,len(i)):
 
        if i[j]==winner:
            #it means fight between same kind of players, so it is a draw.
            pass#did nothing
        elif abs(i[j]-winner)==1:
            #it means either a fight between 0 and 1 (rocks or scissor) or between
            # 1 and 2 (scissor and paper) , in both cases, smaller value wins.
            winner = min(winner,i[j])
        else:
            #it means a fight between 0 and 2, i.e. a paper and rock
            winner = 2
    if winner==0:
        rock_wins+=1
    elif winner==1:
        scissor_wins+=1
    else:
        paper_wins+=1
 
total = len(k)
print(rock_wins/total,scissor_wins/total,paper_wins/total)