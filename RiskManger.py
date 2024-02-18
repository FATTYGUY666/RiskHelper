import math
from dataclasses import dataclass
import random 
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
          person.shitList = True
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
             execList.append(x);
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
    



def test_risk_eligibility():
    p1 = person(name="Alice", isFormerExec=True, years=2, lastRisk=7)
    p2 = person(name="Bob", isFormerExec=False, years=3, lastRisk=5)
    riskEligibility(p1)
    riskEligibility(p2)
    assert p1.isEiligible == False
    assert p2.isEiligible == True

def test_shit_list():
    p1 = person(name="Alice", isEiligible=True, moneyOwed=True, gpa=3.0)
    p2 = person(name="Bob", isEiligible=False, moneyOwed=False, gpa=2.8)
    shitList(p1)
    shitList(p2)
    assert p1.onShitList == True
    assert p2.onShitList == False

def test_check_list():
    lst = [1, 2, 3, 4, 5]
    assert check_list(lst, 3) == True
    assert check_list(lst, 6) == False

# Note: You may want to modify the test_risk_selector function as per your requirements.
def test_risk_selector():
    p1 = person(name="Alice", isExec=True, isEiligible=True, onShitList=False)
    p2 = person(name="Bob", isExec=False, isEiligible=True, onShitList=True)
    people = [p1, p2]
    riskSelector(people, 2)  # Adjust the party size according to the number of people available

if __name__ == "__main__":
    test_risk_eligibility()
    test_shit_list()
    test_check_list()
    test_risk_selector()
    print("All tests passed!")

 
        
    
     
             
             
             


        