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
print("Heap implementation")  
## Main operations 
#    Constructor (simple)
#    Insert 
#    Extract min 
#    Decrease key
#    Delete 
#    Constructor (enhanced with build heap) 

## Utility Functions 
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