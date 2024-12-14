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


