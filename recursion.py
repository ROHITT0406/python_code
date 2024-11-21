def f(i,n):
    if (i>n):
        return
    print(i)
    f(i+1,n)
    
n=int(input("enter a number"))
f(1,n)
#to print N to 1 using backtrack then i=1, if condition ==> i>n ,f(i+1,n)
#to print 1 to N using backtrack then i=n, if condition ==> i<1 ,f(i-1,n)
# to print 1 to N using recursion then i=1,if condition ==> i>n ,f(i+1,n)
# to print N to 1 using recursion then i=n,if condition ==> i<1 ,f(i-1,n)    