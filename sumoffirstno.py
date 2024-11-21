#def f(i,sum):
#    if (i<1):
#        print(sum)
#       return
#
#    f(i-1,sum+i)
#n=int(input("enter a number"))
#f(n,0)

def sum(n):    
    if(n==0):
        return 0
    return n + sum(n-1)
n=int(input("enter a number"))
y=sum(n)
print(y)