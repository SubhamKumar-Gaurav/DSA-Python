# Adv Queue and Deque 
#   Queue implementation using Circular List 
#   Implement Stack using Queue 
#   Reverse a Queue 
#   Generate first n numbers with the given digits 
#   Design a data structure with min/max operations 
#   Maximums of all subarrays of size k 
#   First Circular Tour 


## Queue implementation using Circular List   
class myQueue: 
    def __init__(self, c) : 
        self.l=[None]*c 
        self.cap=c  
        self.size=0 
        self.front=0 

    def isEmpty(self) : 
        return self.size==0

    def getFront(self) : 
        if self.size==0 : 
            return None 
        else : 
            return self.l[self.front] 
    
    def getRear(self) : 
        if self.size==0 : 
            return None 
        else : 
            rear=(self.front+self.size-1)%self.cap 
            return self.l[rear]
    
    def enque(self, x) : 
        if self.size==self.cap : 
            return 
        else : 
            rear=(self.front+self.size-1)%self.cap 
            rear=(rear+1)%self.cap 
            self.l[rear]=x 
            self.size=self.size+1 
    
    def deque(self) : 
        if self.size==0 : 
            return None 
        else : 
            res=self.l[self.front] 
            self.front=(self.front+1)%self.cap 
            self.size=self.size-1 
            return res 

    def __str__(self):    # Custom string representation for the queue
        if self.size == 0:
            return "Queue is empty"
        items = []
        for i in range(self.size):
            index = (self.front + i) % self.cap
            items.append(str(self.l[index]))
        return " -> ".join(items)

print("Queue implementation using circular list : ")
q=myQueue(4) 
q.enque(10)
q.enque(20)
q.enque(30)
print(q)
print(q.deque())
print(q)
print(q.size)
print(q.getFront())
print(q.getRear()) 
print(q.isEmpty())
print("\n") \


## Implement Stack using Queue 
# push - O(n) ;  other ops - constant time 
from collections import deque
class myStack: 
    def __init__(self) : 
        self.q1=deque() 
        self.q2=deque()  
    
    def push(self, x) : 
        self.q2.append(x) 
        while self.q1 : 
            self.q2.append(self.q1.popleft()) 
        self.q1, self.q2 = self.q2, self.q1 
    
    def pop(self) : 
        if self.q1 : 
            return self.q1.popleft()
        return None 

    def top(self) : 
        if self.q1 : 
            return self.q1[0] 
        else : 
            return None 
        
    def size(self) : 
        return len(self.q1) 

    def __str__(self):    # Custom string representation of the stack
        return "Stack (Top -> Bottom): " + " -> ".join(map(str, self.q1))
print("Stack implementation using Queue : ")
q=myStack()
q.push(10)
q.push(20)
q.push(30)
print(q)
print(q.pop()) 
print(q)
print('\n') 


## Reverse a Queue 
print("Reversing a Queue : ")
# 1. Iterative solution 
from collections import deque
def reverseQueue(q) : 
    st=[] 
    while q : 
        st.append(q.popleft())
    while st : 
        q.append(st.pop())
    return q
print("Iterative solution: ")
q=deque() 
q.append(20)
q.append(30)
q.append(10)
q.appendleft(40)
print("Before : ",q)
print("After : ", reverseQueue(q)) 
print()

# 2. Recursive solution 
print("Recursive solution: ")
def revQ(q) : 
    if len(q)==0 : 
        return 
    x=q.popleft() 
    revQ(q)
    q.append(x) 
q=deque() 
q.append(1)
q.append(3)
q.append(2)
q.appendleft(4)
print("Before : ",q)
revQ(q)
print("After : ",q)
print("\n") 


## Generate first n numbers with the given digits - 5, 6
# Simple efficient approach 
def printFirstN(n) : 
    q=deque() 
    q.append("5")
    q.append("6")
    for i in range(n) : 
        curr=q.popleft() 
        print(curr, end=" ") 
        q.append(curr+"5") 
        q.append(curr+"6") 
print("Generate first n numbers with the given digits : ")
print("Simple solution: ", end=" ")
printFirstN(10) 
print()

# Optimised efficient approach 
def firstN(n) : 
    q=deque() 
    q.append("5")
    q.append("6")
    i=0
    while (i+len(q))<n : 
        curr=q.popleft() 
        print(curr, end=" ")
        q.append(curr+"5") 
        q.append(curr+"6") 
        i+=1 
    while i<n : 
        print(q.popleft(), end=" ")
        i+=1 
print("Optimised solution : ", end=" ")
firstN(10) 
print("\n") 