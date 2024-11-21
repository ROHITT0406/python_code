class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print( (22/7) * self.radius**2)
        
    
    def perimeter(self):
        print( 2 * (22/7)* self.radius) 
c=circle(4)
c.area()
c.perimeter()     