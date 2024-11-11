# Day - 14 
#    Linked List 


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