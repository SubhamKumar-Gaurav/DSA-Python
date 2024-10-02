# Day - 9
#   Print 1 to N using recursion 
#   Print N to 1 using recursion 
#   Sum of digits using recursion 
#   Palindrome check using recursion 


## Print 1 to N using recursion 
def recursion_1_to_n(n) :
    if n==0 :
        return 
    recursion_1_to_n(n-1) 
    print(n) 
print("Printing 1 to N using Recursion : ")
print(recursion_1_to_n(4))   


## Print N to 1 using recursion 
def recursion_n_to_1(n) :
    if n==0 :
        return 
    print(n)
    recursion_n_to_1(n-1) 
print("Printing N to 1 using recursion : ") 
print(recursion_n_to_1(4))


## Sum of digits using recursion  
def dsum(n) : 
    if n<10 :
        return n 
    return n%10 + dsum(n//10)
print("Sum of the digits : " , dsum(253)) 


## Palindrome check using recursion 
def isPalindrome(s,start,end) : 
    if start>=end :
        return True 
    return (s[start]==s[end]) and (isPalindrome(s,start+1,end-1)) 
print("Palindrome check for 'abca' : " , isPalindrome("abca",0,3)) 
print("Palindrome check for 'abba' : " , isPalindrome("abba",0,3)) 