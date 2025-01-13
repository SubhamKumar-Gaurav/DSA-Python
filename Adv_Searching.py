## Advanced searching 
#    Search in an Infinite sized array 
#    Search in sorted rotated array 
#    Find a Peak element 
#    Count occurences in a sorted array 
#    Two Pointers approach 
#    Triplet in a sorted array
#    Median of two sorted arrays 
#    Repeating element  (Part-1) 
#    Repeating element  (Part-2) 


## Search in an Infinite sized array  
## 1. Naive Approach 
def searchInfy1(arr,x) :
    i=0 
    while True : 
        if arr[i]==x : 
            return i 
        elif arr[i]>x : 
            return -1 
        i+=1 


## 2. Efficient approach 
def bSearch(arr,l,r,x) : 
    while l<=r : 
        mid=(l+r)//2 
        if arr[mid]==x : 
            return mid 
        elif arr[mid]<x : 
            l=mid+1 
        else : 
            r=mid-1 
    return -1 

def searchInfy2(arr,x) : 
    if arr[0]==x : 
        return 0 
    i=1 
    while arr[i]<x : 
        i=i*2 
    if arr[i]==x : 
        return i 
    return bSearch(arr,i//2,i-1,x) 
arr=[1,10,15,20,40,80,90,100,120,500,600,700,1000]
x=100 
print("Search in infinite arr (Efficient) : ",searchInfy2(arr,x)) 
print("\n") 



## Search in sorted rotated array 
# 1. Naive approach: Linear Search 

# 2. Efficient approach 
def searchSortRot(arr,x) : 
    n=len(arr)  
    low=0 
    high=n-1  
    while low<=high : 
        mid=(low+high)//2 
        if arr[mid]==x : 
            return mid 
        if arr[low]<arr[mid] : 
            if arr[low] <= x < arr[mid] : 
                high=mid-1 
            else : 
                low=mid+1 
        else : 
            if arr[mid] < x <= arr[high] : 
                low=mid+1 
            else : 
                high=mid-1 
    return -1 
arr=[10,20,30,40,50,8,9] 
x=30 
print("Search in sorted rotated array : ",searchSortRot(arr,x))
print("\n") 



## Find a Peak element 
# 1. Naive approach 
def getPeak1(arr) : 
    n=len(arr) 
    if n==1 : 
        return arr[0] 
    if arr[0]>arr[1] : 
        return arr[0] 
    if arr[n-1]>arr[n-2] : 
        return arr[n-1]
    for i in range(1,n-1) : 
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1] : 
            return arr[i]
arr=[5,10,20,15,7]
print("Get peak element: Naive ")
print("[5,10,20,15,7] : ",getPeak1(arr))
print("\n") 
 
# 2. Efficient approach 
def getPeak2(arr) : 
    n=len(arr)
    low=0 
    high=n-1 
    while low<=high : 
        mid=(low+high)//2 
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid]) : 
            return arr[mid] 
        if mid>0 and arr[mid-1]>=arr[mid] : 
            high=mid-1 
        else : 
            low=mid+1 
    return -1 
arr=[5,20,40,30,20,50,60]
print("[5,20,40,30,20,50,60] : ",getPeak2(arr)) 
print("\n") 


## Count occurences in a sorted array 
# 1. Naive approach (Linear traversal) 
# 2. Simple Binary search and then linear traversal for same element. O(log n) + O(n) (Worst case)
# 3. Best approach : last_occurence - first_occurence + 1   O(log n)


## Two Pointers approach 
# Find if arr[i]+arr[j] == x   (i!=j)
# 1. Naive approach : O(n^2)
# 2. Using Two pointer approach : O(n)
print("Two Pointers approach ")
def isPair(arr,x) : 
    i=0 
    j=len(arr)-1 
    while i<j : 
        pairSum=arr[i]+arr[j] 
        if pairSum==x : 
            return True 
        elif pairSum<x : 
            i=i+1 
        else : 
            j=j-1 
    return False 
arr=[2,5,8,12,30]
x=17
print("[2,5,8,12,30] : ", isPair(arr,x))
print("\n") 


## Triplet in a sorted array   (arr[i]+arr[j]+arr[k])==x 
# 1. Naive approach : O(n^3) 
# 2. Using two pointer : O(n^2)  
print("Triplet in a sorted array ")
def isPair(arr,x,si) : 
    i=si   # starting index (i+1)  
    j=len(arr)-1 
    while i<j : 
        pairSum=arr[i]+arr[j] 
        if pairSum==x : 
            return True 
        elif pairSum<x : 
            i=i+1 
        else : 
            j=j-1 
    return False 

def isTriplet(arr,x) : 
    n=len(arr)
    for i in range(n-2) : 
        if isPair(arr,x-arr[i],i+1) : 
            return True 
    return False 
arr=[2,3,4,8,9,20,40]
x=32
print("[2,3,4,8,9,20,40] : ", isTriplet(arr,x))
print("\n") 



