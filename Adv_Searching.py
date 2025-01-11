## Advanced searching 
#    Search in an Infinite sized array 
#    Search in sorted rotated array 
#    Find a Peak element 



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
        arr[n-1]
    for i in range(1,n-1) : 
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1] : 
            return arr[i]
arr=[5,10,20,15,7]
print("Get peak element: Naive ")
print("[5,10,20,15,7] : ",getPeak1(arr))
print("\n") 