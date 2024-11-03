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