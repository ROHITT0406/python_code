class fraction:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print(self):
        print(self.x,"/",self.y)
    def normalize(self):
        min_value=min(self.x,self.y)
        while min_value>1:
            if self.x % min_value == 0 and self.y % min_value == 0:
                break
        self.x = self.x // min_value
        self.y = self.y // min_value
    def sub(self,second):
        up_x=(self.x*second*y) - (second.x*self.y)
        up_y=self.y*second.y 
        self.x=up_x
        self.y=up_y
        self.normalize() #to use different method in other method
f1=fraction(10,20)
f2=fraction(30,40)
f1.print()
