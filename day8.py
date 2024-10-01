# Day - 8 
# Recursion 
#    factorial using recursion 
#    fibonacci using recursion  


## Factorial using recursion  
def fact(n) :
    if n==0 :
        return 1
    return n*fact(n-1) 

print("Factorial of 5 using recursion : " , fact(5)) 


## Fibonacci using recursion  
def fibo(n) :
    if n==0 :
        return 0 
    if n==1 :
        return 1 
    return fibo(n-1)+fibo(n-2) 

print("6th term in Fibonacci series : " , fibo(6))