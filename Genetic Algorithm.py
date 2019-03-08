import math
import random
import matplotlib.pyplot as plt
class GA:
    def __init__(self,chromosomeList):
         self.chromosomeList=chromosomeList#initial chromosome list
         self.EvaluateFitness(self.chromosomeList)   
    def EvaluateFitness(self,chromosomeList):
        lst=list()
        self.cList=list()
        self.cList=chromosomeList
        for i in self.cList:
            lst.append(int(i,2))
        self.fitness(lst)
    
    def fitness(self,lst):
        listX=lst#access list of x
        fitX=list()# all chromose list using fitness
        for i in listX:
            fitX.append(i*i)
        self.reproduction(fitX)
    
    def reproduction(self,fitX):
        bestFitness=list()
        bestFitness=fitX
        die_off=min(bestFitness)
        bestFitness.remove(die_off)
        bestFitness.sort()
        max_val=max(bestFitness)
        new_production=list()
        for i in range(len(bestFitness)-1):
            new_production.append(bestFitness[i])
            new_production.append(max_val)
            
        self.crossover(new_production)
    
    def crossover(self,new_production):
      #do crossover using reproduction
      self.new_production=list()
      self.new_production=new_production
      binary_listof_new_production=list()
      for i in range(len(new_production)):
          for j in range(len(new_production)):
                
                if int(math.sqrt(new_production[i]))==int(self.cList[j],2):
                     binary_listof_new_production.append(self.cList[j])                  
      new_crossover_list=list()
      for i in range(len(new_production)/2):
        if i==0:
           temp0=binary_listof_new_production[0][-1]
           temp1=binary_listof_new_production[1][-1]
           prefix0=binary_listof_new_production[0][:len(binary_listof_new_production[0])-1]
           prefix1=binary_listof_new_production[1][:len(binary_listof_new_production[0])-1]
           newL0=prefix0+temp1
           newL1=prefix1+temp0
           new_crossover_list.append(newL0)
           new_crossover_list.append(newL1)
        if i==1:
           temp2=binary_listof_new_production[2][2:]
           temp3=binary_listof_new_production[3][2:]
           prefix2=binary_listof_new_production[2][:2]
           prefix3=binary_listof_new_production[3][:2]
           newL2=prefix2+temp3
           newL3=prefix3+temp2
           new_crossover_list.append(newL2)
           new_crossover_list.append(newL3)
      self.mutation(new_crossover_list)
   
    def mutation(self,new_crossover):
         new_crossover_list=list()
         mutation_list=list()
         new_crossover_list=new_crossover
         previous_genBinToInt=list()
         new_genBinToInt=list()
         for i in range(len(new_crossover_list)):
                rand=random.randint(0,4)
                if new_crossover_list[i][rand]=='1':
                    #new_choromosome=new_crossover_list[i].replace(new_crossover_list[i][rand],'0')
                    #mutation_list.append(new_choromosome)
                    prefix=new_crossover_list[i][:rand]
                    postfix=new_crossover_list[i][rand+1:]
                    new_choromosome=prefix+'0'+postfix
                    mutation_list.append(new_choromosome)
                else:
                    #new_choromosome=new_crossover_list[i].replace(new_crossover_list[i][rand],'1')
                    #mutation_list.append(new_choromosome)
                    prefix=new_crossover_list[i][:rand]
                    postfix=new_crossover_list[i][rand+1:]
                    new_choromosome=prefix+'1'+postfix
                    mutation_list.append(new_choromosome)
                    
         for i,j in zip(self.chromosomeList,mutation_list):
            previous_genBinToInt.append(int(i,2))
            new_genBinToInt.append(int(j,2))
         if sum(new_genBinToInt)>=sum(previous_genBinToInt) and sum(new_genBinToInt)/len(new_genBinToInt)>=\
         sum(previous_genBinToInt)/len(previous_genBinToInt) and max(new_genBinToInt)>=max(previous_genBinToInt):
             self.print_improvement(mutation_list)
         else:
             
             self.EvaluateFitness(mutation_list) #call fitness and send mutation_list
    def print_improvement(self,mutationList):
        mutation_list=list()
        x=[1,2]
        y=[4,5]
        z=[7,8]
        sum_list=list()
        avg_list=list()
        max_list=list()
        previous_genBinToInt=list()
        new_genBinToInt=list()
        mutation_list=mutationList
       
        for i,j in zip(self.chromosomeList,mutation_list):
            previous_genBinToInt.append(int(i,2))
            new_genBinToInt.append(int(j,2))
        print('previous gen:'+str(self.chromosomeList))
        print('new gen:'+str(mutation_list))
        for i in range(2):
            if i==0:
             sum_list.append(sum(previous_genBinToInt))
             avg_list.append(sum(previous_genBinToInt)/len(previous_genBinToInt))
             max_list.append(max(previous_genBinToInt))
            if i==1:
              sum_list.append(sum(new_genBinToInt))
              avg_list.append(sum(new_genBinToInt)/len(new_genBinToInt))
              max_list.append(max(new_genBinToInt))
        
        plt.bar(x,sum_list,label='sum',color='red')
        plt.bar(y,avg_list,label='avg',color='green')
        plt.bar(z,max_list,label='max',color='blue')
        
        plt.title('Genetic Algorithm-change Ratio')
        plt.legend()
        plt.show()
        self.drawpie_chart_prev(previous_genBinToInt)
        self.drawpie_chart_new(new_genBinToInt)
    def drawpie_chart_prev(self,previous_genBinToint):
        previous_genBinToInt=previous_genBinToint
        color=['red','green','magenta','cyan']
        percentage1=[previous_genBinToInt[0],previous_genBinToInt[1],previous_genBinToInt[2],previous_genBinToInt[3]]
        plt.pie(previous_genBinToInt,labels=percentage1,colors=color)
        plt.title('previous Generation')
        plt.legend()
        plt.show()
    def drawpie_chart_new(self,new_genBinToint):
        new_genBinToInt=new_genBinToint
        color=['red','green','magenta','cyan']
        percentage2=[new_genBinToInt[0],new_genBinToInt[1],new_genBinToInt[2],new_genBinToInt[3]]
        plt.pie(new_genBinToInt,labels=percentage2,colors=color)
        plt.title('New Generation')
        plt.legend()
        plt.show()
        
if __name__=='__main__':
   chromosomeList=['01000','01100','00100','10011']
   g=GA(chromosomeList)
   # g.findX()  #recursively calling so not need to call
   # g.fitness() #recursively calling so not need to call
   #g.reproduction() #recursively calling so not need to call
   #g.crossover() 

