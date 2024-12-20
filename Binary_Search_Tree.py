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
def searchBST1(root, key) : 
    if root is None : 
        return False 
    elif root.key==key : 
        return True 
    elif root.key>key : 
        return searchBST1(root.left, key) 
    else : 
        return searchBST1(root.right, key) 
root=Node(10) 
root.left=Node(20) 
root.right=Node(30) 
root.left.left=Node(40) 
root.left.right=Node(50) 


# Iterative implementation 
def searchBST2(root, key) : 
    while root!=None : 
        if root.key==key : 
            return True 
        elif root.key>key : 
            root=root.left 
        else : 
            root=root.right 
    return False 
