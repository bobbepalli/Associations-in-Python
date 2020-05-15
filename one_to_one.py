class Account:
    def __init__(self,AccNo,AccHolderName,AccType,balance):
        self.AccNo=AccNo
        self.AccHolderName=AccHolderName
        self.AccType=AccType
        self.balance=balance

class Employee:
    def __init__(self,eno,ename,esal,account):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.account=account

    def GetAccountDetails(self):
        print("Employee Details")
        print("--------------------------")
        print("Employee No     :",self.eno)
        print("Employee Name   :",self.ename)
        print("Employee Salary :",self.esal)
        print()
        print("Account Details")
        print("--------------------------")
        print("Account No          :",self.account.AccNo)
        print("Account Holder Name :",self.account.AccHolderName)
        print("Account Type        :",self.account.AccType)
        print("Account Balance     :",self.account.balance)
a=Account(62316929320,"Bobbepalli Siva Sai","Savings",5000)
emp=Employee(488,"B Siva Sai",50000,a)
emp.GetAccountDetails()