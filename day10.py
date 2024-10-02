# Searching 
#   Binary search  


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