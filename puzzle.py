 import numpy as np

puzzle=[[6,1,10,2],[7,11,4,14],[5,9,0,15],[8,12,13,3]]
dimension=len(puzzle)
position=0
inversion=0

workdone=np.zeros((4,4),dtype=bool) 
print workdone     
for i in range(len(puzzle)):
    for j in range(len(puzzle)):
        if puzzle[i][j]==0:
            position=dimension-i
            print position
            
for i in range (len(puzzle)):
        for j in range (len(puzzle)):
            workdone[i][j]=True
            for k in range(len(puzzle)):
                for l in range(len(puzzle)):
                          if puzzle[i][j]> puzzle[k][l]:
                              if (workdone[k][l]==False) and puzzle [k][l]!=0:
                                  inversion+=1 
                 
if dimension%2==0:
    if position%2!=0 and inversion%2==0:
        print "puzzle is solvable"
    elif position%2==0 and inversion!=0:
        print "puzzle is solvable"
    else:
        print "puzzle is not solvable where inversion is:"+str(inversion)
elif dimension%2!=0:
    if inversion%2==0:
        print "puzzle is solvable"
    else:
         print "puzzle is not solvable where inversion is:"+str(inversion)