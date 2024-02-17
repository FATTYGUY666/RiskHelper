import math
class person:
    def __init__(self,name, gpa, social, greekBill, riskCount, lastRisk, isEiligible, attendence, moneyOwed, isPlege, isBrother, isExec, isSenior, isFormerExec, programing, shitList, years):
        self.name = name
        self.gpa = gpa
        self.social = social
        self.greekBill = greekBill
        self.riskCount = riskCount
        self.lastRisk = lastRisk
        self.isEiligible = True
        self.attendence = attendence
        self.moneyOwed = moneyOwed
        self.isPlege = isPlege
        self.isBrother = isBrother
        self.isExec = isExec
        self.programing = programing
        self.shitList = shitList
        self.years = years

    def riskEligibility(self):
        
         if  self.isFormerExec == False:
             self.isEiligible = False
         if  self.years == 4:
             self.isEiligible = False

            

             
             
             


        