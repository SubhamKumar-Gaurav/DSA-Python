# Day - 3 
# Mathematics :
#   Prime factorization 
#   All divisors of a number - 3 approaches 
#   Sieve of Eratosthenes - 3 approaches (prime nos. upto n)
#   Computing power - 2 approaches 
#   Iterative Power - Binary Exponentiation 

# Prime factorization : 
# the below program is just a naive approach, this code can be optimised further 
def isPrime(n) :  # for checking prime number 
    if n==1 :
        return False 
    elif n==2 or n==3 :
        return True 
    elif n%2==0 or n%3==0 :
        return False 
    i=5 
    while i*i <= n :
        if n%i==0 or n%(i+2)==0 :
            return False 
        i+=1
    return True 

def primeFactors(n) :
    for i in range(2,n+1) :
        if isPrime(i) :
            x=i 
            while n%x==0 :
                print(i,end=" ")
                x=x*i  
print("Prime Factors of 10 : ")                       
primeFactors(10)  
print("\n")


# All divisors of a number :
def alldiv1(n) :  # Naive approach 
    for i in range(1,n+1) :
        if n%i==0 :
            print(i,end=" ")
print("All divisors of 9 : ")          
alldiv1(9)
print("\n") 

# concept - all divisors appear in pair 
def alldiv2(n) : # efficient solution but divisors necessarily need not be in order  
    i=1  
    while (i*i <= n) :
        if n%i==0 :
            print(i,end=" ")
            if (i!=n//i) :
                print(n//i,end=" ")
        i+=1 
print("All divisors of 8 :  (Not necessarily be in order) ")   
alldiv2(8) 
print("\n")

# prints all the divisors and in order 
def alldiv3(n) :  
    i=1 
    while (i*i)<=n :
        if n%i==0 : 
            print(i,end=" ") 
        i+=1 
    while(i>=1) :
        if n%i==0 : 
            print(n//i,end=" ") 
        i-=1
print("All divisors of 8 : (In order)")        
alldiv3(8)
print("\n")              


# Sieve of Eratosthenes : 
# approach 1 
def sieve1(n) :
    for i in range(2,n+1) :
        if isPrime(i) :
            print(i,end=" ")
print("Prime numbers upto 10 : ")            
sieve1(10)            
print("\n")

# Approach 2 :
def sieve2(n) :
    isprime=[True]*(n+1)
    if n==1 :
        return False
    
    i=2 
    while i*i <= n :
        if isprime[i] :
            for j in range(2*i,n+1,i) : 
                isprime[j]=False 
        i+=1 
    for i in range(2,n+1) :
        if isprime[i] :
            print(i,end=" ") 
print("Prime nos. upto 10 :")            
print(sieve2(10))
print("\n")             

# Approach 3 :  (more optimized solution)  Time ; O(nloglogn) 
def sieve3(n) :
    if n==1 :
        return 
    isprime=[True]*(n+1) 
    i=2 
    while i <= n :
        if isprime[i] :
            print(i,end=" ")
            for j in range(i*i,n+1,i) :
                isprime[j]=False  
        i+=1 
print("Prime nos upto 100 : ")        
sieve3(100)  
print("\n")                


# Computing Power :
# Approach 1 : Naive solution 
def power1(x,n) :
    a=1 
    for i in range(n) :
        a=a*x 
    return a 
print("5 raised to the power of 3 : ")
print(power1(5,3))
print("\n") 

# Approach 2 : 
def power2(x,n) :
    if n==1 :
        return x 
    temp=power2(x,n//2) 
    temp=temp*temp 
    if n%2==0 :
        return temp 
    else :
        return temp*x 
print("5 raised to the power of 6 :")  
print(power2(5,6)) 
print("\n")   


# Iterative power - Binary Exponentiation 
def power3(x,n) :
    temp=1  
    while n>0 : 
        if n%2==1 :
            temp=temp*x 
        x=x*x 
        n=n//2 
    return temp
print("2 raised to the power of 10 : ") 
print(power3(2,10))  
print("\n")      

def power4(x,n) :   # using AND operator 
    res=1 
    while n>0 :
        if n&1 :
            res=res*x 
        x=x*x 
        n=n//2 
    return res 
print("3 raised to the power of 10 :") 
print(power4(3,10))       