## Dynamic Programming 
#   Memoization
#   Tabulation
#   Longest Common Subsequence 
#   Variation of LCS 
#   Coin Change 
#   Edit Distance 
#   Longest Increasing Sub sequence 
#   Variation of LIS 
#   Rope Cutting  
#   Minimum coins to make a given value 
#   Minimum jumps to reach the end 
#   0-1 Knapsack problem 
#   Optimal Strategy for a game 
#   Egg dropping puzzle 
#   Count BSTs with n keys 
#   Maximum sum with no two consecutive 
#   Subset sum problem 
#   Matrix Chain Multiplication 
#   Palindrome Partitioning 
#   Allocate Minimum Pages 


## Memoization 
# Fibonacci using Recursion 
def fibo(n) : 
    if n==0 or n==1 : 
        return n 
    return fibo(n-1)+fibo(n-2) 
print("Fibonacci (Recursion) : ",fibo(7))


# Fibonacci using DP (memoization) 
memo=[None]*100   # Assumption n<100 
def fib(n) : 
    if memo[n]!=None :  
        return memo[n] 
    if n==0 or n==1 : 
        memo[n]=n 
    else : 
        memo[n]=fib(n-1)+fib(n-2) 
    return memo[n] 
print("Fibonacci (Memoization) : ", fib(7)) 


## Tabulation 
def fibo(n) : 
    dp=[0]*(n+1) 
    dp[0]=0 
    dp[1]=1 
    for i in range(2, n+1) : 
        dp[i]=dp[i-1]+dp[i-2] 
    return dp[n] 
n=7
print("Fibonacci (Tabulation) : ", fibo(n))
print("\n") 


## Longest Common Subsequence 
# Recursive solution 
def lcsRec(s1, s2, n, m) : 
    if n==0 or m==0 : 
        return 0 
    if s1[n-1]==s2[m-1] : 
        return 1+lcsRec(s1, s2, n-1, m-1) 
    else : 
        return max(lcsRec(s1, s2, n, m-1), lcsRec(s1, s2, n-1, m)) 
s1="ABCDGH"
s2="AEDFHR" 
print("LCS using Recursion : ",lcsRec(s1, s2, len(s1), len(s2))) 

# Memoization 
M=1000 
N=1000 
memo=[[-1]*(N) for i in range(M)] 
def lcsMemo(s1, s2, n, m) : 
    if memo[n][m]!=-1 : 
        return memo[n][m] 
    if n==0 or m==0 : 
        memo[n][m]=0 
    else : 
        if s1[n-1]==s2[m-1] : 
            memo[n][m]=1+lcsMemo(s1, s2, n-1, m-1) 
        else : 
            memo[n][m]=max(lcsMemo(s1, s2, n-1, m), lcsMemo(s1, s2, n, m-1)) 
    return memo[n][m] 
print("LCS using Memoization : ", lcsMemo(s1, s2, len(s1), len(s2))) 

# Tabulation 
def lcsTabu(s1, s2) : 
    m=len(s1)
    n=len(s2) 
    dp=[[None]*(n+1) for i in range(m+1)] 
    for i in range(m+1) : 
        for j in range(n+1) : 
            if i==0 or j==0 : 
                dp[i][j]=0 
            elif s1[i-1]==s2[j-1] : 
                dp[i][j]=1+dp[i-1][j-1]
            else : 
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
    return dp[m][n] 
print("LCS using Tabulation : ", lcsTabu(s1, s2)) 
print("\n") 



## Coin Change 
# Recursive 
def coinChangeRec(coins, n, s) : 
    if s==0 : 
        return 1 
    if s<0 : 
        return 0 
    if n==0 : 
        return 0 
    return coinChangeRec(coins, n, s-coins[n-1])+coinChangeRec(coins, n-1, s)
coins=[2,5,3,6] 
s=10 
print("Coin Change (Recursive) : ",coinChangeRec(coins, 4, s)) 

