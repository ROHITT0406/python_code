def insertion_sort(a,n):
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if(a[j]<a[mini]):
                mini=j
                a[mini],a[i]=a[i],a[mini]
    return a
        
a=[]
 
n=int(input("enter a number"))
for i in range(n):
    val=int(input())
    a.append(val)
print(a)
y=insertion_sort(a,n)
print(y)