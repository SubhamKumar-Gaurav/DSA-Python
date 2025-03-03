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