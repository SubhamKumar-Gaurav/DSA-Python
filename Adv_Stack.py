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
