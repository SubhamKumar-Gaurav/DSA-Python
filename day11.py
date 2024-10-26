# Searching 
#     Count occurences in a sorted array 
#     Count 1's in sorted binary list 
#     Square root 


# Count occurences in a sorted array  
# Efficient solution 
def f_occ(l,x) :      # function for first occurrence 
    low=0 
    high=len(l)-1 
    
    while low<=high : 
        mid=(low+high)//2 
        if l[mid]<x : 
            low=mid+1 
        elif l[mid]>x : 
            high=mid-1 
        else : 
            if mid==0 or l[mid-1]!=l[mid] : 
                return mid 
            else : 
                high=mid-1 

def l_occ(l,x) :     # function for last occurrence
    low=0 
    high=len(l)-1 
    while low<=high : 
        mid=(low+high)//2 
        if l[mid]<x : 
            low=mid+1 
        elif l[mid]>x :
            high=mid-1 
        else : 
            if mid==len(l)-1 or l[mid]!=l[mid+1] : 
                return mid 
            else : 
                low=mid+1 

def occ(l,x) :   # last - first + 1
    first=f_occ(l,x)
    last=l_occ(l,x)
    return last-first+1 

l=[10,20,20,20,20,30,30,40,40,50]
print("Total occurrences of 30 : ", occ(l,30)) 
print("Total occurrences of 20 : ", occ(l,20)) 
