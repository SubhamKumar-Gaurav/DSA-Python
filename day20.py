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

s=MyStack() 
s.push(10) 
s.push(20)
s.push(30)
print("Popped element : ",s.pop())
print("Peak element : ",s.peak())
print("Size of Stack : ",s.size())