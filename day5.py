# Day - 5 
# List 
#   Comprehensions 
#   Largest element in a list - 2 approaches 
#   Second largest element in a list - 2 approaches 
#   Check if list is sorted or not - 2 approaches  


# Comprehension in Python : 
even=[x for x in range(11) if x%2==0]
odd=[x for x in range(11) if x%2==1] 
print("Even using list comprehension : " , even) 
print("Odd using list comprehension : " , odd) 
print("\n") 

# functions to get a list that contains all those items of l that are smaller than x :
def getsmaller(l,x) :
    return [e for e in l if e<x ] 
l=[9,15,12,3,7,11] 
x=10 
print("getsmaller : ",getsmaller(l,x)) 
print("\n") 

# Returns two lists : first list - even , second list - odd 
def getevenodd(l) :
    even=[x for x in l if x%2==0]
    odd=[x for x in l if x%2==1]
    return even, odd 
l=[10,3,20,5,12]
even,odd=getevenodd(l)
print("Even : ",even)
print("Odd : ",odd)  
print("\n") 

# comprehension on strings :
s="geekforgeeks" 
l1=[x for x in s if x in "aeiou"] 
print("Characters that are vowels : ",l1) 

l2=['geeks','idle','courses','gfg'] 
l3=[x for x in l2 if x.startswith("g")] 
print("Strings starting with g : ",l3) 

l4=[x*2 for x in range(6)] 
print("Multiples of 2 : ", l4)

l1=['geeks','for','geeks','gfg','ide'] 
l2=[x.upper() for x in l1 if x.startswith("g")] 
print("Capitalise string if it starts with g : ",l2) 
print("\n")

# Set Comprehension 
l=[10,20,3,4,10,20,7,3] 
s1={x for x in l if x%2==0} 
s2={x for x in l if x%2!=0} 
print("Returning the set having even numbers : ",s1)
print("Returning the set having odd numbers : ",s2) 

# Dictionary comprehension : 
l1=[1,3,4,2,5] 
d1={x:x**3 for x in l} 
print("Power of 3 : ",d1) 

d2={x:f"ID{x}" for x in range(5)} 
print("Set comprehension with format specifier : ", d2) 
print("\n") 

l2=[101,103,102] 
l3=["gfg","ide","courses"] 
d3={l2[i]:l3[i] for i in range(len(l2))} 
print("Creating a dictionary with two lists : ") 
print("d3 : ",d3) 
print("Alternative way : ") 
d4=dict(zip(l2,l3)) 
print("d4 : ",d4)  
print("\n") 

# Inverting a dictionary  (key becomes value) and value becomes key 
d1={101:"gfg" , 103:"practice" , 102:"ide"} 
d2={v:k for (v,k) in d1.items()} 
print("Inverting a dictionary : ")
print(d2)  

## Larget element in a list : 2 approaches 
# Approach 1 : O(n^2) time complexity 
def max1(l) :
    for x in l :
        for y in l :
            if y>x :
                break 
        else :
            return x 
    return None 
l=[10,20,5,50]  
print("Largest element in list : ")       
print("Approach 1 : ",max1(l)) 
print("\n")    

# Approach 2 : O(n) time complexity 
def max2(l) :
    res=l[0] 
    for i in range(1,len(l)) :
        if l[i]>res :
            res=l[i] 
    return res 
l=[10,20,3,5,50]         
print("Largest element in list : ")       
print("Approach 2 : ",max2(l))
print("\n") 

# Second largest element in a list :  
def secmax1(l) :
    if len(l)==1 :
        return None 
    lar=max2(l)
    slar=None
    for x in l :
        if x!=lar : 
            if slar==None :
                slar=x 
            else :
                slar=max(slar,x) 
    return slar 
l=[10,20,40,30,100,30,90,80]                
print("Second largest element in a list : ",secmax1(l)) 

def secmax2(l) :
    if len(l)<=1 :
        return None 
    lar=l[0] 
    slar=None 
    for x in l[1:] :
        if x>lar :
            slar=lar 
            lar=x 
        elif x!=lar :
            if slar==None or slar<x :
                slar=x 
    return slar 
l=[10,20,30,40,50,50] 
print("Second largest in list : ",secmax2(l))
print("\n") 

## Check if list is sorted or not 
# Approach 1 : using loop   (Preferred method)
def sort1(l) : 
    i=1 
    while i<len(l) :
        if l[i]<l[i-1] :
            return False 
        i+=1 
    return True 
l=[10,20,30,20,500]  
print("Checking sort using loop : ",sort1(l))    

# Approach 2 :  using sorted function ; sorted() - does not modify list  
def sort2(l) :
    sl=sorted(l) 
    if sl==l :
        return True 
    else :
        return False 
l=[10,20,304,400]
print("Checking sort using sp\orted function :" , sort2(l)) 

