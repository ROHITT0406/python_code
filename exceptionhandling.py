try:
    num=int(input("enter a number"))
    for i in range(1,11):
        print(f"{num}X {i} = {num*i}")
except ValueError:
    print("invalid input")
   