## Day - 20 
#    Stacks 
#    Linked List implementation of Stack


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


import math
## Linked List implementation of Stack 
class Node : 
    def __init__(self,d) : 
        self.data=d 
        self.next=None

class MyStack :  
    def __init__(self) : 
        self.head=None 
        self.sz=0 
    def push(self,x) : 
        temp=Node(x) 
        temp.next=self.head 
        self.head=temp 
        self.sz=self.sz+1 
    def size(self) : 
        return self.sz 
    def peak(self) : 
        if self.head==None : 
            return math.inf 
        return self.head.data 
    def pop(self) : 
        if self.head==None : 
            return math.inf 
        res=self.head.data
        self.head=self.head.next 
        self.sz=self.sz-1 
        return res 
print("Linked List implementation of Stack ")
s=MyStack() 
s.push(10) 
s.push(20)
s.push(30)
print("Popped element : ",s.pop())
print("Peak element : ",s.peak())
print("Size of Stack : ",s.size())
print("\n")  



## Applications of Stack : 
# Function calls 
# Balanced paranthesis
# Reversing items 
# Infix to postfix and prefix 
# Evaluation of postfix/prefix 
# Stock span problems and its variants 
# Undo/Redo  or  Forward/Backward 


## Check for Balanced Paranthesis 
def isMatching(a,b) : 
    if (a=="(" and b==")") or (a=="[" and b=="]") or (a=="{" and b=="}") :
        return True 
    else : 
        return False

def isBalanced(s) : 
    stack=[] 
    for x in s : 
        if x in ("(", "[", "{") : 
            stack.append(x) 
        else : 
            if not stack : 
                return False 
            elif isMatching(stack[-1],x)==False : 
                return False 
            else : 
                stack.pop()
    if stack : 
        return False 
    else : 
        return True 
print("Check for Balanced Paranthesis : ")
s1="([])"
s2="((())"
s3="([)]"
s4="{}([()])"
print("([]) : ", isBalanced(s1))
print("((()) : ", isBalanced(s2))
print("([)] : ", isBalanced(s3))
print("{}([()]) : ", isBalanced(s4))
print("\n")