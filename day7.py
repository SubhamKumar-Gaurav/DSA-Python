# Day - 7 
# Hashing  
#    Chaining 
#    Open Addressing 
#    Frequency of array elements - Naive approach , Dictionary approach 
#    Implementation of Open addressing 
#    Set in Python 

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

# Set operations : 
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