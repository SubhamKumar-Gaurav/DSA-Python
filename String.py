## String 
#   Basics 
#   Escape sequemces and raw strings  
#   Formatted string in Python 
#   String comparison in Python 



## Basics 
#   Characters 'A' to 'Z' are stored as values from 65 to 90 
#   Characters 'z' to 'z' are stored as values from 97 to 122
print(ord("a")) 
print(ord("A"))
print(chr(97)) 
print(chr(65)) 


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