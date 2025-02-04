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


## Intersection point of two linked list  
# Approach 1 : Using a set 
def getIntersection1(head1, head2) : 
    s=set() 
    curr=head1 
    while curr!=None : 
        s.add(curr) 
        curr=curr.next 
    curr=head2 
    while curr!=None : 
        if curr in s : 
            return curr.key 
        curr=curr.next 
    return -1 

## LL - 1
head1=Node(5)
head1.next=Node(8)
head1.next.next=Node(7)
head1.next.next.next=Node(10)
head1.next.next.next.next=Node(12)
head1.next.next.next.next=Node(15) 

# LL - 2 
head2=Node(9) 
head2.next=head1.next.next.next 

print("Intersection point of Linked List: Using Hashing ")
print(getIntersection1(head1, head2)) 
print("\n") 


# Approach 2 : in constant space 
def getIntersection2(d, head1, head2) : 
    curr1=head1 
    curr2=head2 
    for i in range(d) : 
        if curr1==None : 
            return -1 
        curr1=curr1.next 
    while curr1!=None and curr2!=None : 
        if curr1==curr2.next : 
            return curr1.key 
        curr1=curr1.next 
        curr2.next 
## LL - 1
head1=Node(5)
head1.next=Node(8)
head1.next.next=Node(7)
head1.next.next.next=Node(10)
head1.next.next.next.next=Node(12)
head1.next.next.next.next=Node(15) 

# LL - 2 
head2=Node(9) 
head2.next=head1.next.next.next 

print("Intersection point of Linked List: In constant space ")
print(getIntersection2(2, head1, head2)) 
print("\n") 



## Segregate even and add nodes 
# Naive approach - traverse the list first and mark the end pointer , then agaib while traversing if odd element encountered 
# then move to the end and update the pointers accordingly 

# Efficient approach 
 # Doubt --------------->>>>>>>>>>> 


## Pair wise swap nodes 
# Naive approach 
def swapNodes(head) : 
    curr=head 
    while curr!=None and curr.next!=None : 
        curr.key, curr.next.key = curr.next.key, curr.key 
        curr=curr.next.next 
    return head 
head=Node(10) 
head.next=Node(20) 
head.next.next=Node(30) 
head.next.next.next=Node(40) 
head.next.next.next.next=Node(50)  
swapNodes(head)
print("Swap nodes pairwise: Naive")
printList(head) 
print("\n") 

# Efficient approach 
def pairwiseSwap(head) : 
    if head==None or head.next==None : 
        return head 
    curr=head.next.next 
    prev=head 
    head=head.next 
    head.next=prev 
    while curr!=None and curr.next!=None : 
        prev.next = curr.next 
        prev=curr 
        next=curr.next.next 
        curr.next.next=curr 
        curr=next 
    prev.next=curr 
    return head 
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50) 
head.next.next.next.next.next=Node(60) 
new = pairwiseSwap(head) 
print("Pair wise swap: Efficient")
printList(new) 
print("\n") 



## Clone a linked list with random pointer  
# Naive Approach  (Using Hashing)
def cloneHash(h1) : 
    d={None : None }
    curr=head 
    while curr!=None : 
        d[curr]=Node(curr.key) 
        curr=curr.next 
    curr=head 
    while curr!=None : 
        d[curr].next = d[curr.next] 
        d[curr].random = d[curr.random] 
        curr=curr.next 
    return d[h1] 

# Efficient approach 
def clone(h1) : 
    curr=h1 
    while curr!=None : 
        next=curr.next 
        curr.next = Node(curr.key) 
        curr.next.next = next 
        curr=next 
    curr=h1 
    while curr!=None : 
        curr.next.random=curr.random.next 
        curr=curr.next.next 
    h2=h1.next 
    clone=h2 
    curr=h1 
    while curr!=None : 
        curr.next=curr.next.next 
        clone.next=None if clone.next==None else clone.next.next 
        clone=clone.next 
        curr=curr.next 
    return h2 


## Merge two sorted linked lists 
def sortedMerge(a, b) : 
    if a==None : 
        return b 
    if b==None : 
        return a 
    head, tail = None, None 
    if a.key<=b.key : 
        head=tail=a 
        a=a.next 
    else : 
        head=tail=b 
        b=b.next 
    while a!=None and b!=None : 
        if a.key<=b.key : 
            tail.next=a 
            tail=a 
            tail=a 
            a=a.next 
        else : 
            tail.next = b 
            tail = b 
            b = b.next 
    if a==None : 
        tail.next = b 
    else : 
        tail.next = a 
    return head 


## Palindrome Linked List 
# Naive approach (Using stack) 
def isPalindromeStack(head) : 
    stack=[]
    curr=head 
    while curr!=None : 
        stack.append(curr.key)
        curr=curr.next 
    curr=head 
    while curr!=None : 
        if stack.pop()!=curr.key : 
            return False 
        curr=curr.next 
    return True 


from Linked_List_2 import reverseList2
# Efficient approach 
def isPalindromeSF(head) : 
    if head==None : 
        return True 
    slow, fast = head, head 
    while fast.next!=None and fast.next.next!=None : 
        slow=slow.next 
        fast=fast.next.next 
    rev=reverseList2(slow.next) 
    curr=head 
    while rev!=head : 
        if rev.data!=head : 
            return False 
        rev=rev.next 
        curr=curr.next 
    return True 