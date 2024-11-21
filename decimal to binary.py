def binary(n):
    l=[]
    if n < 1:
        return 
    else:
        while(n!=0):
            a= n % 2
            l.append(str(a))
            n= n // 
    l=l[::-1]
    return " ".join(l)
n=int(input("enter a number"))
print(binary(n))  
        
        