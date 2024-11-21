def set_union(a1,a2): 
    a3=set()
    a4=set()
    a5=set()
    
    a3.update(a1)
    a4.update(a2)
    a3.update(a4)
    a5.update(a3)
    return a5 
def set_intersection(a1,a2): 
    a3=set()
    for i in a1:
        for j in a2:
            if i==j:
                a3.add(i)
    
    return a3
def set_difference(a1,a2):
    a3=set()
    a4=set()
    print("a-b ,b-a")     
    for i in a1:
        if i in a2:
            continue
        else:
            a3.add(i)
    for i in a2:
        if i in a1:
            continue
        else:
            a4.add(i)
    return a3,a4
   
a1=set()
a2=set()
n=int(input("How many element you want in set"))
for i in range(1,n+1):
    val=int(input("enter element of first set"))
    a1.add(val)
print(a1) 
for i in range(1,n+1):
    val=int(input("enter element of second set"))
    a2.add(val)
print(a2)
print("Union of two set is:-",set_union(a1,a2))
print("Intersection of two set is:-",set_intersection(a1,a2))
print("Set difference of sets (a-b,b-a) is:_",set_difference(a1,a2))


