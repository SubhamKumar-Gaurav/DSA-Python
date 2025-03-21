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
arr=[-3, 8, -2, 4, -5, 6] 
print("[-3, 8, -2, 4, -5, 6] : ", maxSum2(arr)) 
print("\n")  



## Longest Even Odd subarray  
print("Maximum length even odd subarray: Naive")
def maxEvenOdd1(arr) : 
    n=len(arr) 
    res=1 
    for i in range(n) : 
        curr=1 
        for j in range(i+1,n) : 
            if (arr[j]%2==0 and arr[j-1]%2!=0) or (arr[j]%2!=0 and arr[j-1]%2==0) : 
                curr+=1 
            else : 
                break 
        res=max(res,curr) 
    return res 
arr=[5, 10, 20, 6, 3, 8]
print("[5, 10, 20, 6, 3, 8] : ", maxEvenOdd1(arr))
print("\n") 


print("Maximum length even odd subarray: Efficient")
print("Also Kadane's algorithm ")
def maxEvenOdd2(arr) : 
    n=len(arr) 
    res=1 
    curr=1 
    for i in range(1,n) : 
        if arr[i]%2 != arr[i-1]%2 : 
            curr+=1 
            res=max(res,curr)
        else : 
            curr=1       
    return res 
arr=[7,10,13,14]
print("[7,10,13,14] : ",maxEvenOdd2(arr)) 
print("\n")  


## Maximum Circular Sum Subarray 
print("Maximum Circular Sum Subarray: Naive")
def maxCircularSum(arr) : 
    n=len(arr)
    res=arr[0] 
    for i in range(n) : 
        curr_max=arr[i]
        curr_sum=arr[i]
        for j in range(1,n) : 
            index=(i+j)%n
            curr_sum+=arr[index]
            curr_max=max(curr_max, curr_sum) 
        res=max(res, curr_max) 
    return res 
arr=[5,-2,3,4] 
print("[5,-2,3,4] : ",maxCircularSum(arr)) 
print("\n") 


print("Maximum Circular Sum Subarray: Efficient")
def normalMaxSum(arr) :    # Kadane's algorithm
    n=len(arr) 
    res=arr[0] 
    maxEnding=arr[0]
    for i in range(1,n) : 
        maxEnding=max(maxEnding+arr[i], arr[i]) 
        res=max(res, maxEnding)
    return res 
def overallMaxSum(arr) : 
    n=len(arr) 
    max_normal=normalMaxSum(arr)   # Normal sum
    if max_normal<0 : 
        return max_normal 
    arr_sum=0     # For total sum of arr
    for i in range(n) : 
        arr_sum+=arr[i] 
        arr[i]=-arr[i] 
    max_circular=arr_sum+normalMaxSum(arr)   # Circular sum
    return max(max_circular, max_normal) 
arr=[8,-4,3,-5,4]
print("[8,-4,3,-5,4] : ",overallMaxSum(arr)) 
print("\n") 


## Majority element 
print("Majority element: Naive") 
def findMajority(arr) : 
    n=len(arr) 
    for i in range(n) : 
        count=1 
        for j in range(i+1,n) : 
            if arr[i]==arr[j] : 
                count+=1 
        if count>n/2 : 
            return i 
    return -1 
arr=[8,3,4,8,8]
print("[8,3,4,8,8] : ", findMajority(arr)) 
print("\n") 


print("Majority element: Efficient")
print("Moore's Voting Algorithm") 
def findMajority2(arr) : 
    n=len(arr) 
    # Find a candidate 
    res=0 
    count=1 
    for i in range(1,n) : 
        if arr[i]==arr[res] : 
            count+=1 
        else : 
            count-=1 
        if count==0 : 
            res=i 
            count=1 
    # Check if the candidate is actually a majority 
    count=0 
    for i in range(n) : 
        if arr[i]==arr[res] : 
            count+=1 
    if count<=n/2 : 
        return -1 
    return res 
arr=[8,8,6,6,6,4,6] 
print("[8,8,6,6,6,4,6] : ", findMajority2(arr)) 
print("\n")
 

## Minimum consecutive flips
print("Minimum consecutive flips")   
def minConsFlips(arr) : 
    n=len(arr) 
    for i in range(1,n) : 
        if arr[i]!=arr[i-1] : 
            if arr[i]!=arr[0] : 
                print("From ", i , "to ", end=" ") 
            else : 
                print(i-1) 
    if arr[n-1]!=arr[0] : 
        print(n-1) 
arr=[0,0,1,1,0,0,1,1,0] 
print("[0,0,1,1,0,0,1,1,0] : ")
minConsFlips(arr)
print("\n") 


