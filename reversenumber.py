def reverse(x):
    rev=0
    if(x<0):
        x=abs(x)
    while(x!=0):
       
        digit=(x%10)
            
        rev=(rev*10)+digit
        x = (x//10)
    return  -rev if(x<0) else rev
x=int(input("enter a number "))
y= reverse(x)
print(y)