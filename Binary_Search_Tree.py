## Binary Search Tree 
#     Background 
#     Introduction 
#     Search in BST 
#     Insert in BST 
#     Deletion in BST 
#     Floor in BST 
#     BST Floor 
#     Ceiling in BST 
#     Self Balancing 
#     AVL Tree 
#     Red Black Tree 
#     Applications of BST   


## Binary Tree in Python
class Node : 
    def __init__(self, k): 
        self.left=None 
        self.right=None 
        self.key=k 


## Search in BST  
# Recursive implementation 
print("Search in BST - Recursive approach ")
def searchBST1(root, key) : 
    if root is None : 
        return False 
    elif root.key==key : 
        return True 
    elif root.key>key : 
        return searchBST1(root.left, key) 
    else : 
        return searchBST1(root.right, key) 
root=Node(20) 
root.left=Node(10) 
root.right=Node(40) 
root.left.left=Node(5) 
root.right.left=Node(30) 
root.right.right=Node(80) 
root.right.right.left=Node(50) 
root.right.right.right=Node(100) 
print("40 : ", searchBST1(root, 40))
print("4 : ", searchBST1(root, 4))
print("\n") 


# Iterative implementation 
print("Search in BST -Iterative approach ")
def searchBST2(root, key) : 
    while root!=None : 
        if root.key==key : 
            return True 
        elif root.key>key : 
            root=root.left 
        else : 
            root=root.right 
    return False 
root=Node(20) 
root.left=Node(10) 
root.right=Node(40) 
root.left.left=Node(5) 
root.right.left=Node(30) 
root.right.right=Node(80) 
root.right.right.left=Node(50) 
root.right.right.right=Node(100) 
print("100 : ", searchBST2(root, 100))
print("15 : ", searchBST2(root, 15)) 
print("\n")  

def printKDist(root,k) : 
    if root is None : 
        return 
    if k==0 : 
        print(root.key, end=" ")
    else : 
        printKDist(root.left, k-1)
        printKDist(root.right, k-1)

def height(root) : 
    if root==None : 
        return 0 
    else : 
        return max(height(root.left),height(root.right))+1 

## Insert in BST  
# Recursive approach 
def insert1(root, key) : 
    if root==None : 
        return Node(key) 
    elif root.key==key : 
        return root 
    elif root.key>key : 
        root.left=insert1(root.left, key) 
    else : 
        root.right=insert1(root.right, key) 
    return root 
root=None 
root=insert1(root, 10)
root=insert1(root, 20)
root=insert1(root, 5) 
print("Insert in BST (Recursive approach) : ") 

h=height(root) 
for k in range(h) : 
    printKDist(root,k) 
print("\n")
