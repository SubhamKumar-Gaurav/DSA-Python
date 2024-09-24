# Day - 7 
# Hashing  
#    Chaining 
#    Open Addressing 
#    Frequency of array elements - 

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
print("Frequencies of an array by Naive approach")
freq1(arr)