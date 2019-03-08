#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:13:46 2018

@author: koushikahamed
"""
romania_map ={
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia":70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia":75, "Craiova":120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesti": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesti": 97, "Sibiu":80},
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest":211},
    "Pitesti": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesti": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}
}
heuristic_list={'Arad':366,'Bucharest':0,'Craiova':160,'Dobreta':242,'Eforie':161,'Fagaras':178,
                'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,'Mehadia':241,'Neamt':234,
                'Oradea':380,'Pitesti':98,'RimnicuVilcea':193,'Sibiu':253,'Timisoara':329,
                'Urziceni':80,'Vaslui':199,'Zerind':374}
class RomanianMap:
    
    def __init__(self):
        pass
    def romania(self):
        return romania_map
    def heuristic(self):
        return heuristic_list
