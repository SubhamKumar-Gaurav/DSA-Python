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