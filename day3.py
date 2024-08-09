# Day - 3 
# Mathematics :
#   Prime factorization 
#   All divisors of a number - 3 approaches 


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
                print(i)
                x=x*i  
print("Prime Factors of 10 : ")                       
primeFactors(10)  
print("\n")

# All divisors of a number :
def alldiv1(n) :  # Naive approach 
    for i in range(1,n+1) :
        if n%i==0 :
            print(i)
print("All divisors of 9 : ")          
alldiv1(9)
print("\n") 

# concept - all divisors appear in pair 
def alldiv2(n) : # efficient solution but divisors necessarily need not be in order  
    i=1  
    while (i*i <= n) :
        if n%i==0 :
            print(i)
            if (i!=n//i) :
                print(n//i)
        i+=1 
print("All divisors of 8 :  (Not necessarily be in order) ")   
alldiv2(8) 
print("\n")

# prints all the divisors and in order 
def alldiv3(n) :  
    i=1 
    while (i*i)<=n :
        if n%i==0 : 
            print(i) 
        i+=1 
    while(i>=1) :
        if n%i==0 : 
            print(n//i) 
        i-=1
print("All divisors of 8 : (In order)")        
alldiv3(8)              