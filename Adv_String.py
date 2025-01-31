## Adv String 
#   Pattern searching 
#   Improved Naive Pattern Searching with distinct pattern 
#   Rabin Karp Algorithm 
#   KMP Algorithm 
#   Anagram 
#   Lexicographic rank of a string 
#   Longest substring with distinct characters


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


## Rabin Karp Algorithm 
d=256 
def RabinKarp(txt, pat, q) : 
    m, n = len(pat), len(txt)
    h=1 
    for i in range(m-1) :   # pow(d, m-1)%q 
        h=(h*d)%q

    p, t = 0, 0 
    for i in range(m) :     # hash value of pattern and first window 
        p=(p*d + ord(pat[i]))%q 
        t=(t*d + ord(txt[i]))%q 

    flag=True 
    for i in range(n-m+1) : 
        if p==t : 
            for j in range(m) : 
                if txt[i+j]!=pat[j] :  
                    break 
                else : 
                    j+=1 
            if j==m : 
                print(i) 
                flag=False 
        
        if i<n-m : 
            t=(d*(t-ord(txt[i])*h)+ ord(txt[i+m]))%q  
            if t<0 : 
                t=t+q 
    if flag : 
        print("Not Found")
    