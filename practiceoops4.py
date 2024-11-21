class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,second):
        if self.price>second.price:
            return True
        else:
            return False
c=order("chips",20)
c1=order("frooty",30)
print(c>c1)