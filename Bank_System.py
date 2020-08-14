import random


class Current_Saving_Acc:

    def __init__(self, Name, Deposite):
        self.Name=Name
        self.Deposite=Deposite

    def Acc_No(self):
        self.Acc_No= random.random()
        print(self.Acc_No)


CObj = Current_Saving_Acc('Anna',500)
print(CObj.Name,CObj.Deposite)
CObj.Acc_No()
