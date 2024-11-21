s=input("Enter a string")
lower=0
upper=0
space=0
digit=0
symbols=0

for i in range(len(s)):
    if s[i].isupper():
        upper+=1
    elif s[i].islower():
        lower+=1
    elif s[i]==" ":
        space+=1
    elif s[i].isdigit():
        digit+=1
    elif s[i]=="@" or s[i]=="?" or s[i]=="/" or s[i]==">" or s[i]=="<" or s[i]=="*" or s[i]=="+"  or s[i]=="-":
        symbols+=1        
print("Number of lowercase letter are:-",lower)
print("Number of uppercase letter are:-",upper)
print("Number of space letter are:-",space)
print("Number of digit are:-",digit)
print("Number of symbols are:-",symbols)