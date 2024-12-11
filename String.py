## String 
#   Basics 
#   Escape sequemces and raw strings  
#   Formatted string in Python 
#   String comparison in Python 
#   String operations 
#   Reverse a string 
#   Check if string is rotated 
#   Check for Palindrome 
#   Check if a string is subsequence of other 
#   Check for Anagram
#   Leftmost repeating character 
#   Leftmost non-repeating character 
#   Reverse words in a string 


## Basics 
print("Characters 'A' to 'Z' are stored as values from 65 to 90") 
print("Characters 'z' to 'z' are stored as values from 97 to 122")
print(ord("a")) 
print(ord("A"))
print(chr(97)) 
print(chr(65)) 
print("\n")

## Escape sequences and raw strings 
#   s='Welcome to Geek's Course'   (Will throw an error)
#   print(s) 

# Corrected code : 
print("Corrected code (Escape sequences)")
s='Welcome to Geek\'s course' 
print("s : ",s) 
print("\n") 

s1="Hi, \nWelcome to the course" 
print(s1) 
print("\n")

## Raw strings 
print("Raw strings : ")
s2="C:\project\name.py"
print(s2) 

s3=r"C:\project\name.py"
print("Raw string : ",s3)  
print("\n")



## Formatted string in Python 
# Method - 1: USing % 
name="ABC" 
course="Python Course"
s="Welcome %s to the %s"%(name,course)
print("Formatted string using (%) : ",s)  

# Method - 2 : USing format() method 
s="Welcome {0} to the {1}".format(name,course)
print("Using format() method : ", s)

# Method - 3 : USing f-string 
s=f"Welcome {name} to the {course}" 
print("USing f string : ", s) 

a="10"
b="20"
print(f"Sum of {a} and {b} is {a+b}  [String concatenation]")
a=10 
b=20 
print(f"Sum of {a} and {b} is {a+b}")
print(f"Product of {a} and {b} is {a*b}") 

s1="ABC"
s2="abc" 
print(f"Lowercase of {s1} is {s1.lower()}")
print(f"Uppercase of {s2} is {s2.upper()}") 
print("\n")


## String comparison in Python 
print("String Comparison in Python : ")
s1="geeksforgeeks" 
s2="ide" 
print("s1<s2 : " , s1<s2)  # Compared based on Unicode values of first character 
print("s1<=s2 : " , s1<=s2)
print("s1>s2 : " , s1>s2)
print("s1>=s2 : " , s1>=s2)
print("s1==s2 : ",s1==s2) 
print("s1!=s2 : ",s1!=s2) 
print("abcd > abc : " , "abcd" > "abc" ) 
print("ZAB > ABC : " , "ZAB" > "ABC" ) 
print("abc > ABC : " , "abc" > "ABC" ) 
print("x > abcd : ", "x" > "abcd")  
print("\n") 


## String Operations in Python (Part - 1) 
print("String Operations in Python (Part - 1)") 

print("Program - 1 (Check for substring)")
s1="geeksforgeeks" 
s2="geeks" 
print("s2 in s1 : ",s2 in s1) 
print("s2 not in s1 : ", s2 not in s1) 
print("\n") 

print("Program - 2 (String Concatenation)") 
s1="geeks" 
s2="forgeeks" 
print("s1+s2 : ", s1+s2) 
s4="Welcome to "+ s1 + s2
print(s4) 
print("\n") 

print("Program - 3 (Find position of a substring)") 
s1="geeksforgeeks" 
s2="geeks" 
print(".index() gives index of first occurence : ", s1.index(s2)) 
print(".rindex() gives index of last occurence : ", s1.rindex(s2))  
print("Index in a given range : ", s1.index(s2,0,13)) 
print("Index in a given range : ", s1.index(s2,1,13))   
print("\n") 



## String Operations in Python (Part - 2) 
print("String Operations in Python (Part - 2)")   
s1="geeks" 
print("length of s1 : " , len(s1))
print("s1.upper() : ", s1.upper()) 
print("s1.lower() : ", s1.lower()) 
print("s1.islower() : ", s1.islower()) 
print("s1.isupper() : ", s1.isupper()) 
print("\n") 

print("startswith and endswith function")
s="GeeksforGeeks Python Course" 
print("startswith : ",s.startswith("Geeks")) 
print("endswith : ",s.endswith("Course")) 
print("startswith fn. with parameter : ", s.startswith("Geeks",1)) 
print("startswith fn. with parameter : ", s.startswith("Geeks",8,len(s)))  
print("\n") 


print("split method: ") 
s1="geeks for geeks" 
print("s1.split() : ", s1.split())

s2="geeks, for , geeks" 
print("s2.split(',') : ", s2.split(",")) 
print("\n") 

