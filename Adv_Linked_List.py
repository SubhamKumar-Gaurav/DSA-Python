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
        print(curr.key) 
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
print() 