# Backtracking
#   Concept of backtracking 
#   Rat in a Maze 
#   N Queen problems 
#   Sudoku problems 


## Concept of Backtracking 
# Permutations of "ABC" which does contain "AB" 
## Naive approach 
def permute(s, l, r) : 
    if l==r : 
        if "AB" not in "".join(s) : 
            print("".join(s), end=" ") 
        return 
    else : 
        for i in range(l, r+1) : 
            s[i], s[l] = s[l], s[i] 
            permute(s, l+1, r)  
            s[i], s[l] = s[l], s[i] 
s=["A", "B", "C"]
print("Permutations of ABC (Naive)")
permute(s, 0, 2)
print()


## Backtracking 
def isSafe(s, l, i, r) : 
    if l!=0 and s[l-1]=="A" and s[i]=="B" : 
        return False 
    if r==l+1 and s[i]=="A" and s[l]=="B" : 
        return False 
    return True 

def permute(s, l, r) : 
    if l==r : 
        print("".join(s), sep="", end=" ")
        return 
    else : 
        for i in range(l, r+1) :  
            if isSafe(s, l , i , r) : 
                s[i], s[l] = s[l], s[i] 
                permute(s, l+1, r)
                s[i], s[l] = s[l], s[i]  
s=["A", "B", "C"] 
print("Permutations of ABC (Backtracking)")
permute(s, 0 , 2)
print("\n")