# DP approach 
def coinChangeDP(coins, s) : 
    n=len(coins) 
    dp=[[0 for x in range(s+1)] for x in range(n+1)] 
    for i in range(n+1) : 
        dp[i][0]=1 
    for i in range(1,n+1) : 
        for j in range(1, s+1) :  
            dp[i][j]=dp[i-1][j] 
            if j>=coins[i-1] : 
                dp[i][j]+=dp[i][j-coins[i-1]] 
    return dp[n][s]
coins=[2,5,3,6] 
s=10 
print("Coin Change (DP) : ",coinChangeDP(coins, s)) 
print("\n")



## Edit Distance 
# Recursive 
def edRec(s1, s2, m, n) : 
    if n==0 : 
        return m 
    if m==0 : 
        return n 
    if s1[m-1]==s2[n-1] : 
        return edRec(s1, s2, m-1, n-1)
    else : 
        return 1+min(edRec(s1, s2, m-1, n), edRec(s1, s2, m, n-1), edRec(s1, s2, m-1, n-1)) 
s1="saturday"
s2="sunday" 
print("Edit Distance (Recursive) : ",edRec(s1, s2, len(s1), len(s2))) 


# DP approach 
def edDP(s1, s2) : 
    m=len(s1)
    n=len(s2) 
    dp=[[0 for x in range(n+1)] for x in range(m+1)]  
    for i in range(m+1) : 
        dp[i][0]=i  
    for j in range(n+1) : 
        dp[0][j]=j 
    for i in range(1,m+1) : 
        for j in range(1,n+1) : 
            if s1[i-1]==s2[j-1] : 
                dp[i][j]=dp[i-1][j-1]
            else : 
                dp[i][j]=1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) 
    return dp[m][n] 
s1="sunday"
s2="saturday" 
print("Edit Distance (DP) : ",edDP(s1, s2))
print("\n")



## Longest Increasing Subsequence 
# Naive approach  ;  Time: O(n^2)
def lis1(arr) : 
    n=len(arr) 
    lis=[1]*n 
    for i in range(1,n) : 
        for j in range(i) : 
            if arr[j]<arr[i] : 
                lis[i]=max(lis[i], lis[j]+1) 
    return max(lis) 
arr=[3,4,2,8,10,5,1] 
print("Longest Increasing Subsequence : ",lis1(arr)) 


# Efficient approach   ;   Time: O(n logn)
def lis2(arr) : 
    n=len(arr) 
    tail=[arr[0]] 
    for i in range(1, n) :  
        if arr[i]>tail[-1] : 
            tail.append(arr[i])
        else : 
            c=ceilIdx(tail,arr[i]) 
            tail[c]=arr[i]
    return len(tail) 

def ceilIdx(tail,x) : 
    l=0 
    r=len(tail)-1 
    while l<r : 
        m=l+(r-l)//2 
        if tail[m]>x : 
            r=m 
        else : 
            l=m+1 
    return l
print("Longest Increasing Subsequence : ",lis2(arr))
print("\n")


## Variations of LIS 
# Maximum Sum Increasing Subsequence 
def maxSIS(arr) : 
    n=len(arr)
    msis=[x for x in arr] 
    for i in range(1,n) : 
        for j in range(i) :  
            if arr[j]<arr[i] : 
                msis[i]=max(msis[i], arr[i]+msis[j]) 
    return max(msis) 
arr=[3,1,10,4,7] 
print("Maximum Sum Increasing Subsequence : ",maxSIS(arr))
print("\n")

# Maximum length Bitonic sequence 
def bts(arr) : 
    n=len(arr) 
    lis=[1]*n 
    for i in range(1, n) : 
        for j in range(i) : 
            if arr[j]<arr[i] : 
                lis[i]=max(lis[i], lis[j]+1)
    lds=[1]*n 
    arr=arr[::-1]
    for i in range(1,n) : 
        for j in range(i) : 
            if arr[j]<arr[i] : 
                lds[i]=max(lds[i], lds[j]+1)
    lds=lds[::-1] 
    res=1 
    for i in range(n) : 
        res=max(res, lis[i]+lds[i]-1) 
    return res 
