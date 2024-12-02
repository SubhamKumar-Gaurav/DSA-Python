# Day - 7 
# Hashing  
#    Chaining 
#    Open Addressing 
#    Frequency of array elements - Naive approach , Dictionary approach 
#    Implementation of Open addressing 
#    Set in Python 
#    Count distinct elements in a list 



# Implementation of chaining : 
class MyHash :
    def __init__(self,b) : 
        self.BUCKET=b 
        self.table=[[] for x in range(b)]
    def insert(self,x) :
        i=x%self.BUCKET 
        self.table[i].append(x)
    def remove(self,x) :
        i=x%self.BUCKET 
        if x in self.table[i] :
            self.table[i].remove(x) 
    def search(self,x) :
        i=x%self.BUCKET 
        return x in self.table[i] 

h=MyHash(7)
h.insert(70)                  
h.insert(71)                  
h.insert(9)                  
h.insert(56)                  
h.insert(72)                  
print(h.search(56))
h.remove(56)
print(h.search(56))


# Frequencies of an array : 
# Naive Approach 
arr=[10,20,20,30,10] 
def freq1(arr) :
    for i in range(len(arr)) :
        flag=False 
        for j in range(i) :
            if arr[i]==arr[j] :
                flag=True 
                break 
        if flag==True :
            continue 
        count=1
        for k in range(i+1,len(arr)) :
            if arr[i]==arr[k] :
                count+=1 
        print(arr[i],count)
print("Frequencies of an array by Naive approach : ")
freq1(arr) 

# Dictionary approach - most efficient approach 
array=[10,20,20,30,10] 
def freq2(arr) :
    freq_d={}
    for i in arr :
        if i in freq_d :
            freq_d[i]+=1 
        else :
            freq_d[i]=1 
    return freq_d 
print("Frequency of array using dictionary : ")  
print(freq2(array)) 


# Implementation of Open Addressing 

# Sample class 
#     class myHash : 
#       def __init__(self,c) : 
#           self.cap=c 
#           self.table=[-1]*c 
#           self.size=0 
#       def hash(self,x) :
#           return x%self.cap 
#       def insert(self,x) :
#           ---------
#           --------- 
#       def search(self,x) : 
#           ---------
#           --------- 
#       def remove(self,x) :
#           ---------
#           ---------  


# Search method : 
def search(self,x) :
    h=self.hash(x) 
    t=self.table 
    i=h 
    while t[i]!=-1 :
        if t[i]==x :
            return True 
        i=(i+1)%self.cap 
        if i==h :
            return False 
    return False 

# Insert method :
def insert(self,x) :
    if self.size==self.cap :
        return False 
    if self.search(x)==True :
        return False 
    i=self.hash(x) 
    t=self.table 
    while t[i] not in (-1,-2) :
        i=(i+1)%self.cap 
    t[i]=x 
    self.size=self.size+1 
    return True 

# Remove method : 
def remove(self,x) :
    h=self.hash(x) 
    t=self.table 
    i=h 
    while t[i]!=-1 :
        if t[i]==x :
            t[i]=-2 
            return True 
        i=(i+1)%self.cap 
        if i==h :
            return False 
    return False 

# Important : How to handle cases when -1 and -2 can be input keys ?  
#              Ans : using "None" 

# Set : distinct elements, unordered, no indexing, 
#       Union, intersection, set difference etc are fast , 
#       Uses Hashing internally
s1={10,20,30} 
print("s1 set : ", s1) 
s2=set([20,30,40]) 
print("s2 set : ", s2 ) 
s3={} 
print("s3 set : " , s3) 
print("Type of s3 : ",type(s3)) 
s4=set()
print("s4 set : ", s4) 
print("Type of s4 : ", type(s4))  

# Set operations : [ adding and updating ]
print("Set operations : ")
s={10,20} 
s.add(30) 
print("after adding 30 : ", s) 
s.add(30) 
print("again adding 30 : ", s) 
s.update([40,50]) 
print("updating with [40,50] : ", s) 
s.update({60,70},[80,90]) 
print("updating with {60,70},[80,90] : ", s)  

# [ Removing an item from the set ]
print("Removing an item from the set : ") 
s={10,30,20,40} 
s.discard(30) 
print("Using discard function : ",s) 
s.remove(20) 
print("Using remove function : ",s) 
s.clear() 
print("Using clear function : ",s) 
s.add(50) 
# del s 
# print("del operator : ", s) 

# [ Union , intersection , difference ]  
s1={2,4,6,8} 
s2={3,6,9}  
print("Union of s1 and s2 : ", s1.union(s2) )  
print("Intersection of s1 and s2 : ", s1.intersection(s2) ) 
print("Difference of s1 and s2 , s1-s2 : ", s1.difference(s2) ) 
print("Difference of s1 and s2 , s2-s1 : ", s2.difference(s1) )  
print("Symmetric difference of s1 and s2 : ", s1.symmetric_difference(s2) )  

s1={2,4,6,8} 
s2={4,8} 
print(s1.isdisjoint(s2)) 
print(s1<=s2)  # subset 
print(s1<s2) 
print(s1>=s2)  # superset 
print(s1>s2) 


# Dictionary in Python :  
#   collection of key-value pair, unordered, all keys must be distinct, values may be repeated, uses hashing internally 
d={110:"abc", 101:"xyz", 105:"pqr"} 
print("Dictionary d : ", d )
d={}
d["laptop"]=40000 
d["mobile"]=15000 
d["earphone"]=1000 
print("After inserting laptop, mobile, earphones : ",d)
print(d["mobile"])  

print("GET FUNCTION IN DICTIONARY :") 
d1={110:"abc", 101:"xyz", 105:"pqr"} 
print(d1.get(101))
print(d1.get(125))
print(d1.get(125,"NA")) 
if 125 in d1 :
    print(d1[125]) 
else :
    print("NA") 

print("REMOVING AN ITEM FROM DICTIONARY : ") 
d2={110:"abc", 101:"xyz", 105:"pqr", 106:"bcd"} 
d2[101]="wxy" 
print("Length of dictionary after adding 101:wxy - ",len(d))
print(d2) 
print(d2.pop(105)) 
print("After popping 105 : ",d2) 
del d2[106] 
print("Removing 106 using del function : ",d2) 
d2[108]="cde" 
print(d2.popitem()) 


# Count distinct elements in a list  
# Approach 1 : Naive 
l1=[10,20,10,30,30,20] 
def distict1(l) :
    res=1 
    for i in range(1,len(l)) :
        if l[i] not in l[:i] :
            res+=1 
    return res 
print("Distinct elements in list by Naive Approach : ", distict1(l1))

# Approach 2 : (Using set) 
def distinct2(l) :
    s=set(l) 
    return len(s) 
print("Distinct elements in list using sets : ", distinct2(l1))