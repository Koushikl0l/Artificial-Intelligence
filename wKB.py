#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:00:18 2018

@author: koushikahamed
"""
import numpy as np

kb=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],dtype=object)

case_conclusion=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],dtype=object)

kb_dict={kb[0]:[],kb[1]:['Breeze'],kb[2]:['Pit'],kb[3]:['Breeze'],
             kb[4]:['Stench'],kb[5]:[],kb[6]:['Breeze'],kb[7]:[],
             kb[8]:['Wumpus'],kb[9]:['Breeze','Stench','Gold'],kb[10]:['Pit'],kb[11]:['Breeze'],
             kb[12]:['Stench'],kb[13]:[],kb[14]:['Breeze'],kb[15]:['Pit']}

class KB:
    
    def __init__(self):
        pass    
    
    def access_kb(self):
        return kb_dict
        
    def access_case_conclusion(self):
        return case_conclusion
    
if __name__=='__main__':
    
    knowledgeBase=KB()
    
        