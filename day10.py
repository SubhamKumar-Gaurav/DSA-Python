# Searching 
#   Binary search  
#   Recursive Binary Search in Python 
#   Index of first occurence of an element in sorted array - 3 approaches 
#   Last occurence - 2 approaches 



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
print("") 


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
print("Recursive Binary Search : ")
l=[10,20,30,40]
print("Index of 20 in l : ", bSearch(l,20,0,3))
print("Index of 40 in l : ", bSearch(l,40,0,3))
print("Index of 25 in l : ", bSearch(l,25,0,3))
print("") 

## Index of first ocurence in a sorted array 
# Approach - 1  : Naive Approach 
def firstOccurence1(arr,x) :
    n=len(arr) 
    for i in range(n) : 
        if arr[i]==x :
            return i 
    return -1 
arr1=[1,10,10,10,20,20,20,40]
print("Naive Approach : ")
print("First occurence of 20 : ",firstOccurence1(arr1,20)) 
print("") 

# Approach - 2 :    Recursive Binary Search 
def firstOccurence2(arr,low,high,x) :
    if low>high :
        return -1 
    mid=(low+high)//2 
    
    if arr[mid]>x :
        return firstOccurence2(arr,low,mid-1,x) 
    elif arr[mid]<x :
        return firstOccurence2(arr,mid+1,high,x) 
    else :
        if mid==0 or arr[mid-1]!=arr[mid] :
            return mid 
        else : 
            return firstOccurence2(arr,low,mid-1,x) 
arr2=[5,10,10,15,20,20,20]
x=20 
print("Recursive Binary Search Approach ")
print("First occurence of 20 : ", firstOccurence2(arr2,0,6,20)) 
print("")

# Approach - 3 :  Iterative Binary Search 
def firstOccurence3(arr,x) :
    low=0
    high=len(arr)-1 
    while low<=high : 
        mid=(low+high)//2 
        if arr[mid]>x :
            high=mid-1 
        elif arr[mid]<x :
            low=mid+1 
        else :
            if mid==0 or arr[mid-1]!=arr[mid] :
                return mid 
            else :
                high=mid-1 
    return -1 
arr3=[5,10,10,20,20]
print("Iterative Binary Search : ") 
print("First occurence of 10 : ", firstOccurence3(arr3,10)) 
print("")


## Last Occurence of an element in a sorted array 
# Approach - 1 :   Naive approach 
def lastOccurence1(l,x) :
    for i in reversed(range(len(l))) :
        if l[i]==x :
            return i 
    return -1 
l1=[5,10,10,10,10,10,20,20]
x1=10 
print("Naive approach for last occurence ") 
print("Last occurence of 10 : ", lastOccurence1(l1,x1)) 
print("")

# Approach - 2 :  Iterative Binary Search  
def lastOccurence2(l,x) : 
    low=0 
    high=len(l)-1 
    while low<=high :
        mid=(low+high)//2  
        if l[mid]>x :
            high=mid-1
        elif l[mid]<x : 
            low=mid+1 
        else :
            if mid==len(l)-1 or l[mid]!=l[mid+1] :
                return mid 
            else : 
                low=mid+1 
    return -1 
l=[5,10,10,10,10,20,20] 
x=10
print("Iterative Binary Search for last occurence ")
print("Last occurence of 10 : ", lastOccurence2(l,x)) 
