## Matrix 
#    Multidimensional array in python 
#    Passing a 2D array as argument  
#    Matrix in Snake Pattern 
#    Matrix Boundary Traversal
#    Transpose of a Matrix 
#    Rotate matrix anticlockwise by 90 degree 
#    Spiral Traversal of matrix 
#    Search in a row and column wise sorted matrix 
#    Median of a rw wise sorted matrix 


## Multidimensional array in python  
arr=[[1,2,3], [4,5,6]] 
print("Matrix Traversal - 1")
for r in arr : 
    for x in r : 
        print(x, end=" ")
    print()
print("No. of rows : ", len(arr))
print("Count in the first row : ", len(arr[0]))
print("Count in the second row : ", len(arr[1])) 
print() 

# An alternate way of Traversal
print("An alternate way of Traversal") 
arr=[[1,2,3], [4,5,6,7,8]] 
for i in range(len(arr)) : 
    for j in range(len(arr[i])) : 
        print(arr[i][j], end=" ")
    print() 

# User specified dimensions - Not recommended 
print("User specified dimensions - Not recommended ")
rows=3 
cols=4 
arr=[[0]*cols]*rows 
arr[0][0]=1 
for r in arr : 
    print(r)
print() 

print("Recommended way ")
arr=[[0 for i in range(cols)] for j in range(rows)]
arr[0][0]=1 
for r in arr : 
    print(r) 
print() 



## Passing a 2D array as argument 
print("Passing a 2D array as argument : ")
def printMatrix(mat) : 
    M=len(mat)
    N=len(mat[0]) 
    for i in range(M) : 
        for j in range(N) : 
            print(mat[i][j], end=" ") 
if __name__=="__main__" : 
    mat=[[10,20], [30,40], [50,60]] 
    printMatrix(mat)
print("\n") 


## Matrix in Snake Pattern 
def snakePattern(mat) : 
    for i in range(len(mat)) : 
        if i%2==0 :
            for j in range(len(mat[i])) :  
                print(mat[i][j], end=" ") 
        else : 
            for j in range(len(mat[i])-1, -1, -1) : 
                print(mat[i][j], end=" ") 



## Matrix Boundary Traversal 
def boundary(mat) : 
    r=len(mat)
    c=len(mat[0])
    if r==1 : 
        for i in range(c) : 
            print(mat[0][i], end=" ")
    elif c==1 : 
        for i in range(r) : 
            print(mat[i][0], end=" ") 
    else : 
        for i in range(c) : 
            print(mat[0][i], end=" ")
        for i in range(1,r) : 
            print(mat[i][c-1], end=" ")
        for i in range(c-2, -1, -1) : 
            print(mat[r-1][i], end=" ")
        for i in range(r-2,0,-1) : 
            print(mat[i][0], end=" ")


## Transpose of a Matrix  
def transpose(mat) : 
    n=len(mat) 
    for i in range(n) : 
        for j in range(i+1,n) : 
            mat[i][j] , mat[j][i] = mat[j][i], mat[i][j] 
    return mat  




## Rotate matrix anticlockwise by 90 degree 
# Naive solution 
def rotate90(mat) : 
    n=len(mat)
    temp=[[0 for _ in range(n)] for _ in range(n)]  
    for i in range(n) : 
        for j in range(n) : 
            temp[n-j-1][i]=mat[i][j] 
    for i in range(n) : 
        for j in range(n) : 
            mat[i][j]=temp[i][j]
    return mat 


def rotate90acc(mat) : 
    n=len(mat)
    for i in range(n) :   ## Transpose 
        for j in range(i+1,n) : 
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(n) :   ## reversing columns 
        for j in range(n//2) : 
            mat[j][i], mat[n-j-1][i] = mat[n-j-1][i], mat[j][i] 
    return mat 
