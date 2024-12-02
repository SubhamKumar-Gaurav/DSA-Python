# Day - 6 
#  Reversing a list - 4 methods 
#  Remove Duplicates (Counting unique items) - 2 methods 
#  Rotating a list - 3 approaches 


## Reversing a list 
# Method 1 :
l=[10,20,30,40,50] 
l.reverse() 
print("List Reversal using reverse() function : ",l) 
print("\n") 

# Method 2 :
l=[10,20,30,40,50,60] 
new_l=list(reversed(l)) 
print("List reversal using revrsed() : ",new_l)  
print("\n") 

# Method 3 :
l=[10,20,30,40,50]
new_l=l[::-1] 
print("List reversal using slicing : ", new_l) 
print("\n") 

# Method 4 :  (using loop)
def rlist1(l) :   # using for loop 
    n=len(l)
    for i in range(n//2) :
        l[i],l[n-i-1]=l[n-i-1],l[i] 
    return l 
l=[10,20,30,40,50]     
print("List Reversal using for loop :",rlist1(l)) 

def rlist2(l) : 
    n=len(l)
    i=0  
    j=n-1 
    while i<j :
        l[i],l[j]=l[j],l[i] 
        i+=1 
        j-=1 
    return l 
l=[10,20,30,40,50]     
print('List Reversal using for loop :',rlist2(l)) 


## Remove duplicates from a sorted array :  (Counting unique elements)
# Approach 1 :  Naive approach 
def remdup(arr,n) :
    temp=[0]*n 
    temp[0]=arr[0]  
    res=1 
    for i in range(1,n) :
        if temp[res-1]!=arr[i] :
            temp[res]=arr[i] 
            res+=1 
    for i in range(0,res) :
        arr[i]=temp[i] 
    return res 
l=[10,20,20,30,30,30,30] 
n=len(l)
print("Using extra space : ",remdup(l,n))            

# Approach 2 : Without using extra space 
def removedup(arr,n) :
    res=1 
    for i in range(1,n) :
        if (arr[res-1]!=arr[i]) :
            arr[res]=arr[i] 
            res+=1 
    return res 
l=[10,20,20,30,30,30,30] 
n=len(l)
print("Without using extra space : ",removedup(l,n))     


## Rotating a list by one on left 
# Approach 1 : using slicing 
l=[10,20,30,40,50]
l=l[1:]+l[:1]
print("Rotating list using slicing : ",l) 

# Approach 2 : using pop and append 
l=[10,20,30,40,50]
l.append(l.pop(0))
print("Rotating list using pop and append : ",l) 

# Approach 3 : 
def rotatebyone(l) :
    n=len(l) 
    x=l[0] 
    for i in range(1,n) :
        l[i-1]=l[i] 
    l[n-1]=x 
    return l 
l=[10,20,30,40,50] 
print("Rotating by one on left : ",rotatebyone(l)) 