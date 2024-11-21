'''m,n=map(int,input("enter a number").split())
l=[]
for i in range(m):
    new_row=[]
    for j in range(n):
        val=int(input())
        new_row.append(val)
    l.appen1d(new_row)
print(l)'''
l=[[12,3,22],[12,3,42,35,3,4],[2,354,6,223,5]]
for i in range(len(l)):
    max=l[i][0]
    for j in range(len(l[i])):
        if l[i][j]>max:
            max=l[i][j]
    print(max,end=" ")

    