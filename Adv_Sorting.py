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