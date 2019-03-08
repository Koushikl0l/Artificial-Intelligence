#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:57:03 2018

@author: koushikahamed
"""
from wKB import KB,kb
import random

class wumpus_world:
    #global variables strats here
    
    climbingOutwithGold=0
    fallIntoPitOrEaten=0
    eachStep=0
    useArrow=0
    arrowbox=1 
    perfomance_measure=0 #total cost of getting the goal and reach out if the cave cost 
    perception_set=set() #perception set is for break the  reursion ex:('Stench','Breeze','Gold')
    visitedlist=set() #visited list sign [v]
    OK_list=list() #ok list sign OK it means this  position is safe for you
    agent_knowledge_base={} #every single position agent got the perception and updates knowledge base
    agent_prediction={} #agent predicts that the position is not ok
    safe_position_list=list()
    child_parent={} #this condition is for backtracking
    backtrack_set=set()
    #global variables ends here

    def __init__(self,kb_dict,case_conclusion):
        self.kb_dict=kb_dict
        #self.agent_possible_path=agent_possible_path
        self.case_conclusion=case_conclusion
        
    def doIteration(self):
        pass
    
    def find_safe_adjacent_position(self,current_position):
      if current_position not in self.backtrack_set:
        self.backtrack_set.add(current_position)
        if (current_position-1>=0):
           if current_position-1 not in self.OK_list and self.agent_knowledge_base[current_position] == []:
               self.safe_position_list.append(current_position-1)
               self.OK_list.append(current_position-1)
                   
           if current_position-1 not in self.OK_list and 'Breeze' in self.agent_knowledge_base[current_position]:
               if self.agent_prediction[current_position-1]=='Wumpus':
                   self.safe_position_list.append(current_position-1)
                   self.OK_list.append(current_position-1)
                   self.agent_prediction[current_position-1]=[]      
               else: 
                  self.agent_prediction[current_position-1]='Pit' 
                  
           if current_position-1 not in self.OK_list and 'Stench' in self.agent_knowledge_base[current_position]:
               if  self.agent_prediction.get(current_position-1) is not None:
                   self.safe_position_list.append(current_position-1)
                   self.OK_list.append(current_position-1)
                   self.agent_prediction[current_position-1]=[]      
               else: 
                  self.agent_prediction[current_position-1]='Wumpus'
           
        if (current_position+1)<=15:
           if current_position+1 not in self.OK_list and self.agent_knowledge_base[current_position] ==[]:
               self.safe_position_list.append(current_position+1)
               self.OK_list.append(current_position+1)
               
           if current_position+1 not in self.OK_list and 'Breeze' in self.agent_knowledge_base[current_position]:
               if self.agent_prediction.get(current_position+1) is not None:
                   self.safe_position_list.append(current_position+1)
                   self.OK_list.append(current_position+1)
                   self.agent_prediction[current_position+1]=[]      
               else: 
                  self.agent_prediction[current_position+1]='Pit' 
          
           if current_position+1 not in self.OK_list and 'Stench' in self.agent_knowledge_base[current_position]:
               if self.agent_prediction.get(current_position+1) is not None:
                   self.safe_position_list.append(current_position+1)
                   self.OK_list.append(current_position+1)
                   self.agent_prediction[current_position+1]=[]      
               else: 
                  self.agent_prediction[current_position+1]='Wumpus'
                  
        if (current_position+4)<=15:
            if current_position+4 not in self.OK_list and self.agent_knowledge_base[current_position]==[]:
               self.safe_position_list.append(current_position+4)
               self.OK_list.append(current_position+4)
               
            if current_position+4 not in self.OK_list and 'Breeze' in self.agent_knowledge_base[current_position]:
               if self.agent_prediction.get(current_position+4) is not None:
                   self.safe_position_list.append(current_position+4)
                   self.OK_list.append(current_position+4)
                   self.agent_prediction[current_position+4]=[]      
               else: 
                  self.agent_prediction[current_position+4]='Pit' 
            
            if current_position+4 not in self.OK_list and 'Stench' in self.agent_knowledge_base[current_position]:
               if self.agent_prediction.get(current_position+4) is not None:
                   self.safe_position_list.append(current_position+4)
                   self.OK_list.append(current_position+4)
                   self.agent_prediction[current_position+4]=[]      
               else: 
                  self.agent_prediction[current_position+4]='Wumpus' 
                  
        if (current_position-4)>=0:
            if current_position-4 not in self.OK_list and self.agent_knowledge_base[current_position]==[]:
               self.safe_position_list.append(current_position-4)
               self.OK_list.append(current_position-4)
               
            if current_position-4 not in self.OK_list and 'Breeze' in self.agent_knowledge_base[current_position]:
               if self.agent_prediction[current_position-4]=='Wumpus':
                   self.safe_position_list.append(current_position-4)
                   self.OK_list.append(current_position-4)
                   self.agent_prediction[current_position-4]=[]      
               else: 
                  self.agent_prediction[current_position-4]='Pit' 
                  
            if current_position-4 not in self.OK_list and 'Stench' in self.agent_knowledge_base[current_position]:
               if self.agent_prediction[current_position-4]=='Pit':
                   self.safe_position_list.append(current_position-4)
                   self.OK_list.append(current_position-4)
                   self.agent_prediction[current_position-4]=[]      
               else: 
                  self.agent_prediction[current_position-4]='Wumpus'      
      else:
          if (current_position-1)>=0:
              if current_position-1  in self.OK_list and current_position-1 not in self.visitedlist:
                   self.safe_position_list.append(current_position-1)
                   self.OK_list.append(current_position-1)
          if (current_position+1)<=15:
              if current_position+1  in self.OK_list and current_position+1 not in self.visitedlist:
                   self.safe_position_list.append(current_position+1)
                   self.OK_list.append(current_position+1)
          if (current_position+4)<=15:
              if current_position+4  in self.OK_list and current_position+4 not in self.visitedlist:
                   self.safe_position_list.append(current_position+4)
                   self.OK_list.append(current_position+4)
          if (current_position-4)>=0:
              if current_position-4  in self.OK_list and current_position-4 not in self.visitedlist:
                   self.safe_position_list.append(current_position-4)
                   self.OK_list.append(current_position-4)
      return self.safe_position_list
    
    def backtracking_relation(self,parent,child):
        
           self.child_parent.update({child:parent})
           
    def doBacktrack(self,parent,agent_current_position):
           backtrackList=list()
           backtrackList.append(agent_current_position)
           while parent !=0:
               parent=self.child_parent.get(agent_current_position)
               backtrackList.append(parent)
               agent_current_position=parent
           return backtrackList
        
    def print_perfomance_measure(self):
           print('climbing out with glod:',(self.climbingOutwithGold))
           print('fallIntoPitOrEaten:',(self.fallIntoPitOrEaten))
           print('eachStep:',(self.eachStep))
           print('useArrow:',(self.useArrow))
           self.perfomance_measure=self.climbingOutwithGold+self.fallIntoPitOrEaten+self.eachStep+self.useArrow
           print('perfomance_measure:',(self.perfomance_measure)) #print perfomance measure
    def doOperation(self):
        current_position_perception_list=[]
        agent_current_position=0
        print agent_current_position
        self.OK_list.append(agent_current_position)
        self.agent_knowledge_base[agent_current_position]=current_position_perception_list
    
        while 'Gold' not in current_position_perception_list:
                  safe_position=self.find_safe_adjacent_position(agent_current_position)
                  parent=agent_current_position
                  if safe_position !=[]:
                      agent_current_position=random.choice(safe_position)
                      print agent_current_position
                      self.backtracking_relation(parent,agent_current_position)
                      self.visitedlist.add(agent_current_position)
                      current_position_perception_list=self.kb_dict[agent_current_position]
                      self.agent_knowledge_base[agent_current_position]=current_position_perception_list
                      self.eachStep-=1
                      if 'Wumpus'  in current_position_perception_list:
                          if  self.arrowbox!=0:
                              self.useArrow-=10
                              self.arrowbox=0
                          else:
                              self.fallIntoPitOrEaten-=1000
                          break
                      if 'Pit'  in current_position_perception_list:
                              self.fallIntoPitOrEaten-=1000
                      if 'Gold' in current_position_perception_list:
                          self.climbingOutwithGold+=1000
                          backtracklist=self.doBacktrack(parent,agent_current_position)
                          print('Backtrack List after getting gold to initial:'+str(backtracklist))
                      self.safe_position_list=[] #set the safe position list as empty list 
                  else:
                      agent_current_position=self.child_parent.get(agent_current_position)
                      print agent_current_position
                      self.eachStep-=1
                      self.visitedlist.add(agent_current_position)
        
if __name__=='__main__':
    classkb=KB()
    kb_dict=classkb.access_kb()
    #agent_possible_path=classkb.access_agent_possible_path()
    case_conclusion=classkb.access_case_conclusion()
    WW=wumpus_world(kb_dict,case_conclusion)
    WW.doOperation()
    WW.print_perfomance_measure()
