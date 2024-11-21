def insertion_sort(a,n):
    for i in range(1,n):
        j=i
        while(a[j-1]>a[j] and j>0):
            a[j-1],a[j]=a[j],a[j-1]
            j-=1
    return a
a=[2,35,523,21,5,1,5,6]
n=len(a)
insertion_sort(a,n)
print(a)            