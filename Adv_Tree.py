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
