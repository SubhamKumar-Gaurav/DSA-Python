# Adv Tree 
#   Level Order Traversal by Line - 2 codes 
#   Check for Balanced Binary Tree 
#   Vertical Traversal of Binary tree 
#   Bottom View of Binary Tree 
#   Maximum Width of Binary Tree 
#   Convert Binary Tree to Doubly Linked List 
#   Construct Binary Tree from Inorder and Preorder 
#   Tree Traversal in Spiral Form 
#   Diameter of a Binary Tree 
#   LCA of Binary Tree 
#   Burn a Binary Tree from a Leaf 
#   Count Nodes in a Complete Binary Tree 
#   Serialize and Deserialize a Binary Tree 
#   Iterative Inorder Traversal 
#   Iterative Preorder Traversal 
#   Iterative Preorder Traversal (Space optimized) 


# Tree Definition 
class Node : 
    def __init__(self, k): 
        self.left=None 
        self.right=None 
        self.key=k 

## Level Order Traversal by Line
# Code - 1 
from collections import deque
def printLevelOrder1(root) : 
    if root is None : 
        return 
    q=deque()
    q.append(root) 
    q.append(None) 
    while len(q)>1 : 
        curr=q.popleft() 
        if curr==None : 
            print() 
            q.append(None)
            continue
        print(curr.key, end=" ")
        if curr.left is not None : 
            q.append(curr.left) 
        if curr.right is not None : 
            q.append(curr.right) 
print("Level order Traversal by Line : Code 1")
root=Node(10)
root.left=Node(20)
root.right=Node(30) 
root.left.left=Node(40)
root.left.right=Node(50) 
root.right.left=Node(60)
root.right.right=Node(70)
printLevelOrder1(root) 
print("\n")


# Code - 2 
def printLevelOrder2(root) : 
    if root is None : 
        return 
    q=deque() 
    q.append(root) 
    while len(q)>0 : 
        count=len(q) 
        for i in range(count) : 
            curr=q.popleft() 
            print(curr.key, end=" ")
            if curr.left is not None : 
                q.append(curr.left)
            if curr.right is not None : 
                q.append(curr.right) 
        print() 
print("Level order Traversal by Line : Code 2")
root=Node(10)
root.left=Node(20)
root.right=Node(30) 
root.left.left=Node(40)
root.left.right=Node(50) 
root.right.left=Node(60)
root.right.right=Node(70)
printLevelOrder2(root) 
print("\n")


## Check for Balanced Binary Tree 
# Naive approach         Time : O(n^2)
def height(root) : 
    if root==None : 
        return 0 
    else : 
        return max(height(root.left),height(root.right))+1 

def isBalanced1(root) : 
    if root==None : 
        return True 
    lh=height(root.left)
    rh=height(root.right) 
    return abs(lh-rh)<=1 and isBalanced1(root.left) and isBalanced1(root.right) 


# Efficient approach 
def isBalanced(root) : 
    if root==None : 
        return True 
    lh=isBalanced(root.left)
    if lh==-1 : 
        return -1 
    rh=isBalanced(root.right)
    if rh==-1 : 
        return -1 
    if abs(lh-rh)>1 : 
        return -1 
    return max(lh, rh)+1 

def isBalancedMain(root) : 
    if isBalanced(root)==-1 : 
        return False
    return True 



##  Vertical Traversal of Binary tree 
# Code - 1
def findMinMax(node, minimum, maximum, hd) : 
    if node is None : 
        return 
    minimum[0]=min(minimum[0], hd) 
    maximum[0]=max(maximum[0], hd) 
    findMinMax(node.left, minimum, maximum, hd-1)
    findMinMax(node.right, minimum, maximum, hd+1)

def printVerticalLine(node, line_no, hd) : 
    if node is None : 
        return 
    if hd==line_no :  
        print(node.key, end=" ")
    printVerticalLine(node.left, line_no, hd-1)
    printVerticalLine(node.right, line_no, hd+1)

