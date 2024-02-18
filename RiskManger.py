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
    isEligible: bool = True  # Corrected attribute name
    attendance: float = None
    moneyOwed: float = None
    isPledge: bool = None
    isBrother: bool = None
    isExec: bool = None
    onShitList: bool = False
    years: int = None
    isFormerExec: bool = None
        

def riskEligibility(person):
    if person.isFormerExec:
        person.isEligible = False
    elif person.years == 4:
        person.isEligible = False
    elif person.lastRisk >= 6:
        person.isEligible = True
    else:
        person.isEligible = False    

def shitList(person):
    if not person.isEligible:
        person.onShitList = False
    elif person.moneyOwed:
        person.onShitList = True
    elif person.gpa < 2.9:
        person.onShitList = True
    else:
        person.onShitList = False

def check_list(lst, value):
    return value in lst
  
def riskSelector(lst, party):
    execList = [x for x in lst if x.isExec]
    riskList = [x for x in lst if x.isEligible and x.onShitList]
    shitListList = [x for x in lst if x.onShitList and not check_list(riskList, x)]
    for _ in range(party):
        riskNumber = int(input("How many people do you want from the Exec List"))
        print(random.sample(execList, riskNumber))
        riskNumber = int(input("How many people do you want from the Risk List"))
        print(random.sample(riskList, riskNumber))
        riskNumber = int(input("How many people do you want from the Shit List"))
        print(random.sample(shitListList, riskNumber))




def test_shit_list():
    p1 = person(name="Alice", isEligible=True, moneyOwed=True, gpa=3.0)
    p2 = person(name="Bob", isEligible=False, moneyOwed=False, gpa=2.8)
    shitList(p1)
    shitList(p2)
    assert p1.onShitList
    assert not p2.onShitList

def test_check_list():
    lst = [1, 2, 3, 4, 5]
    assert check_list(lst, 3)
    assert not check_list(lst, 6)

def test_risk_selector():
    p1 = person(name="Alice", isExec=True, isEligible=True, onShitList=False)
    p2 = person(name="Bob", isExec=False, isEligible=True, onShitList=True)
    people = [p1, p2]
    riskSelector(people, 2)

if __name__ == "__main__":
   
    test_shit_list()
    test_check_list()
    test_risk_selector()
    print("All tests passed!")
