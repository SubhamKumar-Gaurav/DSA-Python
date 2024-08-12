# Day -4 
# List : 
#   Basics 
#   


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
