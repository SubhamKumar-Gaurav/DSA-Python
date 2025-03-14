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


## K closest element 
# Naive approach     Time: O(nk)
def kClosest(arr, x, k) : 
    for i in range(k) :
        mi=0 
        for i in range(1, len(arr)) : 
            if abs(arr[mi]-x) > abs(arr[i]-x) : 
                mi=i 
        print(arr[mi], end=" ") 
        arr.pop(mi) 
arr=[10,31,5,40, 38, 80]
x=35 
k=3
print("K closest elements (Naive) ")
kClosest(arr, x, k) 
print()

# Efficient approach 
def kClosestElements(arr, x, k) :
    n=len(arr) 
    h=[] 
    for i in range(k) : 
        heapq.heappush(h, (-abs(arr[i]-x), i))
    for i in range(k, n) : 
        curr=-abs(arr[i]-x) 
        p, pi = h[0] 
        if curr>p : 
            heapq.heappop(h) 
            heapq.heappush(h, (curr,i)) 
    while h : 
        p, pi = heapq.heappop(h) 
        print(arr[pi], end=" ")
arr=[30,40,32,33,36,37]
x=38 
k=3 
print("K closest elements (Efficient) ")
kClosestElements(arr, x, k) 
print("\n") 


## Merge K sorted arrays 
def mergeKsortedArr(arr) : 
    res=[] 
    h=[] 
    for i in range(len(arr)) : 
        heapq.heappush(h, (arr[i][0], i, 0)) 
    while h : 
        val, ap, vp = heapq.heappop(h) 
        res.append(val) 
        if vp+1<len(arr[ap]) :  
            heapq.heappush(h, (arr[ap][vp+1], ap, vp+1)) 
    return res 
arr=[[10,20], [5,15], [4,9,11]]
print("Merge K sorted array")
print(mergeKsortedArr(arr))
print("\n")



## Median of a stream
from heapq import heappush, heappop 
def streamMedian(arr) : 
    s=[]
    g=[] 
    for i in range(len(arr)) : 
        heappush(s, -arr[i]) 
        heappush(g, -heappop(s))
        if len(g)>len(s) : 
            heappush(s, -heappop(g)) 
        if len(g)<len(s) : 
            print(-s[0], end=" ") 
        else : 
            print((g[0]-s[0])/2, end=" ") 
print("Median of a stream")
arr=[25,7,10,15,20]
streamMedian(arr)