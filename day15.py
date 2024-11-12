# Day - 15  
#    Linked List 
#    Delete first node in Linked List 
#    Delete last node in Linked List 
#    Delete a node with pointer given to it 
#    Sorted insert Linked List 


class Node : 
    def __init__(self,k) :       
        self.key=k 
        self.next=None 

# printList function : 
def printList(head) :  
    curr=head 
    while curr!=None : 
        print(curr.key, end=" ") 
        curr=curr.next 


## Delete first Node 
def delFirst(head) : 
    if head==None : 
        return None 
    else : 
        return head.next 
head=Node(10) 
head.next=Node(20) 
head.next.next=Node(30)  
head=delFirst(head) 
print("Delete first Node : ")
printList(head)  
print("\n")


## Delete last node  
def delLastNode(head) : 
    if head==None : 
        return None 
    if head.next==None : 
        return None 
    curr=head 
    while curr.next.next!=None : 
        curr=curr.next 
    curr.next=None 
    return head 
head=Node(10) 
head.next=Node(20) 
head.next.next=Node(30) 
head=delLastNode(head) 
print("Delete last node : ")
printList(head)
print("\n")