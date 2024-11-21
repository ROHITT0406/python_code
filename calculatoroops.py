class calculator:
    def add(self,a,b):
        return a + b 
    def sub(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b 
    def divide(self,a,b):
        if b != 0:
            return a / b
        else:
            print("cannot divide by 0")
c1=calculator()
print(c1.add(10,20))
print(c1.sub(10,20))
print(c1.divide(10,20))
print(c1.mul(10,20))

        