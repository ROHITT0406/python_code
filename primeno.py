def isprime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
            break
        
    if count==1:
        print(f"Number {n} is not prime")
    else:
        print(f"Number {n} is prime")            
 
n=int(input("enter a Number"))
isprime(n)

    