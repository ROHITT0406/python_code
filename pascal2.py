def ncr(n):
    l=[]
    ans=1
    l.append(ans)
    for i in range(1,n):
        ans=ans*(n-i)
        ans=ans/i
        l.append(int(ans))
    return l
N=int(input("enter the number of rows"))
pascal=[]
for i in range(1,N+1):
    pascal.append(ncr(i))
print(pascal)