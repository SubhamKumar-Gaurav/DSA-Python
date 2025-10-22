## Segment Tree 
    # Construction 
    # Range Query 
    # Update Query 

## Binary Indexed Tree 
    # Prefix Sum 
    # Update operation 
    # Construction 



## Segment Tree Construction 
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
print("\n")



## Range Query in Segment Tree 
print("Range Query : ") 
arr=[10,20,30,40]
tree=[0]*7
buildTree(0,3,0) 
print("arr : ", arr)

def getSumRec(qs, qe, ss, se, si) : 
    if se<qs or ss>qe : 
        return 0 
    if qs<=ss and se<=qe : 
        return tree[si] 
    mid=(ss+se)//2  
    return getSumRec(qs, qe, ss, mid, 2*si+1) + getSumRec(qs, qe, mid+1, se, 2*si+2) 

print("getSum(0,2) : ", getSumRec(0, 2, 0, 3, 0)) 
print("getSum(1,3) : ", getSumRec(1, 3, 0, 3, 0)) 