## Day - 20 
#    Stacks 

## Stacks in Python (4 ways)
# 1. Using List 
print("Stack implementation using List : ")
stack=[] 
stack.append(10)
stack.append(20)
stack.append(30) 
print("pop operation : ", stack.pop())
top=stack[-1] 
print("peak() : ", top)
size=len(stack) 
print("size() : ",size) 
print("\n") 


# 2. Using deque 
print("Stack implementation using Deque : ")
from collections import deque 
stack=deque()
stack.append(10)
stack.append(20)
stack.append(30) 
print("pop operation : ", stack.pop())
top=stack[-1] 
print("peak() : ", top)
size=len(stack) 
print("size() : ",size) 
print("\n")