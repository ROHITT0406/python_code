def isPalindrome(x):
    if (x<0):
        return False
    rev=0 
    i=x      
    while(i>0):
        digit=i % 10
        rev=rev * 10 + digit
        i = i / 10
    if (rev==i):
        return True
    return False
                
x=int(input("enter a number"))
y=isPalindrome(x)
print(y)