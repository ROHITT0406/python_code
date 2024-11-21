def min(x,y):
    if x>y:
        return y
    return x
def max(x,y):
    if x>y:
        return x
    return y
n1=int(input("Enter a number 1:-"))
n2=int(input("Enter a number 2:-"))
z=min(n1,n2)
q=max(n1,n2)
if q%z==0:
    print(f"gcd of {n1} and {n2} is {z}")
else:    
    gcd=1
    for i in range(1,z):
        if n1%i==0 and n2%i==0:
            gcd=i
    print(f"greatest factor of number {n1} and {n2} is",gcd)
    
        