# Day - 15  
#    Linked List 
#    Delete first node in Linked List 
#    Delete last node in Linked List 
#    Delete a node with pointer given to it 
#    Sorted insert Linked List 
#    Middle of Linked List 
#    Nth node from end of Linked List 
#    Remove duplicates from sorted singly linked list 
#    Reverse a Linked List 

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


## Delete a node with pointer given to it 
def delNode(ptr) : 
    temp=ptr.next 
    ptr.data=temp.data 
    ptr.next=temp.next  
 

## Sorted Insert Linked List in Python 
def sortedInsert(head,x) : 
    temp=Node(x) 
    if head==None : 
        return temp 
    elif x<head.data : 
        temp.next=head 
        return temp 
    else : 
        curr=head 
        while curr.next!=None and curr.next.data<x : 
            curr=curr.next 
        temp.next=curr.next 
        curr.next=temp 
        return head 


## Middle of a Linked List 
# Naive approach 
def printMidlle(head) : 
    if head==None : 
        return 
    count=0 
    curr=head 
    while curr : 
        curr=curr.next 
        count+=1 
    curr=head 
    for i in range(count//2) : 
        curr=curr.next 
    print(curr.data) 

# Efficient approach 
def printMiddle(head) : 
    if head==None : 
        return 
    slow=head 
    fast=head 
    while fast!=None and fast.next!=None : 
        slow=slow.next 
        fast=fast.next.next 
    print(slow.data) 


## Nth node from end of Linked List  
# Method -1  (using length of linked list) 
def printNthFromEnd(head,n) : 
    l=0 
    curr=head 
    while curr : 
        curr=curr.next 
        l+=1 
    if n>l : 
        return 
    curr=head 
    for i in range(1,l-n+1) : 
        curr=curr.next 
    # print(curr.data)
 
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
print("Nth node from end of Linked List : ")
print(printNthFromEnd(head,2),"\n") 

# Method - 2 (Using two Pointers/References) 
def printNthfromend(head,n) : 
    if head==None : 
        return 
    first=head 
    for i in range(n) : 
        if first==None : 
            return 
        first=first.next 
    second=head 
    while first!=None : 
        second=second.next 
        first=first.next 
    print(second.data) 