#  Day - 17  
#    Delete head of Circular Linked List 
#    Delete Kth node of Circular Linked List 


class Node : 
    def __init__(self,key) :
        self.key=key 
        self.next=None
 
def printCircular(head) : 
    if head==None : 
        return 
    print(head.key, end=" ") 
    curr=head.next 
    while curr!=head : 
        print(curr.key, end=" ")
        curr=curr.next 

## Delete head of Circular Linked List
# Approach -1    (Linear Time) 
def delHead1(head) : 
    if head==None : 
        return None 
    elif head.next==head : 
        return None 
    curr=head 
    while curr.next!=head : 
        curr=curr.next 
    curr.next=head.next 
    return curr.next  

head=Node(10)
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=head 
print("Delete head of Circular Linked List : ") 
print("Approach - 1 (Linear Time)")
printCircular(delHead1(head))
print("\n") 


# Approach -2  (Constant Time)  
def delHead2(head) : 
    if head==None : 
        return None 
    elif head.next==None : 
        return None 
    else : 
        head.key=head.next.key 
        head.next=head.next.next 
        return head 
head=Node(10)
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=Node(40) 
head.next.next.next.next=head 
print("Approach - 2 (Constant Time)")
printCircular(delHead2(head))
print("\n") 



## Delete Kth node of Circular Linked List  
def delKth(head,k) : 
    if head==None : 
        return None 
    elif k==1 : 
        return delHead2(head) 
    else : 
        curr=head 
        for i in range(k-2) : 
            curr=curr.next 
        curr.next=curr.next.next 
        return head 
head=Node(10)
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=Node(40) 
head.next.next.next.next=Node(50) 
head.next.next.next.next.next=head  
print("Delete Kth node of Circular Linked List : ") 
printCircular(delKth(head,3))