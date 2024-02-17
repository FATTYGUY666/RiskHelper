import math
class person:
    def __init__(self,name, gpa, social, greekBill, riskCount, lastRisk, attendence, moneyOwed, isPlege, isBrother, isExec, isSenior, isFormerExec):
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

    def riskEligibility(self):
        
         if  self.isFormerExec == False:
             self.isEiligible = False

         if  self.isExec == False:
             self.isEiligible == True
        
            

             
             
             


        