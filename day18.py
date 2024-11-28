## Day - 18   Doubly Linked List 
#    Insert at beginning of DLL 
#  


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