## Deque 


# 4 main operations of Deque 
#  insertFront, insertRear, deleteFront, deleteRear 
 
print("Program - 1 : ")
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
print("\n")
 

print("Program - 2 : ")
from collections import deque 
d=deque([10,20,30,40]) 
d.insert(2,10)    # inserting 10 at position 2 
print("Inserting 10 at position 2 : ",d)
print("Counting 10 : ",d.count(10)) 
d.remove(10)
print("Removing first occurence of 10 : ",d) 
d.extend([50,60]) 
print("Inserting 50 , 60 at rear : ",d) 
d.extendleft([15,25]) 
print("Inserting 15, 25 at front : ",d)  
print("\n")

print("Program - 3 : ") 
from collections import deque 
d=deque([10,20,30,40,50]) 
d.rotate(2) 
print("Rotation of 2 in clockwise direction : ", d ) 
d.rotate(-2) 
print("Rotation of 2 in anti-clockwise direction : ", d , " [gives original deque] ") 
d.reverse() 
print("Reversed deque : ", d ) 

