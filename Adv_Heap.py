# Adv Heap 
#   Sort K Sorted Array 
#   Purchase maximum items 
#   K Largest items 
#   K closest elements 
#   Merge K sorted arrays 
#   Median of a stream 


## Sort K Sorted Array   
# PS: arr[i] is present in range of [i-k to i+k] (in sorted form)
import heapq
def sortK(arr, k) : 
    n=len(arr)
    pq=arr[:k+1] 
    heapq.heapify(pq)
    index=0 
    for i in range(k+1, n) :
        arr[index]=heapq.heappop(pq)
        index+=1 
        heapq.heappush(pq, arr[i]) 
    while pq : 
        arr[index]=heapq.heappop(pq) 
        index+=1 
    return arr 
print("Sort K sorted array : ")
arr=[10,9,7,8,4,30,50,60]
k=4
print(sortK(arr, k))
print("\n") 