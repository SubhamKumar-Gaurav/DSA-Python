## Advanced searching 
#    Search in an Infinite sized array 
#    


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