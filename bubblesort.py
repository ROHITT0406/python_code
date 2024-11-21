def bubble_sort(a,n):
    for i in range(n-1,0,-1):
       
        for j in range(0,i):
            if (a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=eval(input("enter a list"))
n=len(a)
#n=int(input("enter a number"))

'''for i in range(n):
    val=int(input())
    a.append(val)
print(a)'''

y=bubble_sort(a,n)
print("sorted list:")
print(y)
#h={}
#for c in a:
    #h[c]=h.get(c,0)+1
#print("occurenece of number in list")
#print(h)