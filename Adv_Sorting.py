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
  

def KthSmallest(arr,k) :
    l=0 
    r=len(arr)-1 
    while l<=r : 
        p=lomuto(arr,l,r) 
        if p==k-1 : 
            return p 
        elif p>k-1 : 
            r=p-1 
        else : 
            l=p+1 
