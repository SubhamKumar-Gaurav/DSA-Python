##  Queue 
#      Queue implementation - List, collections.deque, queue.Queue 



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