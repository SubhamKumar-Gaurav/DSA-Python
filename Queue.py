##  Queue 
#      Queue implementation - 
#           * Using List, collections.deque, queue.Queue 
#      Linked List implementation of Queue 


## Queue implementation using List 
print("Queue implementation using List : ")
q=[]
q.append(10)
q.append(20)
q.append(30) 
print("q : ",q) 
print(q.pop(0)) 
q.append(40) 
print(q.pop(0))  
print(len(q)) 
print(q[0]) 
print(q[-1])  
print("\n") 
 
## Method - 2  (Using deque) 
print("Queue implementation using Deque : ")
from collections import deque 
q=deque() 
q.append(10)
q.append(20)
q.append(30) 
print(q) 
print(q.popleft()) 
q.append(40) 
print(q)
print(q.popleft()) 
print(len(q)) 
print(q[0]) 
print(q[-1]) 
print("\n") 


## Linked List implementation of Queue
class Node : 
    def __init__(self,k) : 
        self.key=k 
        self.next=None 

class MyQueue : 
    def __init__(self) : 
        self.front=None 
        self.rear=None 
        self.sz=0 
    def size(self) : 
        return self.sz 
    def isEmpty(self) : 
        return (self.sz==0) 
    def getFront(self) : 
        return self.front.key 
    def getRear(self) : 
        return self.rear.key 
    def enque(self, x) :   
        temp=Node(x) 
        if self.rear==None : 
            self.front=temp 
        else : 
            self.rear.next=temp 
        self.rear=temp 
        self.sz=self.sz+1 
    def deque(self) : 
        if self.front==None : 
            return None 
        else : 
            res=self.front.key 
            self.front=self.front.next 
            if self.front==None : 
                self.rear=None 
            self.sz=self.sz-1 
            return res 
print("Linked List implementation of Queue : ")
q=MyQueue() 
q.enque(10)
q.enque(20)
q.enque(30) 
print(q.deque())
print("\n")


## Queue implementation using Circular List 
class MyQueue : 
    def __init__(self,c) : 
        self.l=[None]*c 
        self.cap=c 
        self.size=0 
        self.front=0 
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
    def enque(self,x) : 
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


## Implement stack using queue  
class Stack : 
    def __init__(self) : 
        self.q1=deque() 
        self.q2=deque()  
    
    def push(self,x) : 
        self.q2.append(x) 
        while self.q1 : 
            self.q2.append(self.q1.popleft()) 
        self.q1, self.q2=self.q2, self.q1  
    def pop(self) : 
        if self.q1 : 
            self.q1.popleft() 
    def top(self) : 
        if self.q1 : 
            return self.q1[0] 
        else : 
            return None 
    def size(self) : 
        return len(self.q1) 
    
