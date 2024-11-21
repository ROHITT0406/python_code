class parent():
    def __init__(self,x,y):
        self.x=x
        self.y=y
class child(parent):
    def __init__(self,x,y,a,b):
        super().__init__(x,y)
        self.a=a
        self.b=b
    def print(self):
        print(self.x)
        print(self.y)
        print(self.a)
        print(self.b)
c=child(1,2,3,4)
c.print()