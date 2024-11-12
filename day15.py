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

def delFirst(head) : 
    if head==None : 
        return None 
    else : 
        return head.next 

head=Node(10) 
head.next=Node(20) 
head.next.next=Node(30)  
head=delFirst(head) 
printList(head)  