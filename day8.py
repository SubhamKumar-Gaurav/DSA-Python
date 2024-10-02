# Day - 8 
# Recursion 
#    factorial using recursion 
#    fibonacci using recursion  
#    basic recursion practice

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

## Recursion practice - I 
def fun(n) :
    if n==0 :
        return 
    print(n)
    fun(n-1)
    print(n) 
print("Output for the above function : ") 
print(fun(3))

def fun(n) : 
    if n==0 :
        return 
    fun(n-1) 
    print(n) 
    fun(n-1) 
print("Output for above fn. : ") 
print(fun(3))  

## Recursion for practice - II 
def fun(n) :
    if n<=1 :
        return 0 
    else :
        return 1+fun(n/2) 
print("Output of above function : ") 
print(fun(16))

def bin(n) :
    if n==0 :
        return 
    bin(n//2) 
    print(n%2) 
print("Binary representation of the number 13 : ")  
print(bin(13)) 

