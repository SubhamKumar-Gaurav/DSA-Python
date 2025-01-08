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
