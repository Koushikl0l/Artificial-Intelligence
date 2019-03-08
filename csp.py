#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 21:44:34 2018

@author: koushikahamed
"""
from __future__ import print_function
import operator
import time

class csp:
    def __init__(self,aus_map,domain):
         self.domain=domain
         self.aus_map=aus_map
         self.domain_variable_dict={}
         
    def find_degree(self):
           keys=[self.aus_map.keys()]
           mapofdegree={}
           for  i in range(len(self.aus_map.keys())):
               degree=len(self.aus_map.get(keys[0][i]))
               mapofdegree[keys[0][i]]=degree     
           return mapofdegree
       
    def setDomain(self):
        self.keys=[self.aus_map.keys()]
        self.domain_variable_dict={}
        for i in range(len(self.aus_map.keys())):
            self.domain_variable_dict[self.keys[0][i]]=self.domain[i]
            
    def keys_accordingToDegree(self,mapOfDegree):
        sorted_x = sorted(mapOfDegree.items(), key=operator.itemgetter(1),reverse=True)
        return map(lambda a:a[0],sorted_x)
    
    def doIterAndUpdate(self,key):
        adjacent_node=self.aus_map.get(key)
        parent_key_domain=self.domain_variable_dict.get(key)  
        for i in range(len(adjacent_node)):
            length=len(self.domain_variable_dict.get(adjacent_node[i]))
            if length>1:
                child_key_domain=self.domain_variable_dict.get(adjacent_node[i])
                for index,j in enumerate(child_key_domain):
                    if parent_key_domain[0]==j:
                        child_key_domain.pop(index)
                        self.domain_variable_dict.update({adjacent_node[i]:child_key_domain})
             
        
    def doSolve(self,mapOfDegree,key):
        list_keys=self.keys_accordingToDegree(mapOfDegree)
        if key>=len(list_keys):
            return True
        if key==0:
            domain_list=self.domain_variable_dict.get(list_keys[key])
            domain_list=[domain_list[0]]
            self.domain_variable_dict.update({list_keys[key]:domain_list})
            self.doIterAndUpdate(list_keys[key]) 
        else:
            
            domain_list=self.domain_variable_dict.get(list_keys[key])
            #if len(domain_list)!=1:
            domain_list=[domain_list[0]]
            self.domain_variable_dict.update({list_keys[key]:domain_list})
            self.doIterAndUpdate(list_keys[key])

        self.doSolve(mapOfDegree,key+1)    
if __name__=='__main__':
    t=time.time()
    aus_map={'sa':['nt','wa','q','nsw','v'],'q':['nt','nsw','sa'],'nsw':['q','v','sa'],'nt':['wa','q','sa'],'wa':['nt','sa'],'v':['sa','nsw'],'t':[]}
    domain=[['R','G','B'],['R','G','B'],['R','G','B'],['R','G','B'],['R','G','B'],['R','G','B'],['R','G','B']]
    gp=csp(aus_map,domain)
    mapOfDegree=gp.find_degree()
    gp.setDomain()
    gp.doSolve(mapOfDegree,key=0)
    print(gp.domain_variable_dict)
    print("Time taken:",time.time()-t)
    
