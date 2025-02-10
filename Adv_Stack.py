## Advanced Stack 
#   Implement two stacks in an array 
#   Implement K stacks in an array 
#   Stock Span Problem 
#   Previous Greater Element 
#   Next Greater Element 
#   Largest Area in Histogram 
#   Largest Rectangle with all 1's 
#   Stack with getMin() in O(1) 
#   Infix, Prefix and Postfix 
#   Infix to Postfix 
#   Evaluation of Postfix 
#   Infix to Prefix 
#   Evaluation of Prefix 



## Implement two stacks in an array 
class TwoStacks : 
    def __init__(self, n) :  
        self.size=n 
        self.arr=[None]*n 
        self.top1=-1 
        self.top2=self.size 
    
    def push1(self, x) : 
        if self.top1<self.top2-1 : 
            self.top1+=1 
            self.arr[self.top1]=x
            return self.arr 
        return False 
    
    def push2(self, x) : 
        if self.top1<self.top2-1 : 
            self.top2-=1 
            self.arr[self.top2]=x 
            return self.arr
        return False 
    
    def pop1(self) : 
        if self.top1>=0 : 
            x=self.arr[self.top1] 
            self.arr[self.top1]=None 
            self.top1-=1 
            return x 
        return None 
    
    def pop2(self) : 
        if self.top2<self.size : 
            x=self.arr[self.top2]
            self.arr[self.top2]=None  
            self.top2-=1 
            return x 
        return None 
    
    def size1(self) : 
        return self.top1+1 
    
    def size2(self) :  
        return self.size-self.top2 

print("Two stacks in an array : ")
ts=TwoStacks(5) 
print(ts.push1(10))
print(ts.push1(20))
print(ts.push2(70))
print(ts.push2(60))
print(ts.pop1()) 
print(ts.pop2()) 
print("\n") 



## Implement K stacks in an array   
class KStacks : 
    def __init__(self, n, k) : 
        self.cap=n 
        self.k=k 
        self.arr=[None]*n 
        self.top=[-1]*k 
        self.next=[i+1 for i in range(n)] 
        self.next[n-1]=-1 
        self.free_top=0 
    
    def push(self, sn, x) : 
        i=self.free_top 
        self.free_top=self.next[self.free_top] 
        self.arr[i]=x 
        self.next[i]=self.top[sn] 
        self.top[sn]=i 
    
    def pop(self, sn) : 
        prev_top=self.top[sn] 
        self.top[sn]=self.next[prev_top] 
        self.next[prev_top]=self.free_top 
        self.free_top=prev_top 
        return self.arr[prev_top] 
    
    def isEmpty(self, sn) : 
        return self.top[sn]==-1 



## Stock Span Problem 
# Naive approach 
def stockSpan1(arr) : 
    n=len(arr) 
    for i in range(n) :
        span=1 
        j=i-1 
        while j>=0 and arr[i]>=arr[j] : 
            span+=1 
            j-=1 
        print(span, end=" ")
print("Stock Span Problem: Naive") 
arr=[13, 15, 12, 14, 16, 8, 6, 4, 10, 30] 
stockSpan1(arr)
print("\n") 

# Efficient approach 
def stockSpan2(arr) : 
    n=len(arr)
    st=[] 
    st.append(0) 
    print(1, end=" ") 
    for i in range(1, n) : 
        while len(st)>0 and arr[st[-1]]<=arr[i] : 
            st.pop() 
        if len(st)==0 : 
            span=(i+1) 
        else : 
            span=i-st[-1] 
        print(span, end=" ") 
        st.append(i) 
print("Stock Span Problem: Efficient")
stockSpan2(arr)
print("\n") 


## Previous greater element 
# Naive solution 
def prevGreat1(arr) : 
    n=len(arr)
    for i in range(n) : 
        pg=-1 
        for j in range(i-1, -1, -1) : 
            if arr[j]>arr[i] : 
                pg=arr[j] 
                break 
        print(pg, end=" ") 
print("Previous greater element: Naive")
arr=[15, 10, 18, 12, 4, 6, 2, 8] 
prevGreat1(arr)
print("\n") 

# Efficient solution
def prevGreat2(arr) : 
    n=len(arr) 
    st=[]  
    for i in range(n) : 
        while len(st)>0 and st[-1]<=arr[i] : 
            st.pop() 
        if len(st)==0 : 
            ans=-1
        else : 
            ans=st[-1] 
        print(ans, end=" ")
        st.append(arr[i])
print("Previous greater element: Efficient")
prevGreat2(arr) 
print("\n")


## Next greater element 
# Naive solution 
def nextGreater1(arr) : 
    n=len(arr) 
    for i in range(n) : 
        ng=-1 
        for j in range(i+1, n) : 
            if arr[j]>arr[i] : 
                ng=arr[j] 
                break 
        print(ng, end=" ") 
print("Next greater element: Naive") 
arr=[5, 15, 10, 8, 6, 12, 7] 
nextGreater1(arr)
print("\n")


def nextGreater2(arr) : 
    n=len(arr) 
    st=[] 
    ans=[None]*n
    for i in reversed(range(n)) : 
        while len(st)>0 and st[-1]<=arr[i] : 
            st.pop() 
        if len(st)==0 : 
            ans[i]=-1 
        else : 
            ans[i]=st[-1] 
        st.append(arr[i]) 
    for x in ans : 
        print(x, end=" ") 
print("Next greater element: Efficient") 
arr=[5, 15, 10, 8, 6, 12, 7]
nextGreater2(arr)
print("\n")