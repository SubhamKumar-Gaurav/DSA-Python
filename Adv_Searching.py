## Advanced searching 
#    Search in an Infinite sized array 
#    


## Search in an Infinite sized array  
## 1. Naive Approach 
def searchInfy(arr,x) :
    i=0 
    while True : 
        if arr[i]==x : 
            return i 
        elif arr[i]>x : 
            return -1 
        i+=1 
