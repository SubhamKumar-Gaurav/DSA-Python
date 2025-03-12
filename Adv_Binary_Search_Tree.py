# Adv Binary Search Tree 
#   Ceiling on the left side in an array 
#   Find Kth smallest in BST 
#   Check for BST 
#   Fix BST with Two Nodes Swapped 
#   Pair sum with given BST  


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


