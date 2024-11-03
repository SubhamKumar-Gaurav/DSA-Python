# Sorting 
#    Sorting in Python - sort() , sorted() 
#    List sort in Python 



## Sort() : 
#   Works only for list 
#   Sorts in place 
#   Uses Timsort (uses mergesort and insertion sort) and stable  
  
## Sorted() : 
#    Works for any iterables 
#    Does  not modify the passed container. Returns a list of sorted items 
#   Uses Timsort (uses mergesort and insertion sort) and stable 

## List sort in Python 
l1=[5,10,15,1]
l1.sort() 
print("l1 : ", l1)

l2=[5,10,3,1]
l2.sort(reverse=True) 
print("l2 : ", l2) 

l3=['gfg', 'ide', 'courses'] 
l3.sort() 
print("l3 : ", l3) 

# Key Parameter 
def myFun(s) : 
    return len(s) 

l=["gfg", 'courses', 'python'] 
l.sort(key=myFun)
print("On the basis of length of the string ")
print("l : ", l) 

l.sort(key=myFun, reverse=True)
print("reversed l : ", l) 

# Sorting user defined ojects : 
# 1. Using a separate method : 
class Point :
    def __init__(self,x,y) :
        self.x = x
        self.y = y 
def myFun1(s) : 
    return s.x 

l=[Point(1,15), Point(10,5), Point(3,8)] 
l.sort(key=myFun1) 
print("Sorts on the basis of x axis : ")
for i in l : 
    print(i.x, i.y)
print("") 

l=[Point(1,15), Point(10,5), Point(1,8)] 
print("priority given to first appearing element : ")
l.sort(key=myFun1) 
for i in l :
    print(i.x , i.y ) 
print("")

# 2. Using lt function : 
# Method 1 : Maintaining the same order ; if x is same 
class Point : 
    def __init__(self, x, y) : 
        self.x=x 
        self.y=y 
    def __lt__(self,other) : 
        return self.x < other.x  

l1=[Point(1,15), Point(10,5), Point(3,8)] 
l1.sort()  
print("Using lt function and maintaining the same order : ")
for i in l1 : 
    print(i.x, i.y) 
print("") 

# Method 2 : Sorting on the basis of y ; if x is same 
class Point : 
    def __init__(self, x, y) : 
        self.x=x 
        self.y=y 
    def __lt__(self,other) : 
        if self.x==other.x : 
            return self.y<other.y 
        else :
            return self.x < other.x  

l2=[Point(1,15), Point(10,5), Point(1,8)] 
l2.sort()  
print("Using lt function and sorting on the basis of y , if x is same : ")
for i in l2 : 
    print(i.x, i.y) 

    
## Sorted() in Python 
l=[10,20,14] 
ls=sorted(l) 
print(l) 
print(ls) 

l=[10,-15,-2,1] 
ls=sorted(l,key=abs,reverse=True) 
print(ls) 

t=(10,12,5,1) 
print(sorted(t)) 

s={"gfg", "courses", "python"} 
print(sorted(s)) 

st="gfg" 
print(sorted(st)) 

