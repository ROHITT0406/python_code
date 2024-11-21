class bank:
    def __init__(self):
        self.customer={}
        
    def create_account(self,accountno,balance=0):
        if accountno in self.customer:
            print("Account already exist")
        else:
            self.customer[accountno]=balance
            print("Account successsfully created")
    def withdrwals(self,accountno,amount):
        if accountno in self.customer:
            if self.customer[accountno]>=amount:
                self.customer[accountno]-=amount
                print("Rs",amount,"amount has debited")
            else:
                print("insufficient fund")    
        else:
            print("Account does not exist")
    def make_depoist(self,accountno,amount):
        if accountno in self.customer: 
            self.customer[accountno]+=amount
            print("Rs",amount,"amount was credited")
        else:
            print("Account does not exist")
    def get_balance(self,accountno):
        if accountno in self.customer:
            balance=self.customer[accountno]
            print(f"Balance is {balance }")
        else:
            print("Account no does not exist")
bank=bank()
bank.create_account(10000,1241412)
bank.make_depoist(10000,1241241241)
bank.withdrwals(10000,2141431)
bank.get_balance(100001) 
bank.create_account(100001,1241412)
bank.make_depoist(100001,1241241241)
bank.withdrwals(100001,2141431)
bank.get_balance(100001) 
 