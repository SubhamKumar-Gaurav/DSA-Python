## Advanced List  
#   Left rotate by d places 




## Left rotate by d places 
print("Left rotate by d places ")
# Using List slicing
print("Using List Slicing : ")
l=[10,20,30,40,50]
d=2 
l=l[d:]+l[:d] 
print(l) 
print("\n") 

# Using deque
print("Using deque : ")
from collections import deque
l=[10,20,30,40,50]
d=2 
dq=deque(l) 
dq.rotate(-d) 
l=list(dq) 
print(l) 
print("\n") 

# Using pop and append 
def leftRotate(l,d) : 
    for i in range(d) : 
        l.append(l.pop(0))
    print(l)
l=[10,20,30,40,50]
d=3 
print("Using pop and append")
leftRotate(l,d) 
print("\n")   

# Using reverse function  Time: O(n) 
def reverse(l,b,e) : 
    while b<e : 
        l[b], l[e]= l[e], l[b]
        b+=1 
        e-=1 
def leftRotate(l,d) : 
    n=len(l)
    reverse(l,0,d-1) 
    reverse(l,d,n-1)
    reverse(l,0,n-1)
    return l
l=[10,20,30,40,50]
d=3
print(leftRotate(l,d))