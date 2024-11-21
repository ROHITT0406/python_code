class student:
    def __init__(self,chem,maths,phy):
        self.chem=chem
        self.maths=maths
        self.phy=phy
    #@property
    def percentage(self):
        print((self.maths+self.chem+self.phy)//3)
       
c1=student(98,96,94)
c1.percentage
c1.phy=86
print(c1.phy)