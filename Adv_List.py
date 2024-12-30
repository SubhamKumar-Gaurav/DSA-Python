## Advanced List  
#   Left rotate by d places 




## Left rotate by d places 
print("Left rotate by d places ")
print("Using String Slicing : ")
l=[10,20,30,40,50]
d=2 
l=l[d:]+l[:d] 
print(l) 
print("\n") 

print("Using deque : ")
from collections import deque
l=[10,20,30,40,50]
d=2 
dq=deque(l) 
dq.rotate(-d) 
l=list(dq) 
print(l) 
print("\n") 