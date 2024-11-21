def isPalindrome(i,s):
    s=s.lower()
    n=len(s)
    if (i> n//2):
        return True
    if (s[i]!=s[n-i-1]):
        return False
    return isPalindrome(i+1,s)
s=str(input("enter a string"))
isPalindrome(0,s)      
