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
root=Node(20) 
root.left=Node(10) 
root.right=Node(40) 
root.left.left=Node(5) 
root.right.left=Node(30) 
root.right.right=Node(80) 
root.right.right.left=Node(50) 
root.right.right.right=Node(100) 
print("40 : ", searchBST1(root, 40))

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
