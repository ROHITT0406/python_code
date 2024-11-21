def reverse(i,arr,n):
    if (i > n//2):
        return
    temp=arr[i]
    arr[i]=arr[n-i-1]
    arr[n-i-1]=temp
    reverse(i+1,arr,n)
    
n=int(input("enter no of ele in array"))
arr=[]
print("add number of ele in array")
for i in range(n):
    val=int(input())
    arr.append(val)
print("Entered array",arr,end=" ")
reverse(0,arr,n) 
print()
print("Reversed array",arr)

