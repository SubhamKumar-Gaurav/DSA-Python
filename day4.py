# Day -4 
# List : 
#   Basics 
#   Average or mean of a list 
#   Separate odd/even 
#   Slicing (list, tuple, string)


# Basics :
# Inserting elements in list :
print("Inserting elements in list :")
l1=[10,20,30,40,50] 
l1.append(30)
print(l1)
l1.insert(1,15)
print(l1)
print(15 in l1)
print(l1.count(30))
print(l1.index(30))
print(l1.index(30,4,7)) 
print("\n") 

# Python functions to demonstrate removal of items 
print("Python functions to demonstrate removal of items :")
l2=[10,20,30,40,50,60,70,80] 
l2.remove(20)
print(l2)
print(l2.pop())
print(l2)
print(l2.pop(2)) 
print(l2)
del l2[1]
print(l2) 
del l2[0:2] 
print(l2) 
print("\n") 

# Some general purpose functions :
print("Some general purpose functions on integers :")
l3=[10,40,20,50] 
print(max(l3)) 
print(min(l3)) 
print(sum(l3)) 
l3.reverse() 
print(l3) 
l3.sort() 
print(l3) 
print("\n")

print("Some general purpose functions on string :")
l4=['efg','abc','gfg','def'] 
print(max(l4)) 
print(min(l4)) 
l4.reverse()
print(l4)
l4.sort() 
print(l4) 
print("\n")


# Average / Mean :
def avg1(l) :
    sum=0 
    for x in l :
        sum+=x 
    n=len(l) 
    return sum/n 
l=[10,20,30,40,5]
print("Average of a list :")
print(avg1(l))
print("\n")

def avg2(l) :
    return sum(l)/len(l)
print("Avg of a list using sum,len functions : ")
print(avg2(l))
print("\n") 
   

# Separate even , odd :
def sep1(l) :
    even=[]
    odd=[] 
    for i in l :
        if i%2==0 :
            even.append(i)
        else :
            odd.append(i)    
    return even, odd 
l=[10,20,30,40,5]
even,odd=sep1(l) 
print("even : ",even)
print("odd : ",odd)
print("\n") 

# Two pinter approach : 
# Separating odd, even using two pointer approach : (order need not be same)
def sep2(l) :  # odd first then even 
    n=len(l)
    i=-1
    j=0
    while j!=n :
        if l[j]%2==1 :
            i+=1
            l[i],l[j]=l[j],l[i]  
        j+=1 
    return l 
l=[1,3,2,8,4,3,7,8]
print("Odd Even using 2 pointer approach : ")
print(sep2(l)) 

def sep3(l) :   # Even first then odd 
    n=len(l)
    i=-1 
    j=0
    while j!=n :
        if l[j]%2==0 :
            i+=1 
            l[i],l[j]=l[j],l[i]  
        j+=1 
    return l 
print("Even odd using 2 pointer approach : ")        
print(sep3(l))
print("\n") 


# Slicing :
# List
l1=[10,20,30,40,50]
l2=l1[:]
print("l1 : ", l1)
print("l2 : ", l2)
print("l1 is l2 : ", l1 is l2 )
print("l2 is l1 : ", l2 is l1 )
# Tuple
t1=(10,20,30,40,50)
t2=t1[:]
print("t1 : ", t1)
print("t2 : ", t2)
print("t1 is t2 : ", t1 is t2 )
print("t2 is t1 : ", t2 is t1 )
# String 
s1="SKG"
s2=s1[:]
print("s1 : ", s1)
print("s2 : ", s2)
print("s1 is s2 : ", s1 is s2 )
print("s2 is s1 : ", s2 is s1 )
