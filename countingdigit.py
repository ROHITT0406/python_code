n=int(input("enter a number"))
c=0
if n<0:
    n= (-1)*(n)
while(n>0):
    n=n//10
    c=c+1
print(f"The number of digit {c}")
