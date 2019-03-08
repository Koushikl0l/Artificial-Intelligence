 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 08:44:39 2018

@author: koushikahamed
"""
from R import RomanianMap
from queue import Queue
import time

class GraphProblem(object):

    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        self.initial=initial
        self.goal=goal
        self.graph = graph

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def goal_test(self,state):
        return state==self.goal    

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph[A][B] or self.infinity)

class Node:

    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node.  Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return list(self.child_node(problem, action)for action in problem.actions(self.state))

    def child_node(self, problem, action):
        """[Figure 3.10]"""  
        next = problem.result(self.state, action)
        pathCost=problem.path_cost(self.path_cost, self.state,action, next)
        return Node(next, self, action,pathCost)

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return list(node.state for node in self.path())
       #return list(node.state for node in self.path()[0:])
    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back =self, []
        while node:
            path_back.append(node)
            node = node.parent
            
        return list(reversed(path_back))
 
def breadth_first_search(problem):
    """[Figure 3.11]"""    
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = Queue()
    #frontier=list()
    frontier.append(node)        
    explored = set() 
    while frontier:
        node = frontier.pop()
        explored.add(node.state) 
        for child in node.expand(problem):
            if child.state not in explored and child.state not in frontier.data:
            #if child.state not in explored and child.state not in frontier:                 
                if problem.goal_test(child.state):return child
                frontier.append(child)
                          
    return None


Romania=RomanianMap() 
t=time.time()
gp=GraphProblem("Arad","Bucharest",Romania.romania())

result=breadth_first_search(gp)
print result.solution(),result.path_cost
print "time taken:",time.time()-t