arr=[1,11,2,10,4,5,2,1]
print("Max length Bitonic sequence : ",bts(arr))  
print("\n")  



## Building Bridges 
arr=[[1,8], [1,2], [4,3], [3,4], [2,6], [6,7], [7,8], [5,5]] 
def buildBridges(arr) : 
    arr.sort(key=lambda x: (x[0],x[1]))  
    new_arr=[] 
    for i in range(len(arr)) : 
        new_arr.append(arr[i][1]) 
    return lis2(new_arr)
print("Build bridges : ",buildBridges(arr)) 
print("\n")  



## Longest Chain of Pairs 
#  O(n^2) solution 
arr=[[5,24], [39,60], [15,28], [27,40], [50,90]] 
def longestChainPairs(arr) : 
    n=len(arr)
    arr.sort(key=lambda x: x[0]) 
    lis=[1]*n 
    for i in range(1,n) : 
        for j in range(i) : 
            if arr[i][0]>arr[j][1] : 
                lis[i]=max(lis[i], lis[j]+1) 
    return max(lis)
print("Longest Chain of Pairs ")   
print("O(n^2) solution : ", longestChainPairs(arr)) 


# O(n logn) solution 
def longestChainofPairs(arr) : 
    n=len(arr)
    arr.sort(key=lambda x: x[0]) 
    last_end=arr[0][1] 
    count=1 
    for i in range(1,n) : 
        if arr[i][0]>last_end : 
            count+=1 
            last_end=arr[i][1] 
    return count
print("O(n logn) solution : ",longestChainofPairs(arr))
print("\n") 


## Rope cutting 
# Recursive solution 
def ropeCuttingRec(n,a,b,c) : 
    if n==0 : 
        return 0 
    if n<0 : 
        return -1 
    res=max(ropeCuttingRec(n-a, a, b, c), ropeCuttingRec(n-b, a, b, c), ropeCuttingRec(n-c, a, b, c)) 
    if res==-1 : 
        return res 
    return res+1 
print("Rope cutting (Recursive) : ", ropeCuttingRec(5,1,2,3)) 


# DP solution 
def ropeCuttingDP(n,a,b,c) : 
    dp=[-1 for i in range(n+1)] 
    dp[0]=0
    for i in range(1,n+1) : 
        if i>=a : 
            dp[i]=dp[i-a]
        if i>=b : 
            dp[i]=max(dp[i], dp[i-b])
        if i>=c : 
            dp[i]=max(dp[i], dp[i-c])
        if dp[i]!=-1 : 
            dp[i]=dp[i]+1
    return dp[n]
print("Rope cutting (DP) : ", ropeCuttingDP(5,1,2,3))
print("\n") 



## Minimum coins to make a given value 
# Recursive solution 
def minCoinsRec(coins, val) : 
    if val==0 : 
        return 0 
    n=len(coins) 
    res=-1 
    for i in range(n) : 
        if coins[i]<=val : 
            sub_res=minCoinsRec(coins, val-coins[i]) 
            if sub_res!=-1 : 
                if res==-1 or (sub_res+1)<res : 
                    res=sub_res+1 
    return res 
coins=[25,10,5]
val=30
print("Minimum Coins to make a value (Recursive) : ",minCoinsRec(coins, val))

# DP solution 
def minCoinsDP(coins, val) : 
    dp=[float("inf")]*(val+1) 
    dp[0]=0 

    for amount in range(1,val+1) : 
        for coin in coins : 
            if coin<=amount : 
                dp[amount]=min(dp[amount], dp[amount-coin]+1) 
    if dp[val]!=float("inf") : 
        return dp[val] 
    return -1 
coins=[25,10,5]
val=30
print("Minimum Coins to make a value (Bottom-Up DP) : ",minCoinsDP(coins, val))
print("\n")



