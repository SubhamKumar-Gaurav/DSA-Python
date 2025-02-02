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
    

## Longest Proper Prefix Suffix array 
# Naive solution 
def longProPrefixSuffix(str, n) : 
    for length in range(n-1, -1, -1) : 
        for j in range(length) : 
            if str[j]!=str[n-length+j] : 
                break 
        else : 
            return length 
    return 0 
def fillLPS(str, lps) : 
    lps[0]=0 
    for i in range(1, len(str)) : 
        lps[i]=longProPrefixSuffix(str, i+1) 
    return lps
# s="abbabb" 
# lps=[0]*len(s)
# fillLPS(s, lps)
# print(lps)

# Efficient solution 
def fillLPS(s, lps ) : 
    n=len(s)
    lps[0]=0 
    i=1 
    length=0 
    while i<n : 
        if s[i]==s[length] : 
            length+=1 
            lps[i]=length 
            i+=1 
        else : 
            if length==0 : 
                lps[i]=0 
                i+=1 
            else : 
                length=lps[length-1] 
    return lps 
# s="abacabad" 
# lps=[0]*len(s) 
# print(fillLPS(s, lps))


## KMP Algorithm 
def fillLPS(pattern) : 
    n=len(pattern) 
    lps=[0]*n 
    length=0 
    i=1 
    while i<n : 
        if pattern[i]==pattern[length] : 
            length+=1 
            lps[i]=length 
            i+=1 
        else : 
            if length==0 : 
                lps[i]=0 
                i+=1 
            else : 
                length=lps[length-1] 
    return lps 

def KMP(pattern, text) : 
    n=len(text)
    m=len(pattern) 
    lps=fillLPS(pattern) 
    i=0 
    j=0 
    while i<n : 
        if pattern[j]==text[i] : 
            i+=1 
            j+=1 
        if j==m : 
            print(i-j, end=" ") 
            j=lps[j-1] 
        elif i<n and pattern[j]!=text[i] : 
            if j==0 : 
                i+=1 
            else : 
                j=lps[j-1] 


## Anagram    
# Naive solution 
CHAR=256 
def areAnagram(pat, txt, i) : 
    count=[0]*CHAR 
    for j in range(len(pat)) : 
        count[ord(pat[j])]+=1 
        count[ord(txt[i+j])]-=1  
    for j in range(CHAR) : 
        if count[j]!=0 : 
            return False 
    return True 

def isPresent(pat, txt) : 
    n=len(txt) 
    m=len(pat) 
    for i in range(n-m+1) : 
        if areAnagram(pat, txt, i) : 
            return True 
    return False 

# Efficient solution 
CHAR=256 
def areSame(CT, CP) : 
    for i in range(CHAR) : 
        if CT[i]!=CP[i] : 
            return False 
    return True 
def isAnagram(txt, pat) : 
    n=len(txt)
    m=len(pat) 
    CT=[0]*CHAR 
    CP=[0]*CHAR 
    for i in range(m) : 
        CT[ord(txt[i])]+=1 
        CP[ord(pat[i])]+=1 
    for i in range(m,n) : 
        if areSame(CT, CP) : 
            return True 
        CT[ord(txt[i])]+=1 
        CT[ord(txt[i-m])]-=1 
    return False 


## Lexicographic rank of a string 
# Efficient approach - Assumption : No duplicate characters
def fact(n) : 
    if n==0 : 
        return 1 
    return n*fact(n-1)
CHAR=256 
def lexRank(s) :  
    res=1 
    n=len(s) 
    mul=fact(n) 
    count=[0]*CHAR 
    for i in range(n) : 
        count[ord(s[i])]+=1 

    for i in range(1, CHAR) : 
        count[i]+=count[i-1] 

    for i in range(n-1) : 
        mul = mul//(n-i)   
        res+=count[ord(s[i])-1] * mul 
        for j in range(ord(s[i]), CHAR) : 
            count[j]-=1 
    return res 


## Longest Substring with distinct characters 
def areDistinct(s, i, j) : 
    visited=[0]*256 
    for k in range(i, j+1) : 
        if visited[ord(s[k])] : 
            return False 
        visited[ord(s[k])]=True 
    return True 
def longestDistinct(s) :  
    n=len(s) 
    res=0 
    for i in range(n) : 
        for j in range(i, n) : 
            if areDistinct(s, i, j) : 
                res=max(res, j-i+1) 
    return res 
