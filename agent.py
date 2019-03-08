import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__) #'%s'%(__name__)
   
    
class Agent(Object):
    def __init__(self):

        def program(percept): #abstract

            self.program=program


def traceAgent(agent):
    old_program=agent.program
    def new_program(percept):
        action=old_program(percept)
        print('%s perceives %s and does %s')%(agent,percept,action)
        return action

    
    agent.program=new_program    
    return agent



class tableDrivenAgent(Agent):

    def __init__(self,table):
        Agent.__init__(self)
        percepts=[]

        def program(percept):
            percepts.append(percept)
            action=table.get(tuple(percepts))
            print('Agent perceives ',percept,' and does ', action)
            return action

        self.program=program


loc_A,loc_B=(0,0,'A'),(1,0,'B')

def tableDrivenVaccumAgent():
    table = {
              ((loc_A,'Clean'),):'Right',
              ((loc_A,'Dirty'),):'Suck',
              ((loc_B,'Clean'),):'Left',
              ((loc_B,'Dirty'),):'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
            }
    return tableDrivenAgent(table)

    
class vaccumEnvironment():

    def __init__(self):
        self.status={ loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty'])
                      }
    def add_object(self,object,location=None):
        object.location=location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action=='Right': agent.location=loc_B
        elif action=='Left': agent.location=loc_A
        elif action=='Suck':
            #if self.status[agent.location]=='Dirty'
            self.status[agent.location]='Clean'

    


a=tableDrivenVaccumAgent()
e=vaccumEnvironment()
e.add_object(a)

p=e.percept(a)
action=a.program(p)
e.execute_action(a,action)

   
    














