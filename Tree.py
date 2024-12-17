##  Tree 
#     Basic terms 
#     Applications of Tree
#     Binary Tree 
#     Tree Traversal 
#     Depth first 
#       - Inorder 
#       - Preorder 
#       - Postorder
#     Height of Binary Tree 
#     Print Node at K distance 
#     Level Order Traversal  
#     Size of Binary Tree   
#     Maximum in Binary Tree


## Basic terms in Tree Data Structure  
# node, root, leaf, child, parent, subtree, descendants, ancestors, degree   


## Applications of Tree
#    To represent hierarchical data 
#       - Organization structure 
#       - Folder structure 
#       - XML/HTML Content (JSON Objects) 
#       - In OOP (Inheritance) 
#    Binary Search Trees 
#    Binary Heap 
#    B and B+ Trees in DBMS 
#    Spanning and Shortest path tree in Computer Networks 
#    Parse Tree, Expression Tree in Compilers 


## Binary Tree in Python
class Node : 
    def __init__(self, k): 
        self.left=None 
        self.right=None 
        self.key=k 

# Driver code : 
root=Node(10) 
root.left=Node(20)
root.right=Node(20)
root.left.left=Node(40) 


## Tree Traversal 
#      Breadth First (Level order)
#      Depth First  
#         - Inorder 
#         - Preorder 
#         - Postorder   



##  Inorder Traversal  
class Node : 
    def __init__(self, k): 
        self.key=k 
        self.left=None 
        self.right=None 
def inorder(root) : 
    if root!=None : 
        inorder(root.left)
        print(root.key) 
        inorder(root.right)  

root=Node(10) 
root.left=Node(20)
root.right=Node(30) 
root.right.left=Node(40) 
root.right.right=Node(50) 
print("Inorder Traversal of Tree : ")
inorder(root) 
print("\n") 


##  Preorder Traversal  
class Node : 
    def __init__(self, k): 
        self.key=k 
        self.left=None 
        self.right=None 
def preorder(root) : 
    if root!=None : 
        print(root.key) 
        preorder(root.left)
        preorder(root.right)  

root=Node(10) 
root.left=Node(20)
root.right=Node(30) 
root.right.left=Node(40) 
root.right.right=Node(50) 
print("Preorder Traversal of Tree : ")
preorder(root) 
print("\n") 



##  Postorder Traversal  
class Node : 
    def __init__(self, k): 
        self.key=k 
        self.left=None 
        self.right=None 
def postorder(root) : 
    if root!=None : 
        postorder(root.left)
        postorder(root.right)
        print(root.key)   

root=Node(10) 
root.left=Node(20)
root.right=Node(30) 
root.right.left=Node(40) 
root.right.right=Node(50) 
print("Postorder Traversal of Tree : ")
postorder(root) 
print("\n") 


##  Height of Binary Tree 
# Code - 1  (with the variables rh and lh)
def height(root) : 
    if root==None : 
        return 0 
    else : 
        lh=height(root.left)
        rh=height(root.right)
        return max(rh,lh)+1 
root=Node(10)
root.left=Node(20) 
root.right=Node(30) 
root.right.left=Node(40)
print("Height of the Tree : ", height(root))


##  Code - 2 (Shorter implementation)
def height(root) : 
    if root==None : 
        return 0 
    else : 
        return max(height(root.left),height(root.right))+1 
root=Node(10)
root.left=Node(8) 
root.right=Node(30) 
root.right.left=Node(40)
root.right.right=Node(50) 
root.right.right.left=Node(50) 
print("Height of the Tree : ", height(root))
print("\n") 


## Print Node at K distance
def printKDist(root,k) : 
    if root is None : 
        return 
    if k==0 : 
        print(root.key, end=" ")
    else : 
        printKDist(root.left, k-1)
        printKDist(root.right, k-1)
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.right=Node(70)
root.right.right=Node(80)
print("Node at k=2 distance : ") 
printKDist(root,2)
print("\n") 


## Level Order Traversal  
# Naive approach 

root=Node(10)
root.left=Node(20) 
root.left.right=Node(30)
root.left.right.left=Node(40)
root.left.right.right=Node(50)

print("Level order traversal (Naive method)")
h=height(root) 
for k in range(h) : 
    printKDist(root,k) 
print("\n") 


from collections import deque 
def printLevelOrder(root) : 
    if root is None : 
        return 
    q=deque() 
    q.append(root) 
    while len(q)>0 : 
        node=q.popleft() 
        print(node.key) 
        if node.left is not None : 
            q.append(node.left) 
        if node.right is not None : 
            q.append(node.right)
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.right=Node(60) 
root.left.right.left=Node(70)
root.left.right.right=Node(80)



#     Size of Binary Tree   
#     Maximum in Binary Tree