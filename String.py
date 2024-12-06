## String 
#    


## Basics 
#   Characters 'A' to 'Z' are stored as values from 65 to 90 
#   Characters 'z' to 'z' are stored as values from 97 to 122



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
print("Raw strings : ",s3)