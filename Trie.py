## Trie 
class TrieNode : 
    child=[None] * 26 
    isEndOfWord=False 


## insert 
def insert(node, key) : 
    for x in key : 
        i=ord(x)-ord('a') 
        if node.child[i] is None : 
            node.child[i]=TrieNode() 
        node=node.child[i] 
    node.isEndOfWord=True 


## search 
def search(node, key) : 
    for x in key : 
        i=ord(x)-ord("a") 
        if node.child[i] is None : 
            return False 
        node=node.child[i] 
    return node.isEndOfWord 


## delete 
def delNode(rrot, key, i=0) : 
    if root==None : 
        return None 
    if i==len(key) : 
        if root.isEndOfWord : 
            root.isEndOfWord=False 
        if isEmpty(root) : 
            root=None 
        return root 
    index=ord(key[i])-ord("a") 
    root.child[index]=delNode(root.child[index], key, i+1)  
    if isEmpty(root) and root.isEndOfWord==False : 
        root=None 
    return root 

def isEmpty(root) : 
    for x in root.child : 
        if x!=None : 
            return False 
    return True 



## Count distinct rows in binary matrix 
class TrieNode : 
    def __init__(self) : 
        self.child=[None]*2 

def insert(node, row) : 
    isNew=False 
    for e in row : 
        if not node.child[e] : 
            node.child[e]=TrieNode() 
            isNew=True 
        node=node.child[e] 
    return isNew 

def countDist(mat) : 
    res=0 
    root=TrieNode() 
    for i in range(len(mat)) : 
        if insert(mat[i]) : 
            res=res+1 
    return res 
    