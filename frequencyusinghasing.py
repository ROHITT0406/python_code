a=[]
n=int(input("ENter a number:-"))
for i in range(n):
    val=int(input())
    a.append(val)
print(a)
#q=int(input("Enter a number you want to search"))
'''w=[]
for i in range(q):
    num=int(input())
    w.append(num)5
print(w)'''
h={}
for c in a:
    #if c in w:
    h[c]=h.get(c,0)+1
print(h)
#using function
'''def freq(a,b):
    f={}
    for i in a:
        if i in b: 
            f[i]=f.get(i,0)+1
    return f
a=[1,2,2,3,4,4,5]
b=[1,2,3]
y=freq(a,b)'''