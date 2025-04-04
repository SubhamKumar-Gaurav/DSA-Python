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


# Memoization 
# Fibonacci using Recursion 
def fibo(n) : 
    if n==0 or n==1 : 
        return n 
    return fibo(n-1)+fibo(n-2) 
print("Fibonacci (Recursion) : ",fibo(7))


# Fibonacci using DP 
memo=[None]*100   # Assumption n<100 
def fib(n) : 
    if memo[n]!=None : 
        return memo[n] 
    if n==0 or n==1 : 
        memo[n]=n 
    else : 
        memo[n]=fib(n-1)+fib(n-2) 
    return memo[n] 
print("Fibonacci (DP) : ", fib(7)) 
print("\n")
