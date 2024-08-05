# Day - 3 
# Mathematics 
#  GCD or HCF of a number 
#    (i)checking with each value 
#    (ii)Euclidean Algorithm 
#    (iii)Optimised Euclidean Algorithm 
#  LCM of a number - Naive approach, By Maths property 
#  Check Prime - 3 approaches 


import math 
# GCD of a number :
def gcd1(a,b) :   # Checking with each value 
    m=min(a,b) 
    while m!=0 :
        if a%m==0 and b%m==0 :
            return m 
        else :
            m=m-1 
print(gcd1(12,15))     

def gcd2(a,b) :  # Euclidean Algorithm 
    while a!=b :
        if a>b :
            a=a-b 
        else :
            b=b-a 
    return a
print(gcd2(10,15))            

def gcd3(a,b) :  # Optimised Euclidean Algorithm 
    if b==0 :
        return a 
    return gcd3(b,a%b) 
print(gcd3(12,15))


# LCM of a number : 
# Approach - 1  (Naive approach)
def lcm1(a,b) :
    m=max(a,b) 
    while True :
        if m%a==0 and m%b==0 :
            return m 
        m+=1 

# Approach - 2  (By Maths property)
# WKT :  a*b=LCM(a,b)*GCD(a,b) 
def gcd(a,b) :
    if b==0 :
        return a 
    return gcd(b,a%b)
def lcm(a,b) :
    return (a*b)//gcd(a,b)
print(lcm(10,12))


# Check for Prime : 
def prime1(n) :      # Naive approach 
    for i in range(2,n) :
        if n%i==0 :
            return False 
    return True 
print(prime1(7))    
  
def prime2(n) :    # a little efficient approach with time comp: O(root(n))
    i=2 
    while (i*i)<=n :
        if n%i==0 :
            return False 
        i+=1 
    return True 
print(prime2(36))     

def prime3(n) :  # super efficient approach , time : O(root(n)/6) 
    if n==1 :
        return False 
    elif n==2 or n==3 :
        return True 
    elif n%2==0 or n%3==0 :
        return False 
    else :
        i=5 
        while( i*i <= n ) :
            if n%i==0 or n%(i+2)==0 :
                return False
            i+=6 
        return True     
print(prime3(101))     

