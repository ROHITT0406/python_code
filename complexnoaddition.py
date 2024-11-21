class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def print(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,second):
        newreal= self.real + second.real
        newimg = self.img  + second.img 
        #print(self.real,"i +",self.img,"j")
        return complex(newreal,newimg)
    def __sub__(self,second):
        newreal= self.real - second.real
        newimg = self.img  - second.img 
        #print(self.real,"i -",self.img,"j")
        return complex(newreal,newimg)
num1=complex(1,2)
num1.print()
num2=complex(4,3)
num2.print()
#num1.add(num2)
#num3=num1-num2
num3=num1+num2
num3.print()