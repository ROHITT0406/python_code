m,n=map(int,input("enter a string").split())
#1m=int(dimensions[0])
#n=int(dimensions[1])
print(m,n)
l=[]
#list_1dform=[int(i) for i in input().split()]
for i in range(m):
    #new_row=list_1dform[i*n:(i+1)*n]
    
    
    new_row=[int(ele) for ele in input("enter value").split()]
    #new_row=[]
    #for j in range(n):
    #    ele=int(input("enter value"))
    #    new_row.append(ele)
    l.append(new_row)
print(l)
    