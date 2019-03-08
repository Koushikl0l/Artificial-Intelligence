#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 08:47:44 2018

@author: koushikahamed
"""
import numpy as np
import time

class Nqueen:
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.N=8       
    def solution(self,N):
        self.keepTrack=np.array([0,1,2,3,4,5,6,7],dtype=object)
        if(self.doSolve(0,N,self.keepTrack)):
            return self.keepTrack
        return None
    
    def print_solution(self,result):
        self.res=np.zeros((self.N,self.N),dtype=int)
        for i in range(self.N):
            for j in range(self.N):
                if i==result[i].row and j==result[i].col:
                   self.res[i][j]=1
        print 'solution one:'
        print self.res
        print 'solution two:'
        print self.res[::-1]

    def doSolve(self,row,N,keeptrack):
        if row==N:
            return True
        for col in range(N):
            self.isSafe=True
            for queen in range(row):
                #if queen in same col
                if keeptrack[queen].col==col:
                    self.isSafe=False
                    break
                #top -> left diagonal attack check
                elif keeptrack[queen].row-keeptrack[queen].col==row-col:
                    self.isSafe=False
                    break
                #bottom->left diagonal attack check
                elif keeptrack[queen].row+keeptrack[queen].col==row+col:
                    self.isSafe=False
                    break
                    
            #if the place is safe to place queen
            if self.isSafe==True:
               keeptrack[row]=Nqueen(row,col)
               if self.doSolve(row+1,N,keeptrack)==True:
                  return True
        return False
    
if __name__=='__main__':
    t=time.time()
    nqueen=Nqueen(0,0)
    result=nqueen.solution(nqueen.N)
    nqueen.print_solution(result)
    print("Time required: "+str(time.time()-t))
