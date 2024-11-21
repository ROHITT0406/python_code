class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        #self.x=x
        #self.y=y
        #self.z=z
    def average(self):
        #sum=(self.x+self.y+self.z)/3
        sum=0
        for val in self.marks:
           sum += val
        print("hi",self.name,"your average marks is ",sum/3)
s1=student("rohit",[23,323,3234])
s1.average()