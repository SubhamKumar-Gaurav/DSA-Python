## Deque 
#   Implementation using 
#      from collections module 
#      using Linked list
#      using List 


# 4 main operations of Deque 
#  insertFront, insertRear, deleteFront, deleteRear 

print("Program - 1 : ")
from collections import deque
from typing import Any 
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
print("\n")
 

print("Program - 4 : ") 
from collections import deque 
d=deque([10,20,30,40,50]) 
print("3rd element : ",d[2])
d[2]=100 
print("Updating 3rd element to 100 : ",d) 
print("Front element : ",d[0]) 
print("Rear element : ",d[-1]) 
print("\n") 




## Linked List implementation of Deque 
class Node : 
    def __init__(self, k) : 
        self.key=k 
        self.prev=None 
        self.next=None 

class MyDeque : 
    def __init__(self) : 
        self.front=None 
        self.rear=None 
        self.sz=0 
    def size(self) : 
        return self.sz 
    def isEmpty(self) : 
        return self.sz==0 
    def insertRear(self,x) : 
        temp=Node(x) 
        if self.rear==None : 
            self.front=temp 
        else : 
            self.rear.next=temp 
            temp.prev=self.rear 
        self.rear=temp 
        self.sz=self.sz+1 
    def deleteFront(self) : 
        if self.front==None : 
            return None 
        else : 
            res=self.front.key 
            self.front=self.front.next 
            if self.front==None : 
                return None 
            else : 
                self.front.prev=None 
            self.sz=self.sz+1 
            return res 
d=MyDeque() 
d.insertRear(10) 
d.insertRear(20) 
d.insertRear(30) 
d.deleteFront()


## List implementation of Deque 
class MyDeque : 
    def __init__(self, c) : 
        self.l=[None]*c 
        self.cap=c 
        self.sz=0 
        self.front=0 
    def deleteFront(self) : 
        if self.sz==0 : 
            return None 
        else : 
            res=self.l[self.front] 
            self.front=(self.front+1)%self.cap 
            self.sz=self.sz-1 
            return res 
    def insertFront(self,x) : 
        if self.sz==self.cap : 
            return 
        else : 
            self.front=(self.front-1)%self.cap 
            self.l[self.front]=x 
            self.sz=self.sz+1 
    def insertRear(self,x) : 
        if self.sz==self.cap : 
            return 
        new_rear=(self.front+self.sz)%self.cap 
        self.l[new_rear]=x 
        self.sz=self.sz+1 
    def deleteRear(self) : 
        sz=self.sz 
        if sz==0 : 
            return None  
        else :
            rear=(self.front+sz-1)%self.cap  
            self.sz=self.sz-1 
            return self.l[rear] 
print("List implementation of Deque : ")
d=MyDeque(4)  
print(d)
d.insertRear(10) 
print("insertRear(10) : ", d)
d.insertFront(20) 
print("insertFront(20) : ", d) 
d.insertFront(30) 
print("insertFront(30) : ", d) 
d.deleteFront() 
print("deleteFront : " , d) 
d.deleteRear() 
print("deleteRear() : ", d) 
print("\n") 