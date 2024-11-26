# Day - 16 
#     Circular Linked List Traversal 
#     Insert at beginning 
#     Insert at end 


class Node : 
    def __init__(self,key) :
        self.key=key 
        self.next=None

## Circular Linked List Traversal  
def printCircular(head) : 
    if head==None : 
        return 
    print(head.key, end=" ") 
    curr=head.next 
    while curr!=head : 
        print(curr.key, end=" ")
        curr=curr.next 
head=Node(10)
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=head 
printCircular(head)