## Minimum Jumps to reach the end 
# Recursive solution      Time: O(n^n)
def minJumpsRec(arr, n) :
    if n==1 : 
        return 0 
    res=float("inf") 
    for i in range(n-1) : 
        if i+arr[i]>=n-1 : 
            sub_res=minJumpsRec(arr, i+1) 
            if sub_res!=float("inf") : 
                res=min(res, sub_res+1) 
    return res 
arr=[3,4,2,1,2,1]
n=len(arr) 
print("Min Jumps to reach end (Recursive) : ", minJumpsRec(arr,n)) 


# DP solution         Time: O(n^2)
def minJumpsDP(arr) : 
    n=len(arr) 
    dp=[float("inf")]*n 
    dp[0]=0 
    for i in range(1,n) : 
        for j in range(i) : 
            if (i<=j+arr[j]) and (dp[j]!=float("inf")) : 
                dp[i]=min(dp[i], dp[j]+1) 
                break 
    return dp[n-1] 
arr=[3,4,2,1,2,1]
n=len(arr) 
print("Min Jumps to reach end (DP) : ", minJumpsDP(arr)) 
print("\n") 



## 0-1 knapsack problem 
# Recursive solution   
def knapSackRec(W, wt, val, n) : 
    if n==0 or W==0 : 
        return 0 
    if wt[n-1]>W : 
        return knapSackRec(W, wt, val, n-1) 
    else :  
        return max(val[n-1]+knapSackRec(W-wt[n-1], wt, val, n-1), knapSackRec(W, wt, val, n-1)) 
val=[60,100,120]
wt=[10,20,30] 
W=50
print("0-1 Knapsack (Recursive) : ", knapSackRec(W, wt, val, 3)) 

# DP solution 
def knapSackDP(W, wt, val) : 
    n=len(wt) 
    dp=[[0 for _ in range(W+1)] for x in range(n+1)]  
    for i in range(1,n+1) : 
        for j in range(1, W+1) : 
            if wt[i-1]<=j : 
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-wt[i-1]]+val[i-1]) 
            else : 
                dp[i][j]=dp[i-1][j] 
    return dp[n][W] 
val=[60,100,120]
wt=[10,20,30] 
W=50
print("0-1 Knapsack (DP) : ", knapSackDP(W, wt, val))  
print("\n")



## Optimal strategy for a Game 
# Recursive solution - 1
def mVRec(arr, i, j, sum) : 
    if i+1==j : 
        return max(arr[i], arr[j]) 
    return max(sum-mVRec(arr, i+1, j, sum-arr[i]), sum-mVRec(arr, i, j-1, sum-arr[j])) 

def maxVal(arr) : 
    return mVRec(arr, 0, len(arr)-1, sum(arr)) 

arr=[25, 30, 4, 11, 6, 5] 
print("Max val in a game (Recursive-1) : ", maxVal(arr))

# Recursive solution - 2 
def mV(arr, i, j) : 
    if i+1==j : 
        return max(arr[i], arr[j]) 
    return max( min(mV(arr, i+2, j), mV(arr, i+1, j-1)) +arr[i], 
                min(mV(arr, i, j-2), mV(arr, i+1, j-1)) +arr[j] )
arr=[25, 30, 4, 11, 6, 5] 
print("Max val in a game (Recursive-2) : ", mV(arr, 0, 5)) 

# DP Solution 
def maxValDP(arr) : 
    n=len(arr) 
    dp=[[0 for x in range(n)] for y in range(n)] 

    for i in range(n-1) : 
        dp[i][i+1]=max(arr[i], arr[i+1]) 
    
    for gap in range(3, n, 2) : 
        for i in range(n-gap) : 
            j=i+gap 
            dp[i][j]=max( arr[i]+ min(dp[i+2][j], dp[i+1][j-1]), 
                          arr[j]+ min(dp[i][j-2], dp[i+1][j-1]) ) 
    return dp[0][n-1] 
# arr=[20,5,4,6,8,3] 
print("Max val in a game (DP) : ", maxValDP(arr)) 
print("\n") 


