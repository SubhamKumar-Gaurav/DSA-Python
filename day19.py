## Day - 19 
#    Delete Head of DLL 
#    Delete last node of DLL 
#    Reverse a DLL 


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


## Delete Head of DLL 
def delHead(head) : 
    if head==None : 
        return None 
    if head.next==None : 
        return None  
    else : 
        head=head.next 
        head.prev=None 
        return head 
head=Node(10) 
temp1=Node(20) 
temp2=Node(30) 
head.next=temp1 
temp1.prev=head 
temp1.next=temp2 
temp2.prev=temp1 
print("Delete Head of DLL : ")
printList(delHead(head)) 
print("\n")  


## Delete last Node of DLL 
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
temp1=Node(20) 
temp2=Node(30) 
head.next=temp1 
temp1.prev=head 
temp1.next=temp2 
temp2.prev=temp1 
print("Delete Last Node of DLL : ")
printList(delLastNode(head)) 
print("\n")  


## Reverse a DLL 
def reverseDLL(head) : 
    if head==None : 
        return None 
    if head.next==None : 
        return head 
    curr=head 
    prev=None 
    while curr!=None : 
        prev=curr 
        curr.next,curr.prev=curr.prev,curr.next 
        curr=curr.prev 
    return prev 
head=Node(10) 
temp1=Node(20) 
temp2=Node(30) 
head.next=temp1 
temp1.prev=head 
temp1.next=temp2 
temp2.prev=temp1 
print("Reverse a DLL : ")
printList(reverseDLL(head)) 
print("\n")
