# Day - 2
# Mathematics : 
#   Sum of Natural nos. 
#   Count Digits 
#   Palindrome number 
#   Factorial number (iterative implementation, recursive approach) 


# Sum of natural nos. 
def sum1(n) :
    return n*(n+1)//2 

def sum2(n) :
    ans=0 
    for i in range(1,n+1) :
        ans=ans+i 
    return ans 
print(sum2(10))   

def sum3(n) :
    ans=0 
    for i in range(n) :
        temp=0
        for j in range(i+1) :
            temp+=1 
        ans+=temp 
    return ans 
print(sum3(11))

# Count digits 
def cd(n) :
    c=0 
    while(n>0) :
        n=n//10 
        c+=1 
    return c 
print(cd(8756))    

# Palindrome number 
def isPal(n) :
    rev=0 
    temp=n 
    while(temp>0) :
        ld=temp%10 
        rev=(rev*10)+ld 
        temp=temp//10 
    return rev==n 
print(isPal(121))   

# Factorial of a number 
# Iterative implementation 
def fact1(n) :
    ans=1 
    for i in range(2,n+1) :
        ans=ans*i 
    return ans 
print(fact1(5))  

# Recursive approach 
def fact2(n) :
    if n==0 :
        return 1 
    return n*fact2(n-1) 
print(fact2(6))

        