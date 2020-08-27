import random
from abc import ABCMeta, abstractmethod

class Acc(metaclass = ABCMeta):
    @abstractmethod
    def create_account(self, Name, init_Deposite):
        return 0

    @abstractmethod
    def authenticate(self, Name, Acc_No):
        return 0

    @abstractmethod
    def withdrawal(self, withdrawal_Amt):
        return 0

    @abstractmethod
    def deposite(self,depo_amt):
        return 0

    @abstractmethod
    def display_avl_bal(self):
        return 0

class Current_Saving_Acc(Acc):

    def __init__(self):
        self.Savings_Acc={}

    def create_account(self, Name, init_Deposite):
        self.acc_num= random.randint(10000, 99999)
        self.Savings_Acc[self.acc_num] = [Name, init_Deposite]
        print("Account is Successfully created. Account Number:", self.acc_num)

    def authenticate(self, Name, Acc_No):
        if acc_num in self.Savings_Acc.keys():
            if self.Savings_Acc[acc_num][0] == Name:
                print("Aunthentication Successfull")
                return True
            else:
                print("Aunthentication Failed")

                return False
        else:
            print("Aunthentication Failed")
            return False

    def withdrawal(self, withdrawal_Amt):
        if withdrawal_Amt > self.Savings_Acc[self.acc_num][1]:
            print("Insufficient Balance")
        else:
            self.Savings_Acc[self.acc_num][1] -= withdrawal_Amt
            print("Withdrawal Successfull. ")
            self.display_avl_bal()


    def deposite(self,depo_amt):
        self.Savings_Acc[self.acc_num][1] += depo_amt
        print("Deposite Successfull.")
        self.display_avl_bal()

    def display_avl_bal(self):
        print("Available Balance:", self.Savings_Acc[self.acc_num][1])


Savings = Current_Saving_Acc()

while True:
    print ("Enter 1 to create a new account")
    print ("Enter 2 to access an existing account")
    print ("Enter 3 to exit")
    Choice = int(input())
    if Choice == 1:
        print("Name:")
        Name=input()
        print("Initial Depsite:")
        Init_Deposite=int(input())
        Savings.create_account(Name,Init_Deposite)

    elif Choice == 2:
        print("Name:")
        Name=input()
        print("Account Number:")
        acc_num=int(input())
        auth_result=Savings.authenticate(Name,acc_num)
        if auth_result is True:
            while True:
                print("Enter 1 for withdrawal")
                print("Enter 2 for deposite")
                print("Enter 3 to display available balance")
                Opt= int(input())
                if Opt == 1:
                    WD_Amt=int(input("Withdrawal Amount:"))
                    Savings.withdrawal(WD_Amt)
                elif Opt == 2:
                    D_Amt=int(input("Deposite Amount:"))
                    Savings.deposite(D_Amt)
                elif Opt == 3:
                    Savings.display_avl_bal()
                else:
                    print("Invalid Number!!")
                    continue
        else:
            continue
    else:
        exit()
