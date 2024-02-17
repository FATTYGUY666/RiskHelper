import math
from dataclasses import dataclass
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
        shitList: bool = False
        years: int = None
        isFormerExec: bool = None

def riskEligibility(self):
        
    if  person.isFormerExec == False:
        person.isEiligible = False
    if  person.years == 4:
        person.isEiligible = False
    if  person.lastRisk >= 6:
        person.isEiligible = True
    if  person.lastRisk < 6:
        person.isEiligible = False    

def shitList(self):
     if person.moneyOwed == True:
          person.shitList = True
     if person.gpa < 2.9:
          person.shitList = True
     if person.isEiligible == False:
          person.shitList = False

def notShitList(self):
     if person.gpa >=2.9 & person.moneyOwed == False:
          person.shitList = False
            

             
             
             


        