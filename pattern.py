# basics for pattern
#n=5
#for i in range(n):
#    for j in range(n):
#        print('*',end=' ')
#    print()
"""* * * * * * * * * 
    * * * * * * * 
      * * * * *
        * * *
          *"""
n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()
