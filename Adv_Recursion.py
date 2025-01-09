## Advanced Recursion 
#    Rope cutting problem 
#    Subset of a given string 
#    Tower of Hanoi 
#    Josephus problem 
#    Subset sum problem 
#    Printing all permutations 


## Rope cutting problem 
def ropeCut(n,a,b,c) : 
    if n==0 : 
        return 0 
    if n<0 : 
        return -1 
    res=max(ropeCut(n-a,a,b,c), ropeCut(n-b,a,b,c), ropeCut(n-c,a,b,c)) 
    if res==-1 : 
        return -1 
    return res+1 
print("Rope cutting problem ")
print("n=5, a=2, b=5, c=1 : ",ropeCut(5,2,5,1))
print("n=23, a=12, b=9, c=11 : ",ropeCut(23,12,9,11))
print("n=5, a=4, b=2, c=6 : ",ropeCut(5,4,2,6)) 
print("\n") 


## Subset of a given string 
print("Subset of a given string")
def sub(str, curr, ind) : 
    if ind==len(str) : 
        print(curr, end=" ")
        return 
    sub(str,curr,ind+1) 
    sub(str,curr+str[ind],ind+1) 
s="ABC" 
print(sub(s," ",0)) 
print("\n")


## Tower of Hanoi
print("Tower of Hanoi")
def TOH(n,A,B,C) : 
    if n==1 : 
        print("Move 1 from", A , "to", C)
    else : 
        TOH(n-1,A,C,B) 
        print("Move", n, "from", A, "to", C)
        TOH(n-1,B,A,C)
print("n=3, A, B, C : ") 
TOH(3,"A", "B", "C")  
print("\n") 


## Josephus problem 
print("Josephus problem")  
def Josephus(n,k) : 
    if n==1 : 
        return 0 
    else : 
        return (Josephus(n-1,k)+k)%n 
print("n=5, k=3 : ", Josephus(5,3)) 
print("\n") 


## Subset sum problem 
print("Subset sum problem")
def subsetSum(arr,n,sum) : 
    if n==0 : 
        if sum==0 : 
            return 1 
        else : 
            return 0 
    return subsetSum(arr,n-1,sum) + subsetSum(arr,n-1,sum-arr[n-1])
arr=[10,20,15]
n=len(arr) 
print("[10,20,15], sum=25 : ", subsetSum(arr,n,25))
print("\n") 


## Print all permutations of a string 
print("Print all permutations : ") 
def permute(s,i) : 
    n=len(s) 
    if (i==n-1) : 
        print("".join(s))
        return 
    for j in range(i,n) : 
        s[i], s[j] = s[j], s[i] 
        permute(s,i+1)
        s[i], s[j] = s[j], s[i] 
s=["A","B","C"]
print('["A","B","C"] : ')
permute(s,0)
print("\n") 