def verticalOrder(root) : 
    minimum=[0]
    maximum=[0]
    findMinMax(root, minimum, maximum, 0)

    for line_no in range(minimum[0], maximum[0]+1) : 
        printVerticalLine(root, line_no, 0)
        print()
        
print("Vertical Traversal of Binary Tree : ")
root=Node(30)
root.left=Node(40)
root.right=Node(80)
root.left.left=Node(50)
root.left.right=Node(70)
root.left.right.left=Node(20)
root.left.right.right=Node(10)
root.right.left=Node(5)
verticalOrder(root)
print("\n")
 
# Code 2 
# Maintains the same order 
import collections 
def vTraversal(root) : 
    mp={} 
    q=[] 
    q1=[] 
    q.append(root) 
    q1.append(0) 

    while len(q)>0 :  
        curr=q.pop(0) 
        hd=q1.pop(0) 

        if mp.get(hd) is None : 
            mp[hd]=[] 
        mp[hd].append(curr.key) 
        if curr.left!=None : 
            q.append(curr.left) 
            q1.append(hd-1) 
        if curr.right!=None : 
            q.append(curr.right)
            q1.append(hd+1) 
    sorted_mp=collections.OrderedDict(sorted(mp.items())) 
    for i in sorted_mp.values() : 
        for j in i : 
            print(j, end=" ") 
        print() 
print("Vertical Traversal 2 ")
root=Node(30)
root.left=Node(40)
root.right=Node(80)
root.left.left=Node(50)
root.left.right=Node(70)
root.left.right.left=Node(20)
root.left.right.right=Node(10)
root.left.right.right.left=Node(3)
root.left.right.right.left.left=Node(25)
root.right.left=Node(5)
vTraversal(root)
print("\n") 


## Bottom View of Binary Tree 
def bottomView(root) : 
    mp={} 
    q=[] 
    q1=[] 

    q.append(root)
    q1.append(0)

    while len(q)>0 : 
        curr=q.pop(0)
        hd=q1.pop(0) 

        mp[hd]=curr.key 
        if curr.left != None : 
            q.append(curr.left)
            q1.append(hd-1)
        if curr.right != None : 
            q.append(curr.right)
            q1.append(hd+1)
    for i in sorted(mp) : 
        print(mp[i], end=" ")
print("Bottom view of Binary Tree ")
bottomView(root) 
print("\n")



## Maximum width of Binary Tree 
def maxWidth(root) : 
    if root is None : 
        return 0 
    q=deque() 
    q.append(root)
    res=0 
    while q : 
        count=len(q)
        for i in range(count) : 
            node=q.popleft() 
            if node.left : 
                q.append(node.left) 
            if node.right : 
                q.append(node.right)
        res=max(res, count)
    return res 
print("Maximum width of Binary Tree ")
print(maxWidth(root)) 
print("\n")



## Convert Binary Tree to Doubly Linked List inplace  (by Inorder traversal)
# DLL 
# Tree Definition 
class Node : 
    def __init__(self, k): 
        self.left=None 
        self.right=None 
        self.key=k 
        self.prev=None 
        self.next=None 
# print DLL
def printDLL(head) : 
    curr=head 
    while curr != None : 
        print(curr.key, end=" ")
        curr=curr.right
# inorder Traversal
def inorder(root) : 
    if root!=None : 
        inorder(root.left)
        print(root.key, end=" ") 
        inorder(root.right)  

prev=None 
def convert(root) : 
    if root is None : 
        return root 
    global prev 
    head=convert(root.left)
    if prev is None : 
        head=root 
    else : 
        prev.right=root 
        root.left=prev 
    prev=root 
    convert(root.right) 
    return head 
root=Node(10)
root.left=Node(5)
root.right=Node(30)
root.right.left=Node(20)
print("Binary Tree to DLL ")
print("Binary Tree (inorder): ", end=" ")
inorder(root)
print()
print("DLL : ", end=" ")
printDLL(convert(root))
print("\n") 


