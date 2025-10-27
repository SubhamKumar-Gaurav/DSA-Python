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
print("\n") 


## Update Query in Segment Tree  
print("Update Query in Segment Tree : ")   
def update(ss, se, i, si, diff) : 
    if si<ss or si>se : 
        return 
    tree[si]+=diff 
    if se>ss : 
        mid=(ss+se)//2 
        update(ss, mid, i, 2*si+1, diff) 
        update(mid+1, se, i, 2*si+2, diff)  

update(0,3,1,0,5) 
print("getSumRec(0,1,0,3,0) : ", getSumRec(0,1,0,3,0)) 



## Binary Indexed Tree 
# Get Sum in Binary Indexed Tree 
def getSumBIT(i) :
    i=i+1 
    res=0 
    while i>0 : 
        res=res+BITree[i] 
        i=i-(i&(-i)) 
    return res 

# Update in Binary Indexed tree
def updateBIT(i, x) : 
    diff=x-arr[i] 
    arr[i]=x 
    i=i+1 
    while i<len(BITree) : 
        BITree[i]+=diff 
        i=i+(i&(-i)) 


# Construction of Binary Indexed Tree 
arr=[10,20,30,40,50] 
n=len(arr) 
bITree=[0]*(n+1) 
for i in range(n) : 
    updateCBIT(i, arr[i]) 

def updateCBIT(i, x) : 
    i=i+1 
    while i<=n : 
        bITree[i]+=x 
        i=i+(i&(-i)) 