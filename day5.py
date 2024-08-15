# Day - 5 
# List 
#   Comprehensions 


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