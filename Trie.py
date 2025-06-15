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

