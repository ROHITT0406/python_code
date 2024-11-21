def decimal(n):
    s=0
    i=0
    while (n != 0):
        d= n % 10
        s=s + d * 2**i
        n = n // 10
        i=i+1
    return s

print(decimal(100))
        