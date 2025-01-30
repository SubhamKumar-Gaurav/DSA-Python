## Adv String 
#   Pattern searching 




## Pattern searching 
def patternSearching(txt, pat) : 
    pos=txt.find(pat) 
    while pos>=0 : 
        print(pos)
        pos=txt.find(pat) 

# Naive approach 
def naivePat(txt, pat) : 
    n=len(txt) 
    m=len(pat) 
    for i in range(n-m+1) : 
        j=0 
        while j<m : 
            if pat[j]!=txt[i+j] : 
                break 
            j+=1 
        if j==m : 
            print(i, end=" ")

## Improved Naive Pattern Searching with distinct pattern 
def distinctSearch(txt, pat) : 
    n=len(txt)
    m=len(pat) 
    i=0 
    while i<=(n-m) : 
        for j in range(m) : 
            if pat[j]!=txt[i+j] : 
                break 
        if j==m-1 : 
            print(i, end=" ")
        if j==0 : 
            i+=1 
        else : 
            i+=j 
