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


