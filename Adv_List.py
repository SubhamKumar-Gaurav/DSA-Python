## Advanced List  
#   Left rotate by d places 
#   Maximum difference 
#   Stock buy and sell 
#   Trapping rain water 
#   Maximum subarray sum 
#   Longest Even Odd subarray 
#   Maximum Circular Sum Subarray 
#   Majority element 
#   Minimum consecutive flips 
#   Sliding window technique 
#   Subarray with given sum 
#   Prefix sum technique 
#   Equilibrium point 
#   Maximum appearing element in ranges 



## Left rotate by d places 
print("Left rotate by d places ")
# Using List slicing
print("Using List Slicing : ")
l=[10,20,30,40,50]
d=2 
l=l[d:]+l[:d] 
print(l) 
print("\n") 

# Using deque
print("Using deque : ")
from collections import deque
l=[10,20,30,40,50]
d=2 
dq=deque(l) 
dq.rotate(-d) 
l=list(dq) 
print(l) 
print("\n") 

# Using pop and append 
def leftRotate(l,d) : 
    for i in range(d) : 
        l.append(l.pop(0))
    print(l)
l=[10,20,30,40,50]
d=3 
print("Using pop and append")
leftRotate(l,d) 
print("\n")   

# Using reverse function  Time: O(n) 
print("Using reverse function : ")
def reverse(l,b,e) : 
    while b<e : 
        l[b], l[e]= l[e], l[b]
        b+=1 
        e-=1 
def leftRotate(l,d) : 
    n=len(l)
    reverse(l,0,d-1) 
    reverse(l,d,n-1)
    reverse(l,0,n-1)
    return l
l=[10,20,30,40,50]
d=3
print(leftRotate(l,d)) 
print("\n")   


## Maximum difference 
#  Naive Approach    Time : O(n^2)
print("Maximum difference (Naive approach)")
def maxdiff(arr) : 
    n=len(arr) 
    res=arr[1]-arr[0] 
    for i in range(n-1) : 
        for j in range(i+1,n) : 
            res=max(res,arr[j]-arr[i]) 
    return res 
l=[2,3,10,6,4,8,1] 
print("[2,3,10,6,4,8,1] : ", maxdiff(l)) 
print("\n") 

# Two variable     Time : O(n) 
print("Maximum difference using two variables") 
def maxDiff(arr) : 
    n = len(arr) 
    res = arr[1]-arr[0] 
    minval = arr[0] 
    for i in range(1,n) : 
        res = max(res, arr[i]-minval) 
        minval=min(minval,arr[i])
    return res 
l=[2,3,10,6,4,8,1]
print("[2,3,10,6,4,8,1] : ", maxDiff(l)) 
print("\n")    


## Stock buy and sell 
# Naive solution  
def maxProfit(arr,b,e) : 
    if e<=b : 
        return 0 
    res=0 
    for i in range(b,e) : 
        for j in range(i+1,e+1) : 
            if arr[j]>arr[i] : 
                curr=arr[j]-arr[i]+maxProfit(arr,b,i-1)+maxProfit(arr,j+1,e)  
                res=max(res,curr) 
    return res 
l=[1,5,3,8,12] 
print("Stock buy and sell (Naive - recursive) ") 
print("[1,5,3,8,12] : ", maxProfit(l,0,4)) 
print("\n") 

# Efficient approach   
def maxProfit2(arr) : 
    res=0 
    n=len(arr)
    for i in range(1,n) :  
        if arr[i]>arr[i-1] : 
            res+= arr[i]-arr[i-1] 
    return res 
arr=[1,5,3,8,12] 
print("Stock buy and sell: Efficient " )
print("[1,5,3,8,12] : ",maxProfit2(arr))   
print("\n") 


## Trapping rain water 
print("Trapping rain water : Naive") 
def getWater1(arr) : 
    n=len(arr) 
    res=0 
    for i in range(1,n-1) : 
        lmax=arr[i] 
        for j in range(0,i) : 
            lmax=max(lmax,arr[j]) 
        rmax=arr[j] 
        for j in range(i+1,n) : 
            rmax=max(rmax,arr[j]) 
        res+=(min(lmax,rmax)-arr[i])
    return res 
arr=[3,0,1,2,5] 
print("[3,0,1,2,5] : ",getWater1(arr)) 
print("\n") 


print("Trapping rain water: Efficient") 
def getWater2(arr) : 
    n=len(arr) 
    res=0 
    lmax=[0]*n 
    rmax=[0]*n 

    lmax[0]=arr[0]
    for i in range(1,n-1) : 
        lmax[i]=max(lmax[i-1], arr[i]) 

    rmax[n-1]=arr[n-1]
    for i in range(n-2,-1,-1) : 
        rmax[i]=max(rmax[i+1], arr[i]) 

    for i in range(1,n-1) :
        res+=(min(lmax[i],rmax[i])-arr[i])  
    return res 
arr=[2,0,2]
print("[2,0,2] : ",getWater2(arr)) 
print("\n") 


## Maximum subarray sum  
print("Maximum subarray sum: Naive")  
def maxSum1(arr) : 
    n=len(arr) 
    res=0 
    for i in range(n) : 
        curr=0 
        for j in range(i,n) : 
            curr+=arr[j] 
            res=max(res,curr) 
    return res 
arr=[1,-2,3,-1,2] 
print("[1,-2,3,-1,2] : ", maxSum1(arr)) 
print("\n")  

print("Maximum subarray sum : Efficient ")
def maxSum2(arr) : 
    n=len(arr) 
    res=arr[0]
    maxEnding=arr[0] 
    for i in range(1,n) : 
        maxEnding=max(maxEnding+arr[i], arr[i]) 
        res=max(res, maxEnding) 
    return res 
arr=[-5,1,-2,3,-1,2,-2] 
print("[-5,1,-2,3,-1,2,-2] : ", maxSum2(arr)) 
print("\n") 