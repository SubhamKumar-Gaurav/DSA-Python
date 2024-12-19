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
