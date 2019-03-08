#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 23:38:34 2018

@author: koushikahamed
"""
import numpy as np

class puzzle:
    def __init__(self,start,goal,puzzleMap):
        self.puzzleMap=puzzleMap
        self.start=start
        self.goal=goal
        self.visited=np.zeros((1,9),dtype=bool)
        self.track={}
        self.result=[]
        
    def keep_track(self,child,parent):
        self.track[child]=parent
        
    def doSolve(self):
        path=[]
        path.append(self.start)
        self.visited[0][self.start]=True
        
        while path:
            extend=path.pop(0)
            if extend==self.goal:
                self.result.append(extend)
                while extend!=self.start:
                    self.result.append(self.track.get(extend))
                    extend=self.track.get(extend)
                break
            
            for child in self.puzzleMap[extend]:
                     if self.visited[0][child]==False:
                        self.keep_track(child,extend)
                        path.append(child)
                        self.visited[0][child]=True
                                                                        
if __name__=='__main__':
    puzzleMap={
               0:[1,3],1:[2,0],
               2:[1], 3:[0,4,6],
               4:[3,5,7],5:[4],
               6:[3],7:[4,8]
               }
    obj=puzzle(0,8,puzzleMap)
    obj.doSolve()
    print 'escaping path is:',obj.result[::-1]
        