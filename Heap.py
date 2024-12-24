## Heap 
#    Introduction  
#    Heap Implementation  
#    Binary Heap Insert
#    Binary Heap (Extract min and Heapify) 
#    Decrease Key and Delete operations 
#    Build Heap 
#    Heap sort 
#    Heapq in Python 




## Introduction  
#    Used in Heap Sort 
#    Used to implement Priority Queue 
#    Two types  (Min Heap and Max Heap) 

#   Binary Heap is a complete Binary tree (Stored as an array)   


## Heap implementation 
## Main operations 
#    Constructor (simple)
#    Insert 
#    Extract min 
#    Decrease key
#    Delete 
#    Constructor (enhanced with build heap) 

##  Utility Functions 
#    Left child 
#    Right child 
#    Parent 
#    Min Heapify  


## Binary Heap insert 
class myMinHeap : 
    def __init__(self):
        self.arr=[] 
    def inert(self,x) : 
        arr=self.arr 
        arr.append(x) 
        i=len(arr)-1 
        while i>0 and arr[self.parent(i)]>arr[i] : 
            p=self.parent(i) 
            arr[i], arr[p]= arr[p], arr[i] 
            i=p 
#  .......... 


## Binary Heap (Extract min and Heapify) 
# minHeapify 
def minHeapify(self, i) : 
    arr=self.arr 
    lt=self.lchild(i) 
    rt=self.rchild(i)  
    smallest=i 
    n=len(arr) 
    if lt<n and arr[lt]<arr[smallest] : 
        smallest=lt 
    if rt<n and arr[rt]<arr[smallest] : 
        smallest=rt 
    if smallest!=i : 
        arr[smallest], arr[i] = arr[i], arr[smallest] 
        self.minHeapify(smallest) 

import math
# Extract min 
def extractMin(self) : 
    arr=self.arr 
    n=len(arr) 
    if n==0 : 
        return math.inf 
    res=arr[0] 
    arr[0]=arr[n-1] 
    self.minHeapify(0)
    return res 


## Decrease Key and Delete operations   
#  Decrease Key 
def decreaseKey(self, i, x) : 
    arr=self.arr
    arr[i]=x 
    while i!=0 and arr[self.parent(i)>arr(i)] : 
        p=self.parent(i) 
        arr[i], arr[p] = arr[p], arr[i] 
        i=p 


# Delete 
def deleteKey(self, i) : 
    n=len(self.arr) 
    if i>=n : 
        return 
    else : 
        self.decreaseKey(i, -math.inf) 
        self.extractMin() 


## Build Heap 
class myMinHeap : 
    def __init__(self, l=[]):
        self.arr=l 
        i=(len(l)-2)//2 
        while i>=0 : 
            self.minHeapify(i) 
            i=i-1  


##  Heap Sort 
def buildHeap(arr) : 
    n=len(arr) 
    for i in range((n-2)//2, -1, -1) : 
        maxHeapify(arr, n, i) 

def maxHeapify(arr, n, i) : 
    largest=i 
    left = 2*i + 1
    right = 2*i + 2 
    if left<n and arr[left]>arr[largest] : 
        largest = i 
    if right<n and arr[right]>arr[largest] : 
        largest = i  
    if largest!=i : 
        arr[i], arr[largest] = arr[largest], arr[i] 
        maxHeapify(arr, n , largest) 

def heapSort(arr) : 
    n=len(arr) 
    buildHeap(arr) 
    for i in range(n-1,0,-1) : 
        arr[i], arr[0] = arr[0], arr[i] 
        maxHeapify(arr, i, 0)