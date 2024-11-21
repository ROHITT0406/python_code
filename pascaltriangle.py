def ncr(row,col):
    res=1
    col=col-1
    row=row-1
    for i in range(0,col):
        res=res*(row-i)
        res=res/(i+1)

    return int(res)

row=int(input("enter a number"))
col=int(input("enter a number"))
a=ncr(row,col)
print("the number is ",a)