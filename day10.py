# Searching 
#   Binary search  
#   Recursive Binary Search in Python 


## Binary Search (prerequisite : Array should be sorted) 
arr=[10,20,30,40,50,60,70,80] 
def binSearch(arr,x) :
    low=0 
    high=len(arr)-1  
    while low<=high :
        mid=(low+high)//2
        if arr[mid]==x :
            return mid 
        elif arr[mid]<x :
            low=mid+1
        else :
            high=mid-1 
    return -1 
print("Binary search : ") 
print("Element 60 : ", binSearch(arr,60))      
print("Element 25 : ", binSearch(arr,25))      


## Recursive Binary Search in Python 
def bSearch(l,x,low,high) :
    if low>high :
        return -1 
    mid=(low+high)//2 
    if l[mid]==x :
        return mid
    elif l[mid]>x :
        return bSearch(l,x,low,mid-1) 
    else : 
        return bSearch(l,x,mid+1,high) 
l=[10,20,30,40]
print("Index of 20 in l : ", bSearch(l,20,0,3))
print("Index of 40 in l : ", bSearch(l,40,0,3))
print("Index of 25 in l : ", bSearch(l,25,0,3))