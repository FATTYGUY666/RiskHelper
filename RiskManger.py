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
    execList = [x.name for x in lst if x.isExec]
    riskList = [x.name for x in lst if x.isEligible and x.onShitList]
    shitListList = [x.name for x in lst if x.onShitList and x.name not in riskList]
    for _ in range(party):
        while True:
            try:
                riskNumber = int(input("How many people do you want from the Exec List: "))
                if 0 <= riskNumber <= len(execList):
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and", len(execList))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        print(random.sample(execList, riskNumber))

        while True:
            try:
                riskNumber = int(input("How many people do you want from the Risk List: "))
                if 0 <= riskNumber <= len(riskList):
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and", len(riskList))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        print(random.sample(riskList, riskNumber))

        while True:
            try:
                riskNumber = int(input("How many people do you want from the Shit List: "))
                if 0 <= riskNumber <= len(shitListList):
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and", len(shitListList))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

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
    p3 = person(name="Alic", isExec=True, isEligible=True, onShitList=False)
    p4 = person(name="Bo", isExec=False, isEligible=True, onShitList=True)
    p5 = person(name="Ali", isExec=True, isEligible=True, onShitList=False)
    p6 = person(name="B", isExec=False, isEligible=True, onShitList=True)
    p7 = person(name="Al", isExec=True, isEligible=True, onShitList=False)
    p8 = person(name=" ", isExec=False, isEligible=True, onShitList=True)
    p9 = person(name="A", isExec=True, isEligible=True, onShitList=False)
    p10 = person(name="Bobbob", isExec=False, isEligible=True, onShitList=True)
    people = [p1, p2,p3,p4,p5,p6,p7,p8,p9,p10]
    riskSelector(people, 2)

if __name__ == "__main__":
   
    test_shit_list()
    test_check_list()
    test_risk_selector()
    print("All tests passed!")
