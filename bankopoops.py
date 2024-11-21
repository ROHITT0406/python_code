class Account:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.accountno=accountno
    def debit(self,amount):
        self.balance=self.balance-amount
        print("Rs",amount,"amount has debited")
        print("Total balance",self.get_balance())
    def credit(self,amount):
        self.balance=self.balance+amount
        print("Rs",amount,"amount was credited")
        print("Total balance",self.get_balance())
    def get_balance(self):
        return self.balance
a=Account(10000,12314141)
a.credit(100)
a.debit(1000)   