## Median of two sorted arrays 
# Naive approach : O(n*log(n))  where [n = len(arr1)+len(arr2)] 
# Efficient approach (Binary Search) 
def getMedian(a1,a2) : 
    def bSearchMedian(arr) : 
        n=len(arr) 
        if n%2==0 : 
            return (arr[n//2]+arr[n//2 -1])/2 
        else : 
            return arr[n//2]

    n1=len(a1)
    n2=len(a2) 

    # Check if one of the arrays is empty 
    if n1==0 and n2!=0 : 
        return bSearchMedian(a2) 
    elif n2==0 and n1!=0 : 
        return bSearchMedian(a1) 

    # Set arr1 as smaller array 
    if n2<n1 : 
        a1, a2 = a2, a1 
        n2, n1 = n1, n2 

    b1, e1 = 0, n1 
    while b1<=e1 : 
        i1=(b1+e1)//2 
        i2=(n1+n2+1)//2 - i1  
        mnr1 = float('inf') if i1==n1 else a1[i1] 
        mxl1 = float('-inf') if i1==0 else a1[i1-1] 
        mnr2 = float('inf') if i2==n2 else a2[i2] 
        mxl2 = float('-inf') if i2==0 else a2[i2-1] 
        if mxl1<=mnr2 and mxl2<=mnr1 : 
            if (n1+n2)%2==0 : 
                return (max(mxl1,mxl2)+min(mnr1,mnr2))//2 
            else : 
                return max(mxl1,mxl2) 
        elif mxl1>mnr2 : 
            e1 = i1 - 1
        else :     # mxl2>mnr1 
            b1 = i1 + 1 


## Repeating element (Part-1) 
# 1. Super Naive     Time : O(n^2) , Space: O(1)
def repeat(arr) : 
    n=len(arr) 
    for i in range(n-1) : 
        for j in range(i+1,n) : 
            if arr[i]==arr[j] : 
                return arr[j] 

# 2. Naive      Time : O(n logn),   Space: O(1)
def repeat(arr) : 
    n=len(arr)
    arr.sort()
    for i in range(n-1) : 
        if arr[i]==arr[i+1] : 
            return arr[i] 

# 3. Efficient :   Time: O(n) , Space: O(n) 
def repeat(arr) : 
    n=len(arr) 
    visit=[False]*n 
    for i in range(n) : 
        if visit[arr[i]] :  
            return arr[i] 
        arr[i]=True 
    return -1 


## Repeating element  (Part-2)  
print("Repeating element - II ")
print("For elements from 1 to max(arr)")
def repeat(arr) : 
    slow=arr[0]
    fast=arr[0]
    slow=arr[slow]
    fast=arr[arr[fast]]
    while slow!=fast : 
        slow=arr[slow]
        fast=arr[arr[fast]]
    slow=arr[0]
    while slow!=fast : 
        slow=arr[slow]
        fast=arr[fast]
    return slow 
arr=[1,3,2,4,6,5,7,3]
print("[1,3,2,4,6,5,7,3] : ",repeat(arr))
print("\n") 

# For elements from 0 to max(arr)
def repeat1(arr) : 
    slow=arr[0]+1 
    fast=arr[0]+1 
    slow=arr[slow]+1 
    fast=arr[arr[fast]+1] 
    while slow!=fast : 
        slow=arr[slow]+1 
        fast=arr[arr[fast]+1] 
    slow=arr[0]+1 
    while slow!=fast : 
        slow=arr[slow]+1 
        fast=arr[fast]+1 
    return slow-1 


## Allocate min no. of pages 
print("Allocate min no. of pages") 
print("Recursive solution")
def minPages(arr,n,k) : 
    if k==1 : 
        return sum(arr[0:n]) 
    if n==1 : 
        return arr[0] 
    res=float("inf") 
    for i in range(1,n) : 
        res=min(res,max(minPages(arr,i,k-1),sum(arr[i:n]))) 
    return res 
arr=[10,20,30,40]
k=2 
print("[10,20,30,40] : ",minPages(arr,4,k)) 
print("\n") 

print("using Binary Search") 
def isFeasible(arr,k,ans) : 
    n=len(arr)
    req=1 
    s=0 
    for i in range(n) : 
        if (s+arr[i])>ans :
            req+=1 
            s=arr[i]
        else : 
            s+=arr[i]
    return req<=k 

def allocateMinPages(arr, k) :  
    n=len(arr) 
    low=max(arr) 
    high=sum(arr) 
    res=0 
    while low<=high : 
        mid=(low+high)//2 
        if isFeasible(arr,k,mid) : 
            res=mid 
            high=mid-1 
        else : 
            low=mid+1 
    return res 
arr=[10,20,10,30]
print("[10,20,10,30], k=2 : ",allocateMinPages(arr,2))
arr=[10,20,30,40]
print("[10,20,30,40], k=2 : ",allocateMinPages(arr,2))
arr=[10,5,30,1,2,5,10,10]
print("[10,5,30,1,2,5,10,10], k=3 : ",allocateMinPages(arr,3))
print("\n") 