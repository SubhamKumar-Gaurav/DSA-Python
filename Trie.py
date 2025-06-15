## Trie 
class TrieNode : 
    child=[None] * 26 
    isEndOfWord=False 

def insert(node, key) : 
    for x in key : 
        i=ord(x)-ord('a') 
        if node.child[i] is None : 
            node.child[i]=TrieNode() 
        node=node.child[i] 
    node.isEndOfWord=True 