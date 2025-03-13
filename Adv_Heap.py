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


## Purchase maximum items 
# Naive approach 
def purchase(cost, x) : 
    cost.sort() 
    res=0 
    for i in cost : 
        if i<=x : 
            res+=1 
            x-=i 
        else : 
            break 
    return res 
cost=[20,10,5,30,100]
x=35
print("Purchase maximum items (Naive) : ", purchase(cost, x))


# Effcient approach 
def purchaseMax(cost, x) : 
    pq=cost 
    heapq.heapify(pq) 
    res=0 
    for i in pq : 
        temp=heapq.heappop(pq) 
        if temp<=x : 
            res+=1 
            x-=temp 
        else : 
            break 
    return res 
print("Purchase maximum items (using Heap) :",purchaseMax(cost, x)) 
print("\n")


## K Largest items 
# PS: Print K largest elements (in increasing order) 
# Naive approach - sort array , print last k elements 

# Efficient approach 
def kLargestElements(arr, k) : 
    n=len(arr)
    pq=arr[:k]
    heapq.heapify(pq) 
    for i in range(k, n) :
        if pq[0]>arr[i] : 
            continue 
        else : 
            heapq.heappop(pq) 
            heapq.heappush(pq, arr[i]) 
    while pq : 
        print(heapq.heappop(pq), end=" ")
arr=[11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
k=4
print("K Largest elements :")
kLargestElements(arr, k)
print("\n")