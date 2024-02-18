import math
from dataclasses import dataclass
import random 
@dataclass
class person:
    
        name: str = None
        gpa: float = 0
        social: str = None
        greekBill: bool = None 
        riskCount: int = None
        lastRisk: int = None
        isEiligible: bool = True
        attendence: float = None
        moneyOwed: float = None
        isPlege: bool = None
        isBrother: bool = None
        isExec: bool = None
        onShitList: bool = False
        years: int = None
        isFormerExec: bool = None
        

def riskEligibility(person):
        
    if  person.isFormerExec == True:
        person.isEiligible = False
    if  person.years == 4:
        person.isEiligible = False
    if  person.lastRisk >= 6:
        person.isEiligible = True
    if  person.lastRisk < 6:
        person.isEiligible = False    

def shitList(person):
     if person.isEiligible == False:
          person.onShitList = False
     if person.moneyOwed == True:
          person.onShitList = True
     if person.gpa < 2.9:
          person.onShitList = True
     else:
        person.onShitList = False

def check_list(list, value):

  if value in list:

    return True

  else:

    return False
  
def riskSelector(list, party):
     execList = []
     riskList = []
     shitListList = []
     riskNumber = 0
     

     for x in list:
         if x.isExec == True:
             execList.append(x)
     for x in list:
        if x.isEiligible == True and x.onShitList == True:
            riskList.append(x)
     for x in list:
          if x.shitList == True and check_list(list, x) != True:
              list.append(x)
     for x in range(party):
        riskNumber = input("How many people do you want from the Exec List")
        print(random.sample(execList, riskNumber))
        riskNumber = input("How many people do you want from the Risk List")
        print(random.sample(riskList, riskNumber))
        riskNumber = input("How many people do you want from the Shit List")
        print(random.sample(shitListList, riskNumber))
    



    
    
        
    
     
             
             
             


        