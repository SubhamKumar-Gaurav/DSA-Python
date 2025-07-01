## Segment Tree 
    # Construction 
    # Range Query 
    # Update Query 

## Binary Indexed Tree 
    # Prefix Sum 
    # Update operation 
    # Construction 



# Segment Tree Construction 
def buildTree(ss, se, si) : 
    global arr  
    global tree 
    if ss==se : 
        tree[si]=arr[ss]
        return arr[ss] 
    mid=(ss+se)//2 
    tree[si]=buildTree(ss, mid, 2*si + 1) + buildTree(mid+1, se, 2*si + 2)  
    return tree[si]  

arr=[10,20,30,40]
n=len(arr)
tree=[0]*(4*n)
buildTree(0,3,0)
print(tree) 