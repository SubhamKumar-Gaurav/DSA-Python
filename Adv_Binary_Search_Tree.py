# Adv Binary Search Tree 
#   Ceiling on the left side in an array 
#   Find Kth smallest in BST 
#   Check for BST 
#   Fix BST with Two Nodes Swapped 
#   Pair sum with given BST  


# Class Defn. 
class Node : 
    def __init__(self, k) : 
        self.key=k 
        self.left=None 
        self.right=None 


## Ceiling on the left side in an array 
# Naive solution      Time: O(n^2) 
def print_Ceiling(arr) : 
    n=len(arr) 
    print("-1", end=" ") 
    for i in range(1, n) : 
        diff=float("inf") 
        for j in range(i) : 
            if arr[j]>=arr[i] : 
                diff=min(diff, arr[j]-arr[i]) 
        if diff==float("inf") : 
            print("-1", end=" ") 
        else : 
            print(arr[i]+diff , end=" ")
arr=[2,8,30,15,25,12]
print("Ceiling on the left side ")
print("Naive : ", end=" ")
print_Ceiling(arr)
print() 

# Efficient approach     Time: O(n)
def printCeiling(arr) : 
    n=len(arr) 
    print("-1", end=" ")
    s=set() 
    s.add(arr[0]) 
    for i in range(1, n) : 
        it=[x for x in s if x>=arr[i]] 
        if len(it)==0 : 
            print("-1", end=" ") 
        else : 
            print(min(it), end=" ")
        s.add(arr[i]) 
arr=[2,8,30,15,25,12]
print("Efficient : ", end=" ")
printCeiling(arr) 
print("\n") 



## Find Kth smallest in BST 
# Naive solution   Time : O(n)
def printKth(root, k) : 
    if root!=None : 
        printKth(root.left, k) 
        printKth.count+=1 
        if printKth.count==k : 
            print(root.key) 
            return 
        printKth(root.right, k) 
root=Node(50) 
root.left=Node(20) 
root.left.left=Node(10) 
root.left.right=Node(40) 
root.right=Node(100) 
root.right.left=Node(70) 
root.right.left.left=Node(60) 
root.right.left.right=Node(80) 
root.right.right=Node(120) 
printKth.count=0
print("Kth smallest in BST ")
print("Naive : ", end=" ")
k=3
printKth(root, k)


# Efficient solution    Time: O(logn) 
def kthSmallest(root, k, count) : 
    if root is None : 
        return None 
    left=kthSmallest(root.left, k, count) 
    if left is not None : 
        return left 
    count[0]+=1  
    if count[0]==k : 
        return root.key
    return kthSmallest(root.right, k, count) 

def printKthSmallest(root, k): 
    count=[0] 
    res=kthSmallest(root, k, count)  
    if res is None : 
        print("There are less than k nodes in the BST") 
    else :
	    print("Efficient : ", res)

root=Node(50) 
root.left=Node(20) 
root.left.left=Node(10) 
root.left.right=Node(40) 
root.right=Node(100) 
root.right.left=Node(70) 
root.right.left.left=Node(60) 
root.right.left.right=Node(80) 
root.right.right=Node(120)
printKthSmallest(root, k) 
print("\n")



## Check for BST 
# Naive approach   Time: O(n^2)
INT_MIN=float("-inf")
def maxvalue(root) : 
    if root is None : 
        return INT_MIN  
    res=root.key 
    lres=maxvalue(root.left)
    rres=maxvalue(root.right)
    if lres>res : 
        res=lres 
    if rres>res : 
        res=rres 
    return res 

INT_MAX=float("inf") 
def minvalue(root) : 
    if root is None : 
        return INT_MAX   
    res=root.key 
    lres=minvalue(root.left)
    rres=minvalue(root.right)
    if lres<res : 
        res=lres 
    if rres<res : 
        res=rres 
    return res 

def isBST(root) : 
    if root is None : 
        return True 
    if root.left!=None and maxvalue(root.left)>root.key : 
        return False  
    if root.right!=None and minvalue(root.right)<root.key : 
        return False   
    if (not isBST(root.left) or not isBST(root.right)) : 
        return False  
    return True  


# Efficient approach    
def isBSTUtil(root, minval, maxval) : 
    if root is None : 
        return True 
    if root.key<=minval or root.key>=maxval : 
        return False 
    return isBSTUtil(root.left, minval, root.key) and isBSTUtil(root.right, root.key, maxval) 



## Fix BST with Two Nodes Swapped 
def inorder(root) : 
    if root : 
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right) 

prevv=None 
first=None 
second=None 
def correctBSTutil(root, first, middle, last, prev) : 
    if root : 
        correctBSTutil(root.left, first, middle, last, prev) 
        if prev[0] and root.key<prev[0].key : 
            if (not first[0]) : 
                first[0]=prev[0] 
                middle[0]=root 
            else :
                last[0]=root 
        prev[0]=root 
        correctBSTutil(root.right, first, middle, last, prev)

def correctBST(root) : 
    first=[None]
    middle=[None]
    last=[None]
    prev=[None]
    correctBSTutil(root, first, middle, last, prev) 
    if first[0] and last[0] : 
        first[0].key, last[0].key = last[0].key, first[0].key 
    elif first[0] and middle[0] : 
        first[0].key, middle[0].key = middle[0].key, first[0].key 
print("Fix BST with Two Nodes Swapped")
root=Node(18)
root.left=Node(60)
root.left.left=Node(4)
root.right=Node(70)
root.right.left=Node(8)
root.right.right=Node(80) 
print("Before swapping : ", end=" ")
inorder(root)
print()
correctBST(root)
print("After swapping : ", end=" ")
inorder(root)
print("\n") 


## Pair sum with given BST   , x=sum_val , s=set()
def isPairSum(root, x, s) : 
    if root is None :  
        return False 
    if isPairSum(root.left, x, s) : 
        return True 
    if x-root.key in s : 
        print(f"Pair Found : {x-root.key} + {root.key} = {x}") 
    else : 
        s.add(root.key) 
    return isPairSum(root.right, x, s) 
root=Node(10)
root.left=Node(8)
root.left.left=Node(4)
root.left.right=Node(9)
root.right=Node(20)
root.right.left=Node(11)
root.right.right=Node(30)
root.right.right.left=Node(25)
s=set()
isPairSum(root, 18, s)
s=set()
isPairSum(root, 19, s)  # Prints all the pairs 
s=set() 
print(isPairSum(root, 2, s))