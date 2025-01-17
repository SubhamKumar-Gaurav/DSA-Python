## Advanced Sorting 
#    Overview of sorting algorithm 
#    Tail call elimination in Quick sort 
#    Kth smallest 
#    Minimum difference in an arrray 
#    Chocolate distribution problem 
#    Sort an array with two types of element 
#    Sort an array with three types of element 
#    Merge overlapping intervals 
#    Meeting the maximum guests 
#    Counting sort 
#    Cycle sort 
#    Radix sort - Introduction 
#    Radix sort - Python implementation  
#    Bucket sort - Introduction 
#    Bucket sort - Python implementation  


## Tail call elimination in Quick sort
def qSort(arr,l,r) : 
    if l<r : 
        p=partition(arr,l,r)
        qSort(arr,l,b)
        qSort(arr,p+1,r) 

# Rewritten code (Tail call optimization)
def qSort(arr,l,r) : 
    while l<r : 
        p=partition(arr,l,r) 
        qSort(arr,l,p) 
        l=p+1 



## Kth smallest 
# Naive approach 
def kthsmallest(arr,k) : 
    n=len(arr) 
    arr.sort() 
    return arr[k-1]
  
# Using Lomuto partition  (code to be reviewed)
def KthSmallest(arr,k) :
    l=0 
    r=len(arr)-1 
    while l<=r : 
        p=lomuto(arr,l,r) 
        if p==k-1 : 
            return p 
        elif len(p)>k-1 : 
            r=len(p)-1 
        else : 
            l=len(p)+1 


## Minimum difference in an array 
# Naive 
def minDiff(arr) : 
    n=len(arr)
    res=float("inf") 
    for i in range(1,n) : 
        for j in range(i) : 
            res=min(res,abs(arr[i]-arr[j])) 
    return res 

# Efficient 
def mindiff(arr) : 
    n=len(arr) 
    arr.sort() 
    res=float('inf') 
    for i in range(1,n) : 
        res=min(res,abs(arr[i]-arr[i-1])) 
    return res 


## Chocolate distribution problem  
def choco(arr,m) : 
    n=len(arr)
    if m==0 or n==0 : 
        return 0
    if n<m : 
        return -1 
    arr.sort() 
    res=arr[m-1]-arr[0] 
    for i in range(1,n-m+1) : 
        res=min(res,arr[i+m-1]-arr[i]) 
    return res 


## Sort an array with two types of element 
def sortArr(arr) : 
    n=len(arr) 
    res=[0]*n 
    i=0  
    for j in range(n) : 
        if arr[j]<0 : 
            res[i]=arr[j] 
            i+=1 
    for j in range(n) : 
        if arr[j]>=0 : 
            res[i]=arr[j] 
            i+=1 
    arr=res  
    return res 
  
