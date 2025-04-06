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
            if arr[i]>arr[j] : 
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
    r=len(tail) 
    while l<r : 
        m=l+(l+r)//2 
        if tail[m]>x : 
            r=m 
        else : 
            l=m+1 
    return m
print("Longest Increasing Subsequence : ",lis2(arr))
print("\n")
