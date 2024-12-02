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