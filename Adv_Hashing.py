## Adv Hashing 
#   Intersection of two arrays 
#   Union of two unsorted array 
#   Pair with given sum in unsorted array 
#   Subarray with 0 sum  
#   Subarray with given sum 
#   Check for Palindrome Permutation
#   Longest Subarray with given sum 
#   Longest subarray with equal number of zero and one 
#   Longest common span with same sum in Binary array 
#   Longest consecutive subsequence 
#   Count distinct elements in every window 
#   More than n/k occurence 
#   More than n/k occurences  [ O(nk) solution ]


## Intersection of two arrays  
# Naive approach 
def intersection_a_b(arr1,arr2) : 
    m=len(arr1)
    n=len(arr2) 
    res=0 
    for i in range(m) : 
        flag=False 
        for j in range(i) : 
            if arr1[i]==arr1[j] : 
                flag=True 
        if flag==True : 
            continue 
        for j in range(n) : 
            if arr1[i]==arr2[j] : 
                res+=1 
                break 
    return res 

# Efficient approach 
def inter_section(arr1, arr2) : 
    m=len(arr1) 
    n=len(arr2) 
    us=set() 
    for i in arr1 : 
        us.add(i) 
    res=0 
    for i in range(n) : 
        if arr2[i] in us : 
            res+=1 
            us.remove(arr2[i]) 
    return res 



## Union of two unsorted array  
# Naive approach 
def unionSize(arr1, arr2) : 
    m=len(arr1)
    n=len(arr2)
    c=[0]*(m+n) 
    for i in range(m) :
        c[i]=arr1[i] 
    for i in range(n) : 
        c[m+i]=arr2[i]
    res=0 
    for i in range(m+n) : 
        flag=False 
        for j in range(i) : 
            if c[i]==c[j] : 
                flag=True 
                break 
        if flag==False : 
            res+=1 
    return res 

# Efficient approach 
def unionSize(arr1, arr2) : 
    m=len(arr1) 
    n=len(arr2) 
    us=set()
    for i in arr1 : 
        us.add(i) 
    for i in arr2 : 
        us.add(i) 
    return len(us) 


## Pair with given sum 
# Naive approach 
def pairSum(arr, x)  : 
    n=len(arr)
    for i in range(n) :  
        for j in range(i+1, n) : 
            if arr[i]+arr[j]==x : 
                return True 
    return False 

# Efficient approach 
def pairSum(arr, x)  : 
    us=set() 
    for i in arr : 
        if x-i in us : 
            return True
        us.add(i) 
    return False 


## Subarray with 0 sum   
# naive approach 
def isZero(arr) : 
    n=len(arr) 
    for i in range(n) : 
        for j in range(i+1,n)  : 
            if sum(arr[i:j+1])==0 : 
                return True 
    return False  

# Efficient approach 
def isZeroSum(arr) : 
    n=len(arr) 
    h=set() 
    preSum=0 
    for i in range(n) : 
        preSum+=arr[i] 
        if preSum==0 or preSum in h : 
            return True 
        h.add(preSum) 
    return False 


## Subarray with given Sum 
# Naive approach
def isSubSum(arr, x) : 
    n=len(arr) 
    for i in range(n) : 
        curr=0 
        for j in range(i,n) : 
            curr+=arr[j]
            if curr==x : 
                return True 
    return False 

# Efficient approach 
def isSubarrSum(arr, x) : 
    n=len(arr) 
    s, curr = 0, 0 
    for e in range(n) : 
        curr+=arr[e] 
        while curr>x : 
            curr-=arr[s] 
            s+=1 
        if curr==x : 
            return True 
    return False 


## Check for Palindrome Permutation 
from collections import Counter 
def isPalPer(s) : 
    cnt=Counter(s) 
    odd=0 
    for freq in cnt.values() :  
        if freq%2!=0 : 
            odd+=1 
            if odd>1 : 
                return False 
    return True 


## Longest Subarray with given sum 
# Naive approach 
def longestSubarrayWithSum(arr, x) : 
    n=len(arr) 
    res=0 
    for i in range(n) : 
        curr_sum=0 
        for j in range(i,n) : 
            curr_sum+=arr[j] 
            if curr_sum==x : 
                res=max(res,j-i+1) 
    return res 


# Efficient approach 
def longestSubSum(arr, x) : 
    n=len(arr) 
    mydict={}
    pre_sum=0 
    res=0 
    for i in range(n) : 
        pre_sum+=arr[i] 
        if pre_sum==x : 
            res=i+1 
        if pre_sum not in mydict : 
            mydict[pre_sum]=i 
        if pre_sum-x in mydict : 
            res=max(res, i-mydict[pre_sum-x]) 
    return res 


## Longest subarray with equal number of zero and one 
# Naive approach 
def longest01Sub(arr) : 
    n=len(arr) 
    res=0 
    for i in range(n) :
        c0=0 
        c1=0 
        for j in range(i,n) : 
            if arr[j]==0 : 
                c0+=1 
            else : 
                c1+=1 
            if c0==c1 : 
                res=max(res, j-i+1 )
    return res 

# Efficient approach 
def longest01Sub(arr) : 
    n=len(arr) 
    for i in range(n) : 
        if arr[i]==0 : 
            arr[i]=-1 
    mydict=dict() 
    x=0 
    res=0 
    for i in range(n) : 
        x+=arr[i] 
        if x==0 : 
            res=i+1 
        if x in mydict : 
            res=max(res, i-mydict[x]) 
        else : 
            mydict[x]=i 
    return res 
