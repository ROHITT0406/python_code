 
def binarySearch(num,target,low,high):
    if low > high:
        return -1
    while low <= high:
        mid = (low+high)//2
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            return binarySearch(num,target,mid+1,high)
        else:
            return binarySearch(num,target,low,mid-1)
   
num = [10,29,1,3,6,7,2,5,7,7,4,2,1,3]
num.sort()
print(binarySearch(num,10,0,len(num)-1))
print(binarySearch(num,1,0,len(num)-1))