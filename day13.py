# Day - 13 
#    Union of two sorted arrays
#    Intersection of two sorted arrays 
#    Count inversions in an array 
#    Partition a given array 
#    Lomuto Partition 
#    Hoare's Partition 



## Union of two sorted arrays 
# Naive Approach 
def print_Union(a,b) : 
    c=a+b 
    c.sort() 
    for i in range(len(c)) : 
        if i==0 or c[i]!=c[i-1] : 
            print(c[i], end=" ") 
a=[3,5,8] 
b=[2,8,9,10,15] 
print("Union of two sorted arrays : ") 
print("Naive Approach : ")
print(print_Union(a,b), "\n") 

# Efficient approach 
def printUnion(a,b) : 
    i=0 
    j=0 
    while (i<len(a) and j<len(b)) : 
        if i>0 and a[i]==a[i-1] : 
            i=i+1 
        elif j>0 and b[j]==b[j-1] : 
            j=j+1 
        elif a[i]<b[j] : 
            print(a[i], end=" ")
            i=i+1
        elif b[j]<a[i] : 
            print(b[j], end=" ") 
            j=j+1 
        else :
            print(a[i], end=" ") 
            i=i+1 
            j=j+1 
    while i<len(a) : 
        if i>0 and a[i]!=a[i-1] : 
            print(a[i], end=" ") 
            i=i+1 
    while j<len(b) : 
        if j>0 and b[j]!=b[j-1] : 
            print(b[j], end=" ")
            j=j+1 
a=[2,10,20,20] 
b=[3,20,40] 
print("Efficient Approach (using merge sort) : ")
print(printUnion(a,b), "\n") 


## Intersection of two sorted arrays  
# Naive approach : 
def intersection1(a,b,m,n) : 
    for i in range(m) : 
        if i>0 and a[i]==a[i-1] : 
            continue 
        for j in range(n) : 
            if a[i]==b[j] : 
                print(a[i], end=" ") 
                break 
a=[1,20,20,40,60] 
b=[2,20,20,20] 
print("Intersection of two arrays : ")
print("Naive approach : " )
print(intersection1(a,b,5,4), "\n") 
 
# Efficient approach 
def intersection2(a,b,m,n) : 
    i=0 
    j=0 
    while i<m and j<n : 
        if i>0 and a[i-1]==a[i] : 
            continue 
        if a[i]<b[j] : 
            i=i+1 
        elif b[j]<a[i] : 
            j=j+1 
        else : 
            print(a[i], end=" ") 
            i=i+1
            j=j+1 
     
a=[3,5,10,10,10,15,15,20]
b=[5,10,10,15,30] 
# print("Efficient solution : ") 
# print(intersection2(a,b,8,5)) 



## Count inversions in an array  
# Naive Approach  
def invCount(arr) : 
    n=len(arr) 
    res=0 
    for i in range(n-1) : 
        for j in range(i+1,n) : 
            if arr[i]>arr[j] : 
                res+=1 
    return res 
a=[2,4,1,3,5] 
print("Count inversions : ")
print("Naive approach ", invCount(a))


# Efficient approach 
def countInv(arr,l,r) : 
    res=0 
    if l<r : 
        m=(l+r)//2
        res+=countInv(arr,l,m) 
        res+=countInv(arr,m+1,r) 
        res+=countMerge(arr,l,m,r) 
    return res 

def countMerge(arr,l,m,r) :  
    left=arr[l:m+1] 
    right=arr[m+1:r+1] 
    res,i,j,k=0,0,0,l 
    while i<len(left) and j<len(right) : 
        if left[i]<=right[j] : 
            arr[k]=left[i] 
            i+=1 
        else : 
            arr[k]=right[j] 
            j+=1 
            res+=(len(left)-i) 
        k+=1 
    while i<len(left) : 
        arr[k]=left[i] 
        i+=1 
        k+=1 
    while j<len(right) : 
        arr[k]=right[j] 
        j+=1 
        k+=1 
    return res 
b=[8,5,11,2,6,3,13,9] 
print("Efficient approach ", countInv(b,0,7), "\n") 


## Partition a given array 
def partition(arr,p) : 
    n=len(arr) 
    arr[p],arr[n-1]=arr[n-1],arr[p] 
    temp=[]
    for x in arr : 
        if x<=arr[n-1] : 
            temp.append(x) 
    for i in arr : 
        if i>arr[n-1] : 
            temp.append(i) 
    for i in range(n) : 
        arr[i]=temp[i] 
    return arr 
a=[5,13,6,9,12,8,11] 
print("Partition a given array : ") 
print(partition(a,5), "\n")