## Construct Binary Tree from Inorder and Preorder
# Approach - 1     Time : O(n^2) 
pre_ind=0 
def buildTree1(pre, io, isi, iei) : 
    if isi>iei : 
        return None 
    global pre_ind 
    root=Node(pre[pre_ind])
    pre_ind+=1 
    if isi==iei : 
        return root 
    for i in range(isi, iei+1) : 
        if io[i]==root.key : 
            break 
    root.left=buildTree1(pre, io, isi, i-1)
    root.right=buildTree1(pre, io, i+1, iei) 
    return root 
io=[40, 20, 50, 10, 30, 80, 70, 90]
pre=[10, 20, 40, 50, 30, 70, 80, 90]
print("Construct Tree from Preorder and Inorder - 1")
printLevelOrder2(buildTree1(pre, io, 0, 7))

# Approach - 2     Time : O(n)
mp={val: idx for idx, val in enumerate(io)}
pre_ind=0 
def buildTree2(pre, io, isi, iei, mp) : 
    if isi>iei : 
        return None 
    global pre_ind 
    root=Node(pre[pre_ind]) 
    pre_ind+=1 
    if isi==iei : 
        return root 
    i=mp[root.key] 
    root.left=buildTree2(pre, io, isi, i-1, mp) 
    root.right=buildTree2(pre, io, i+1, iei, mp) 
    return root 
print("Construct Tree from Preorder and Inorder - 2")
printLevelOrder2(buildTree2(pre, io, 0, 7, mp))
print("\n")


## Tree Traversal in Spiral Form 
# Approach - 1 
def printSpiral(root) : 
    if root is None : 
        return 
    q=deque() 
    s=[] 
    rev=False 
    q.append(root)
    while q : 
        count=len(q) 
        for i in range(count) : 
            temp=q.popleft() 
            if rev : 
                s.append(temp.key) 
            else : 
                if i<count-1 :
                    print(temp.key, end=" ")
                else : 
                    print(temp.key) 
            if temp.left : 
                q.append(temp.left)
            if temp.right : 
                q.append(temp.right) 
        if rev : 
            while s: 
                print(s.pop(), end=" ")
            print() 
        rev = not rev 
root=Node(30)
root.left=Node(40)
root.right=Node(80)
root.left.left=Node(50)
root.left.right=Node(70)
root.left.right.left=Node(20)
root.left.right.right=Node(10)
root.left.right.right.left=Node(3)
root.left.right.right.left.left=Node(25)
root.right.left=Node(5)
print("Tree Traversal in Spiral Form - 1")
printSpiral(root)
print("\n") 


## Diameter of Tree 
# Naive approach     Time : O(n^2)
def height(root) : 
    if root is None : 
        return 0
    else : 
        return max(height(root.left), height(root.right))+1 
def diameter1(root) : 
    if root is None : 
        return 0 
    d1=1+height(root.left)+height(root.right)
    d2=diameter1(root.left)
    d3=diameter1(root.right) 
    return max(d1, d2, d3)-1 
root=Node(10)
root.left=Node(20) 
root.right=Node(30) 
root.right.left=Node(40) 
root.right.left.left=Node(50) 
root.right.right=Node(60) 
root.right.right.right=Node(70) 
print("Diameter of Tree (Naive)")
print(diameter1(root))

# Efficient approach       Time : O(n)
def diameter2(root, res) : 
    if root is None : 
        return 0 
    lh=diameter2(root.left, res)
    rh=diameter2(root.right, res)  
    res[0]=max(res[0], lh+rh) 
    return 1+max(lh, rh)
root=Node(10)
root.left=Node(20) 
root.right=Node(30) 
root.right.left=Node(40) 
root.right.left.left=Node(50) 
root.right.right=Node(60) 
root.right.right.right=Node(70) 
res=[0]
print("Diameter of Tree (Efficient)")
print(diameter2(root, res))
print("\n") 