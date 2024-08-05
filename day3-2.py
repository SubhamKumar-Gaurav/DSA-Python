# Day - 3.2 
# Mathematics :
#   Prime factorization 
#   All divisors of a number - 3 approaches 


# Prime factorization : 
# the below program is just a naive approach, this code can be optimised further 
def isPrime(n) :
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
    return True 

def primeFactors(n) :
    for i in range(2,n+1) :
        if isPrime(i) :
            x=i 
            while n%x==0 :
                print(i)
                x=x*i  

# print(primeFactors(100))       
# print(primeFactors(10))   

# All divisors of a number :
def alldiv1(n) :  # Naive approach 
    for i in range(1,n+1) :
        if n%i==0 :
            print(i)
print(alldiv1(9))
# def alldiv2(n) :  # all divisors appear in pair 
