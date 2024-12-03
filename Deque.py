## Deque 


# 4 main operations of Deque 
#  insertFront, insertRear, deleteFront, deleteRear 
 
from collections import deque 
d=deque() 
d.append(10)
d.append(20)
d.append(30) 
d.appendleft(40) 
print("Deque d : ",d) 
print("pop function : ",d.pop()) 
print("popleft function : ",d.popleft()) 
print(d)