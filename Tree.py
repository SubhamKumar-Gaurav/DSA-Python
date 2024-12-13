##  Tree 
#     Basic terms 



print("Basic terms in Tree Data Structure")  
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