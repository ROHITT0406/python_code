class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.salary=salary
        self.department=department
    def showdetails(self):
        print("Role==>",self.role)
        print("Department==>",self.department)
        print("salary==>",self.salary)
class engineer(employee):
    def __init__(self,role,department,salary,name,age):
        super().__init__(role,department,salary)
        #super().__init__("salesman","market","60,000")
        self.name=name
        self.age=age
    def print(self):
        super().showdetails()
        print("Name==>",self.name)
        print("Age==>",self.age)
engi1=engineer("salesman","market","60,000","rohit",21)    
engi1.showdetails
engi1.print()        