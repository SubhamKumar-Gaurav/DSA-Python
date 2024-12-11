## Day - 18   Doubly Linked List - 
#    Insertion operation :
#       Insert at the Beginning of DLL 
#       Insert at the End of DLL 


class Node : 
    def __init__(self,k) : 
        self.key=k 
        self.prev=None 
        self.next=None 

def printList(head) : 
    curr=head 
    while curr!=None : 
        print(curr.key, end=" ")
        curr=curr.next 


## Insert at the beginning of DLL   
def insertBegin(head,x) :  
    temp=Node(x) 
    if head!=None : 
        head.prev=temp 
    temp.next=head 
    return temp 

head=None 
head=insertBegin(head,10) 
head=insertBegin(head,20)  
print("Insert at the beginning of DLL : ")
printList(head) 
print("\n")  


## Insert at the end of DLL 
def insertEnd(head,x) : 
    temp=Node(x) 
    if head==None : 
        return temp 
    else :
        curr=head 
        while curr.next!=None : 
            curr=curr.next 
        curr.next=temp 
        temp.prev=curr 
        return head 
head=None 
head=insertEnd(head,10) 
head=insertEnd(head,20) 
head=insertEnd(head,30) 
print("Insert at the End of DLL")
printList(head) 
print("\n") 
