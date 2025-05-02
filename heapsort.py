import heapq
def heapsort(arr):
    heapq.heapify(arr)
    n=len(arr)
    new_Arr=[0]*n
    for i in range(n):
        minn=heapq.heappop(arr)
        new_Arr[i]=minn 
    return new_Arr

arr = [7,6,5,-1,2,2,35,45,3,3,5,2,6]
print(heapsort(arr))   