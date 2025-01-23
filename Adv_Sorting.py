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
# Segregate positive and negative : Naive 
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
  

## Segregate positive and negative : using Hoare's partition 
def posNeg(arr) : 
    i=-1 
    j=len(arr) 
    while True : 
        i+=1 
        while arr[i]<0 : 
            i+=1 
        j-=1 
        while arr[j]>=0 : 
            j-=1 
        if i>=j : 
            return arr 
        arr[i], arr[j] = arr[j], arr[i] 



## Sort an array with three types of element 
def sort3Types(arr) :  
    temp=[]
    for x in arr : 
        if x==0 : 
            temp.append(x) 
    for x in arr : 
        if x==1 : 
            temp.append(x) 
    for x in arr : 
        if x==2 : 
            temp.append(x) 
    for i in range(len(arr)) : 
        arr[i]=temp[i] 
    return arr 


# Efficient approach 
def segregate3(arr) : 
    low=0 
    mid=0 
    high=len(arr)-1 
    while mid<=high : 
        if arr[mid]==0 : 
            arr[low], arr[mid] = arr[mid], arr[low] 
            low+=1 
            mid+=1 
        elif arr[mid]==1 : 
            mid+=1 
        else : 
            arr[high], arr[mid] = arr[mid], arr[high] 
            high-=1 
    return arr 


## Merge overlapping intervals 
def mergeIntervals(arr) : 
    n=len(arr)
    arr.sort(key=lambda x: x[0])
    res=0 
    for i in range(1,n) : 
        if arr[res][1]>=arr[i][0] : 
            arr[res][1]=max(arr[res][1], arr[i][1]) 
        else : 
            res+=1 
            arr[res]=arr[i]
    for i in range(res+1) : 
        print(arr[i], end=" ")   
 

## Meeting the maximum guests  
def maxGuests(arr,dept) : 
    n=len(arr)
    arr.sort() 
    dept.sort() 
    res=1
    curr=1  
    i=1 
    j=0 
    while i<n and j<n : 
        if arr[i]<=dept[j] : 
            curr+=1 
            i+=1 
        else : 
            curr-=1 
            j+=1 
        res=max(res,curr) 
    return res 



# Counting Sort 
# Naive approach 
def countingSort(arr,k) : 
    count=[0]*k 
    for x in arr : 
        count[x]+=1 
    index=0 
    for i in range(k) : 
        for j in range(count[i]) : 
            arr[index]=i 
        index+=1 
    return arr 


# Efficient Approach
def countingsort(arr,k) :
    output = [0] * len(arr)
    count = [0] * k
    for x in arr :
        count[x] += 1
        
    for i in range(1,k) :
        count[i] += count[i - 1]
    for x in reversed(arr) :
        output[count[x] - 1] = x
        count[x] -= 1 
    for i in range(len(arr)) :
        arr[i] = output[i]    
    print(arr)
    


## Cycle sort   
def cycleSort(arr) : 
    n=len(arr) 
    for cs in range(n-1) : 
        item=arr[cs] 
        pos=cs 
        for i in range(cs+1,n) : 
            if arr[i]<item : 
                pos+=1 
        if pos==cs : 
            continue 
        while item==arr[pos] : 
            pos+=1 
        arr[pos], item = item, arr[pos] 
        while pos!=cs : 
            pos=cs 
            for i in range(cs+1,n) : 
                if arr[i]<item : 
                    pos+=1 
            while item==arr[pos] :
                pos+=1 
            arr[pos], item = item, arr[pos]
    return arr 


## Radix sort 
def radixSort(arr) : 
    mx=max(arr) 
    exp=1 
    while mx//exp>0 : 
        countingSort(arr,exp) 
        exp*=10 
    return arr 
def countingSort(arr,exp) : 
    output=[0]*len(arr) 
    count=[0]*10 
    for i in range(len(arr)) : 
        index=(arr[i]//exp)%10 
        count[index]+=1 
    for i in range(1,10) : 
        count[i]+=count[i-1] 
    i=len(arr)-1 
    while i>=0 : 
        index=(arr[i]//exp)%10 
        output[count[index]-1]=arr[i] 
        count[index]-=1 
        i-=1 
    for i in range(len(arr)) : 
        arr[i]=output[i] 