print("join method : ")
l=["geeksforgeeks", "python", "course"] 
print(" ".join(l)) 
print(",".join(l)) 
print(", ".join(l)) 
print("\n") 

print("strip method : ") 
s="__geeksforgeeks___" 
print(s.strip("_")) 
print(s.lstrip("_")) 
print(s.rstrip("_"))    
s1="geeks_for_geeks"
print(s1.strip("_")) 
s2="geeks for geeks"
print(s2.strip(" ")) 
print("\n") 

print("find method : ") 
s1="geeks for geeks" 
print(s1.find("geeks"))
print(s1.find("gfg")) 
print(s1.find("geeks",1,len(s1)))
print("\n")  


## Reverse a string 
s="geek" 
rev=""
for i in s : 
    rev = i + rev 
print("Reverse of s (method - 1): ", rev)  
print("Reverse of s (method - 2): ", s[::-1])  
print("\n")  


print("Check if string is rotated : ") 
s1="ABCD"
s2="CDAB" 
def areRotations(s1,s2) : 
    if len(s1)!=len(s2) : 
        return False 
    temp="" 
    temp=s1+s1 
    return temp.find(s2)==-1  
print("ABCD and CDAB : ",areRotations(s1,s2)) 
print("ABAB and ABBA : ",areRotations("ABAB","ABBA")) 
print("\n") 



## Check for Palindrome 
print("Check for Palindrome : ") 
print("Method - 1  Using two pointers ")   
def isPalindrome(s) : 
    n=len(s) 
    low=0 
    high=n-1 
    while low<high : 
        if s[low]!=s[high] : 
            return False 
        low+=1 
        high-=1 
    return True 
s1="abba"
s2="aBA" 
print("abba : ", isPalindrome(s1))
print("aBA : ",isPalindrome(s2))
print("\n")

print("Method - 2   Using string reversal ")
def Palindrome(s) : 
    return s[::]==s[::-1] 
s1="ABBA" 
print("ABBA : ",Palindrome(s1)) 
s2="Aba"
print("Aba : ",Palindrome(s2)) 
print("\n") 


##  Check if a string is subsequence of other 
print("Check for subsequence : ")
def isSubsequence(s1,s2) : 
    m=len(s1) 
    n=len(s2) 
    i=0 
    j=0 
    while i<m and j<n : 
        if s1[i]==s2[j] : 
            i+=1 
            j+=1 
        else : 
            i+=1 
    if j==n : 
        return True 
    return False 

s1="ABCD"
s2="AD" 
print("ABCD and AD : ",isSubsequence(s1,s2)) 
s1="geeksforgeeks" 
s2="grges" 
print("geeksforgeeks and grges : ", isSubsequence(s1,s2))
s1="ABCDE"
s2="AED"
print("ABCDE and AED : ", isSubsequence(s1,s2))  
print("\n")  


 
## Check for Anagram 
print("Check for Anagram : ") 
print("Naive approach with Time : O(n logn )")
def Anagram(s1,s2) : 
    if len(s1)!=len(s2) : 
        return False 
    s1=sorted(s1) 
    s2=sorted(s2) 
    return s1==s2 
s1="listen" 
s2="silent" 
print("listen and silent : ",Anagram(s1,s2)) 
print("aab and abb : ",Anagram("aab","abb")) 
print("\n") 


print("Efficient solution with Time : O(n)") 
def areAnagram(s1,s2) : 
    if len(s1)!=len(s2) : 
        return False 
    counter=[0]*256 
    for i in range(len(s1)) : 
        counter[ord(s1[i])]+=1     
        counter[ord(s2[i])]-=1    
    for x in counter : 
        if x!=0 : 
            return False 
    return True  
print("listen and silent : ", areAnagram("listen", "silent"))  
print("aab and abb : ",areAnagram("aab","abb"))
print("\n") 



## Leftmost repeating character 
print("Leftmost repeating character :  ")  
print("Approach - 1  [Naive approach]   Time: O(n^2)") 
def leftmost1(s) : 
    for i in range(len(s)) : 
        for j in range(i+1,len(s)) : 
            if s[i]==s[j] : 
                return i 
    return -1   
s1="abbccd"
s2="geeksforgeeks"
print("abbccd : ", leftmost1(s1)) 
print("geeksforgeeks : ", leftmost1(s2)) 
print("\n") 


print("Approach - 2  [Better approach]   Time: O(n)") 
def leftmost2(s) : 
    count=[0]*256 
    for i in range(len(s)) : 
        count[ord(s[i])]+=1 
    for i in range(len(s)) : 
        if count[ord(s[i])]>1 : 
            return i 
    return -1 
s3="geeksforgeeks" 
print("geeksforgeeks : ", leftmost2(s3)) 
s4="abcd" 
print("abcd : ", leftmost2(s4)) 
print("\n") 