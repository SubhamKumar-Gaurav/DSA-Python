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


## Longest common span with same sum in Binary array  
# Naive approach 
def longestCommonSpan(arr1, arr2) : 
    n=len(arr1)
    res=0 
    for i in range(n) : 
        sum1=0 
        sum2=0 
        for j in range(i,n) : 
            sum1+=arr1[j]
            sum2+=arr2[j] 
            if sum1==sum2 : 
                res=max(res, j-i+1) 
    return res 

# Efficient approach 
def longestComSpan(arr1, arr2) :
    n=len(arr1) 
    temp=[]
    for i in range(n) : 
        temp.append(arr1[i]-arr2[i])
    pre_sum=0 
    mydict=dict() 
    res=0 
    for i in range(n) : 
        pre_sum+=temp[i]
        if pre_sum==0 : 
            res=i+1  
        if pre_sum in mydict : 
            res=max(res, i-mydict[pre_sum])
        else : 
            mydict[pre_sum]=i 
    return res 


## Longest consecutive subsequence 
# Naive appraoch 
def findLongest(arr) : 
    n=len(arr) 
    arr.sort() 
    res=1 
    curr=1 
    for i in range(1,n) : 
        if arr[i]==arr[i-1]+1 : 
            curr+=1 
        else : 
            res=max(res, curr) 
            curr=1 
    res=max(res, curr) 
    return res 

# Efficient approach 
def findLongest(arr) : 
    s=set() 
    res=0 
    for i in arr : 
        s.add(i) 
    for i in arr : 
        if (i-1) not in s : 
            curr=1 
            while curr+i in s : 
                curr+=1 
            res=max(res, curr) 
    return res 


## Count distinct elements in every window 
# Naive solution 
def printDistinct(arr, k) : 
    for i in range(n-k+1) : 
        print(len(set(arr[i:i+k])))  

# Efficient solution 
from collections import Counter 
def countDistinct(arr, k) : 
    n=len(arr)
    mp=Counter(arr[:k])
    print(len(mp)) 
    for i in range(k,n) : 
        x=arr[i-k]   # first element of prev window 
        mp[x]-=1     
        mp[arr[i]]+=1  # last element of current window 
        if mp[x]==0 : 
            del mp[x] 
        print(len(mp))