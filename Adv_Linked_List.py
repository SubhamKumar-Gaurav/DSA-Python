## Advanced Linked List 
#   Reverse a linked list in group of size k 
#   Detect loop using floyd's cycle detection algorithm 
#   Detect and remove loop in linked list 
#   Intersection point of two linked list 
#   Segregate Even and Odd nodes 
#   Pairwise swap nodes 
#   Clone a linked list with random pointer 
#   Merge two sorted linked lists 
#   Palindrome Linked List 


# LL class 
class Node : 
    def __init__(self, k) : 
        self.key=k 
        self.next=None

# print list 
def printList(head) : 
    curr=head 
    while curr!=None : 
        print(curr.key, end=" ") 
        curr=curr.next 


## Reverse a linked list in group of size k 
# Recursive solution  
def recRevK(head, k) : 
    curr=head 
    prev , next = None, None 
    count=0 
    while curr!=None and count<k : 
        next=curr.next 
        curr.next=prev 
        prev=curr 
        curr=next 
        count+=1 
    if next!=None : 
        rem_head=recRevK(curr, k) 
        head.next=rem_head
    return prev 

print("Reverse LL in grp of k: Recursive")
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
head.next.next.next.next.next.next = Node(70)
head=recRevK(head, 3)
printList(head) 
print("\n") 

# Iterative solution 
def iteRevK(head, k) : 
    curr=head 
    prev_first=None 
    first_pass=True 
    while curr!=None : 
        first, prev = curr, None 
        count=0 
        while curr!=None and count<k : 
            next=curr.next 
            curr.next=prev 
            prev=curr 
            curr=next 
            count+=1 
        if first_pass : 
            head=prev 
            first_pass=False 
        else : 
            prev_first.next=prev 
        prev_first=first 
    return head 
print("Reverse LL in grp of k: Iterative")
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
head.next.next.next.next.next.next = Node(70)
head.next.next.next.next.next.next.next = Node(80)
head=iteRevK(head, 3) 
printList(head)
print("\n") 


## Detect loop using floyd's cycle detection algorithm    
def isLoopFloyd(head) : 
    slow=head 
    fast=head  
    while fast!=None and fast.next!=None : 
        slow=slow.next 
        fast=fast.next.next 
        if slow==fast : 
            return True  
    return False 

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
head.next.next.next.next.next.next = Node(70)   # 70 to 30 loop 
head.next.next.next.next.next.next.next = head.next.next  # when we want to create a loop, we need to link the reference 
print("Detect loop using Floyd's algo : ", isLoopFloyd(head)) 
print("\n") 
# print(head) - Don't try this line for a LL with loop. Since head.next is never equal to None. it will return for infinite time


## Detect and Remove loop in Linked List 
def detectRemoveLoops(head) : 
    slow=head 
    fast=head 
    while fast!=None and fast.next!=None : 
        slow=slow.next 
        fast=fast.next.next 
        if slow==fast : 
            break 
    if slow!=fast : 
        return 
    while slow.next!=fast.next : 
        slow=slow.next 
        fast=fast.next  
    fast.next=None 
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)
head.next.next.next.next.next.next = Node(70)   
head.next.next.next.next.next.next.next = head.next.next # 70 to 30 loop 
detectRemoveLoops(head) 
print("After removing the loop")
printList(head) 
print("\n") 