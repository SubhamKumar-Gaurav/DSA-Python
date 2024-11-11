# Day - 14 
#    Linked List 
#    Traversing through a Linked List 
#    Search in Linked List 


## Simple Linked List implementation in Python 
class Node : 
    def __init__(self,k) : 
        self.key=k 
        self.next=None 
temp1=Node(10)
temp2=Node(20)
temp3=Node(30) 
temp1.next=temp2 
temp2.next=temp3 
head=temp1 

## Alternate shorter implementation  
head=Node(10) 
head.next=Node(20) 
head.next.next=Node(30) 



## Traversing through a Linked List : 
class Node : 
    def __init__(self,k) : 
        self.key=k 
        self.next=None

def printList(head) :  
    curr=head 
    while curr!=None : 
        print(curr.key, end=" ") 
        curr=curr.next 

head=Node(10) 
head.next=Node(20) 
head.next.next=Node(15) 
head.next.next.next=Node(30) 
print("Traversing through a Linked List : ")
printList(head) 
print("\n") 


## Search in Linked List 
class Node : 
    def __init__(self,k) :  
        self.key=k  
        self.next=None 
def searchList(head,x) : 
    curr=head
    i=1 
    while curr!=None : 
        if curr.key==x : 
            return i 
        i+=1
        curr=curr.next 
    return -1 
# [10,15,20,25]
head=Node(10) 
head.next=Node(15)
head.next.next=Node(20) 
head.next.next.next=Node(25) 
x=20
print("Search in Linked List : ")
print(searchList(head,x),"\n") 