## Sliding window technique 
# Naive solution
print("Maximum sum of k consecutive elements: Naive")   
def maxKSum(arr,k) : 
    n=len(arr)
    res=float("-inf") 
    i=0 
    while (i+k-1<n) : 
        curr=0 
        for j in range(k) : 
            curr+=arr[i+j] 
        res=max(curr,res) 
        i+=1 
    return res 
arr=[10,5,-2,20,1] 
k=3 
print("[10,5,-2,20,1] : ",maxKSum(arr,k)) 
print("\n") 

# Efficient approach (Sliding window technique) 
print("K max Sum: Sliding window")
def kMaxSum(arr,k) : 
    n=len(arr) 
    res=0 
    for i in range(k) : 
        res+=arr[i] 
    curr=res
    for i in range(n-k) : 
        curr = curr + arr[i+k] - arr[i] 
        res=max(res,curr) 
    return res 
arr=[1,8,30,-5,20,7]
k=4
print("[1,8,30,-5,20,7] : ",kMaxSum(arr,k)) 
print("\n") 


## Subarray with given sum 
print("Subarray with given sum: Naive") 
def isSubSum(arr,s) : 
    n=len(arr)
    for i in range(n) :
        curr=0 
        for j in range(i,n) : 
            curr+=arr[j] 
            if curr==s : 
                return True 
    return False 
arr=[1,4,20,3,10,5]
s=33 
print("[1,4,20,3,10,5], 33 : ", isSubSum(arr,s))
print("\n") 


print("Efficient (Sliding window with variable size)") 
def givenSumSub(arr,sum_) :  
    n=len(arr) 
    curr=0 
    s=0 
    for e in range(n) : 
        curr+=arr[e] 
        while curr>sum_ : 
            curr-=arr[s] 
            s+=1 
        if curr==sum_ : 
            return True
    return False 
arr=[1,4,20,3,10,5] 
s=33 
print("[1,4,20,3,10,5] , 33 :",givenSumSub(arr,s)) 
arr=[2,4]
s=3 
print("[2,4] , 3 : ",givenSumSub(arr,s))
print("\n") 


## PrefixSum Technique 
# Given a fixed array and multiple range sum queries, how to answer the queries efficiently 
# Naive solution 
def getSum(arr,l,r) : 
    res=0 
    for i in range(l,r+1) : 
        res+=arr[i]
    return res 


## Efficient solution 
print("Prefix Sum Technique : ")
arr=[2,8,3,9,6,5,4]
n=len(arr) 
pSum=[0]*n 
pSum[0]=arr[0]
for i in range(1,n) : 
    pSum[i]=pSum[i-1]+arr[i]
def getSump(l,r) : 
    if l==0 : 
        return pSum[r] 
    else : 
        return pSum[r]-pSum[l-1]  
print("arr = [2,8,3,9,6,5,4] ")
print("getSum(arr,0,3) : ",getSum(arr,0,3))
print("getSum(arr,2,3) : ",getSum(arr,2,3))
print("\n") 


## Equilibrium point 
print("Equilibrium point: Naive approach ") 
def eqPoint(arr) : 
    n=len(arr) 
    for i in range(n) : 
        ls=0 
        rs=0 
        for j in range(i) : 
            ls+=arr[j] 
        for k in range(i+1,n) : 
            rs+=arr[k]
        if ls==rs : 
            return True 
    return False 
arr=[3,4,8,-9,20,6] 
print("[3,4,8,-9,20,6] : ", eqPoint(arr)) 
print("\n") 

print("Equilibrium point: Efficient approach")
def ePoint(arr) : 
    n=len(arr) 
    rs=sum(arr) 
    ls=0 
    for i in range(n) : 
        rs-=arr[i] 
        if ls==rs : 
            return True 
    return False 
arr=[3,4,8,-9,9,7] 
print("[3,4,8,-9,9,7] : ", ePoint(arr)) 
print("\n")  


## Maximum appearing element in ranges    
print("Maximum appearing element in ranges (Naive)") 
def maxAppear1(left, right) : 
    freq=[0]*100 
    for i in range(len(left)) :
        for j in range(left[i], right[i]+1) : 
            freq[j]+=1 
    return freq.index(max(freq)) 
left=[1,2,4]
right=[4,5,7] 
print(maxAppear1(left, right)) 
print("\n") 

print("Maximum appearing element in ranges (Efficient)")    
def maxAppear2(left, right) : 
    freq=[0]*101 
    for i in range(len(left)) : 
        freq[left[i]]+=1 
        freq[right[i]+1]-=1 
    for i in range(1,101) : 
        freq[i]+=freq[i-1] 
    return freq.index(max(freq)) 
print(maxAppear2(left, right)) 
print("\n") 