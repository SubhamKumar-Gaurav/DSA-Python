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



## Rat in a Maze 
# Top left - start ,  Bottom right - end 
# Movements - only two direction - either bottom or right 
def printSol(sol) :
    N=len(sol) 
    for i in range(N) :
        for j in range(N) :  
            print(sol[i][j], end=" ")
        print() 

def isSafe(maze, i, j) : 
    return i<len(maze) and j<len(maze) and maze[i][j]==1 

def solveMaze(maze) : 
    N=len(maze) 
    sol=[[0 for j in range(N)] for i in range(N)]  

    if solveMazeRec(maze, 0, 0, sol)==False : 
        print("Solution does not exists") 
        return False 
    printSol(sol) 
    return True 

def solveMazeRec(maze, i, j, sol) : 
    if i==len(maze)-1 and j==len(maze)-1 and maze[i][j]==1 : 
        sol[i][j]=1 
        return True 
    if isSafe(maze, i, j) : 
        sol[i][j]=1 
        if solveMazeRec(maze, i+1, j, sol) :
            return True 
        if solveMazeRec(maze, i, j+1, sol) : 
            return True 
        sol[i][j]=0 
    return False 
maze=[  [1,0,0,0], 
        [1,1,0,0], 
        [0,1,1,0], 
        [0,1,1,1] ] 
print("Rat in a maze : ")
solveMaze(maze)
print("\n") 



## N Queen problems
def isSafe(row, col) : 
    for i in range(col) : 
        if board[row][i] : 
            return False 
    i, j = row, col 
    while i>=0 and j>=0 : 
        if board[i][j] : 
            return False 
        i-=1 
        j-=1 
    i, j = row, col 
    while i<N and j>0 : 
        if board[i][j] : 
            return False 
        i+=1 
        j-=1 
    return True 

def solve() : 
    if solveRec(0)==False : 
        return False 
    for i in range(N) : 
        for j in range(N) : 
            print(board[i][j], end=" ") 
        print() 
    return True 

def solveRec(col) : 
    if col==N : 
        return True 
    for i in range(N) : 
        if isSafe(i, col) : 
            board[i][col]=1 
            if solveRec(col+1) : 
                return True 
            board[i][col]=0 
    return False 
N=4 
board=[[0 for j in range(N)] for i in range(N)] 
solve()
print("\n")  



