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
print("Traversing through Circular Linked List : ")
printCircular(head) 
print("\n")


## Insert at the beginning of Circular Linked List 
# Approach -1    Time : O(n)
def insertBegin1(head, x) :   
    temp=Node(x)  
    if head==None : 
        temp.next=temp 
        return temp 
    curr=head 
    while curr.next!=head : 
        curr=curr.next 
    curr.next=temp 
    temp.next=head 
    return temp
head=Node(10)
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=head 
x=15
print("Insert at the beginning : ")
print("Approach - 1  (Naive approach)")  
printCircular(insertBegin1(head,x)) 
print("\n")

# Approach - 2    Time : O(1) 
def insertBegin2(head,x) : 
    temp=Node(x) 
    if head==None : 
        temp.next=temp 
        return temp 
    else : 
        temp.next=head.next 
        head.next=temp 
        temp.key, head.key = head.key, temp.key 
        return temp
head=Node(10)
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=head 
x=15
print("Approach -2   (Constant time)")
printCircular(insertBegin2(head,x))
print("\n") 


## Insert at the end of Circular Linked List 
# Approach -1   (Linear Time) 
def insertEnd1(head,x) : 
    temp=Node(x) 
    if head==None : 
        temp.next=temp 
        return temp 
    else : 
        temp.next=head.next 
        head.next=temp 
        temp.key,head.key=head.key,temp.key 
        return temp 
head=Node(10)
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=head 
x=15
print("Insert at the end : ")
print("Approach - 1  (Linear Time)")  
printCircular(insertEnd1(head,x)) 
print("\n") 

# Approach -2  (Constant time) 
def insertEnd2(head,x) : 
    temp=Node(x) 
    if head==None : 
        temp.next=temp 
        return temp 
    else : 
        temp.next=head.next 
        head.next=temp 
        temp.key,head.key=head.key,temp.key 
        return temp 
head=Node(10)
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=head 
x=15
print("Approach - 2  (Constant Time)")  
printCircular(insertEnd2(head,x)) 
print("\n") 

