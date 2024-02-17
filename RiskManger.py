import math
class person:
    def __init__(self,name, gpa, social, greekBill, riskCount, lastRisk, isEiligible, attendence, moneyOwed, isPlege, isBrother, isExec, isSenior, isFormerExec):
        self.name = name
        self.gpa = gpa
        self.social = social
        self.greekBill = greekBill
        self.riskCount = riskCount
        self.lastRisk = lastRisk
        self.isEiligible = isEiligible
        self.attendence = attendence
        self.moneyOwed = moneyOwed
        self.isPlege = isPlege
        self.isBrother = isBrother
        self.isExec = isExec

    def riskEligibility(self):
        
         if self.isExec == False or self.isFormerExec == False:
             self.isEiligible = False
         else:
             if self.social == False or self.greekBill == False:
            

             
             
             


        