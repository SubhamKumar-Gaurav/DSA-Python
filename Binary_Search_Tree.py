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

## Print Tree 
def printTree(root) : 
    h=height(root) 
    for k in range(h) : 
        printKDist(root,k) 
    print("\n") 

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


# Iterative approach 
def insert2(root, key) :    
    parent=None 
    curr=root 
    while curr!=None :  
        parent=curr 
        if curr.key==key : 
            return root 
        elif root.key<key : 
            curr=curr.left 
        else : 
            curr=curr.right 
    if parent==None : 
        return Node(key) 
    if parent.key>key : 
        parent.left=Node(key) 
    else : 
        parent.right=Node(key) 
    return root 

root=insert2(root, 200) 
print("Insert in BST (Iterative approach) : ") 

h=height(root) 
for k in range(h) : 
    printKDist(root,k) 
print("\n") 


## Deletion in BST  
def getSucc(curr, key) : 
    while curr.key!=None : 
        curr=curr.left
    return curr.key 

def delNode(root, key) : 
    if root==None : 
        return 
    if root.key>key : 
        root.left=delNode(root.left, key) 
    elif root.key<key : 
        root.right=delNode(root.right, key) 
    else : 
        if root.left==None : 
            return root.right 
        elif root.right==None : 
            return root.left 
        else : 
            succ=getSucc(root.right, key) 
            root.key=succ 
            root.right=delNode(root.right, succ) 
        return  
root=Node(10) 
root.left=Node(5) 
root.right=Node(20) 
root.right.left=Node(18) 
root.right.right=Node(100)  
printTree(delNode(root, 100)) 


## Floor of BST 
print("Floor of BST : ") 
def getFloor(root, x) : 
    res=None 
    while root!=None : 
        if root.key==x : 
            return root.key 
        elif root.key>x : 
            root=root.left 
        else : 
            res=root 
            root=root.right
    return res.key
root=Node(50)
root.left=Node(30)
root.right=Node(70) 
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(80) 
root.right.left.left=Node(55)
root.right.left.right=Node(65) 
print("Floor of 58 : ",getFloor(root,58))
print("Floor of 50 : ",getFloor(root,50)) 
print("\n")  


## Ceil of BST 
print("Ceil of BST : ")
def getCeil(root, x) : 
    res=None 
    while root!=None : 
        if root.key==x : 
            return root.key 
        elif root.key<x : 
            root=root.right 
        else : 
            res=root 
            root=root.left 
    return res.key 
root=Node(50) 
root.left=Node(30) 
root.left.left=Node(20) 
root.left.right=Node(40) 
root.right=Node(70) 
root.right.left=Node(60) 
root.right.left.left=Node(55) 
root.right.left.right=Node(65) 
root.right.right=Node(78)  
print("Ceil of 69 : ",getCeil(root, 69))
print("Ceil of 63 : ",getCeil(root, 63)) 
print("\n") 