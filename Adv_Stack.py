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



## Largest Area in Histogram 
# Naive approach 
def areaHist(arr) : 
    n=len(arr)
    res=0 
    for i in range(n) : 
        curr=arr[i] 
        for j in range(i-1, -1, -1) : 
            if arr[j]>=arr[i] : 
                curr+=arr[i] 
            else : 
                break
        for j in range(i+1,n) : 
            if arr[j]>=arr[i] : 
                curr+=arr[i] 
            else : 
                break 
        res=max(res, curr) 
    return res 
print("Largest area in Histogram: Naive")
arr=[6,2,5,4,1,5,6] 
print(areaHist(arr))
print("\n") 

# Efficient approach 
def getMaxArea(arr) : 
    n=len(arr)
    st=[] 
    res=0 
    for i in range(n) : 
        while st and arr[st[-1]]>=arr[i] : 
            tp=st[-1] 
            st.pop() 
            if st :
                curr_width=(i-st[-1]-1) 
            else : 
                curr_width=i 
            res=max(res, curr_width*arr[tp]) 
        st.append(i) 
    while st : 
        tp=st[-1] 
        st.pop() 
        if st :
            curr_width=(n-st[-1]-1) 
        else : 
            curr_width=n 
        res=max(res, curr_width*arr[tp]) 
    return res 
print("Largest area in Histogram: Efficient")
arr=[60,20,50,40,10,50,60] 
print(getMaxArea(arr)) 
print("\n") 


##  Largest Rectangle with all 1's   
def maxRectangle(mat) : 
    rows=len(mat) 
    cols=len(mat[0]) 
    res=getMaxArea(mat[0]) 
    for r in range(1,rows) : 
        for c in range(cols) :  
            if mat[r][c] :
                mat[r][c]+=mat[r-1][c] 
        res=max(res, getMaxArea(mat[r]))
    return res 
print("Largest Rectangle with all 1's ")
mat=[[0,1,1], [1,1,1], [0,1,1]] 
print(maxRectangle(mat)) 
print("\n") 



## Stack with getMin() in O(1) 
# Method 1 : All elements are positive
class Stack1 : 
    def __init__(self) : 
        self.s=[] 
        self.min_val=None 

    def push(self, x) :  
        if not self.s : 
            self.min_val=x 
            self.s.append(x) 
        elif x<=self.min_val : 
            self.s.append(x-self.min_val)
            self.min_val=x 
        else : 
            self.s.append(x) 

    def getMin(self) : 
        if self.s : 
            return self.min_val 
        else : 
            return None 

    def peek(self) : 
        if not self.s : 
            return None 
        t=self.s[-1] 
        if t<=0 : 
            return self.min_val 
        else : 
            return t 

    def pop(self) : 
        if not self.s : 
            return None 
        t=self.s.pop() 
        if t<=0 : 
            res=self.min_val 
            self.min_val=self.min_val-t 
            return res 
        else : 
            return t 
print("Stack 1 : handles only positive") 
s=Stack1() 
s.push(5) 
s.push(10) 
s.push(20) 
s.push(2) 
s.push(6) 
s.push(4)     # [5, 10, 20, 2, 6, 4]
print("Get min : ",s.getMin()) 
s.pop()       # [5, 10, 20, 2, 6]
s.pop()       # [5, 10, 20, 2]
s.pop()       # [5, 10, 20]
print("Get min : ",s.getMin()) 
s.push(1)     # [5, 10, 20, 1]
s.push(2)     # [5, 10, 20, 1, 2]
print("Get min : ",s.getMin()) 
s.pop()       # [5, 10, 20, 1]
print("Get min : ",s.getMin()) 
s.pop()       # [5, 10, 20]
print("Get min : ",s.getMin())

# Method - 2 : Handles negative elements as well 
class Stack2 :
    def __init__(self) : 
        self.s=[] 
        self.min_val=None 

    def push(self, x) :  
        if not self.s : 
            self.min_val=x 
            self.s.append(x) 
        elif x<=self.min_val : 
            self.s.append(2*x-self.min_val)
            self.min_val=x 
        else : 
            self.s.append(x) 

    def getMin(self) : 
        if self.s : 
            return self.min_val 
        else : 
            return None 

    def peek(self) : 
        if not self.s : 
            return None 
        t=self.s[-1] 
        if t<=self.min_val : 
            return self.min_val 
        else : 
            return t 

    def pop(self) : 
        if not self.s : 
            return None 
        t=self.s.pop() 
        if t<=self.min_val : 
            res=self.min_val 
            self.min_val=2*self.min_val-t 
            return res 
        else : 
            return t  
print("Stack 2 : Handles negatives as well")
st=Stack2() 
st.push(5)
st.push(2)
st.push(6)
print("Get min: ", st.getMin())
st.push(-10)
st.push(4)
st.pop() 
print("Get min: ", st.getMin())
st.pop() 
st.push(-20)
print("Get min: ", st.getMin())
st.pop()
st.push(2)  
st.push(1)
print("Get min: ", st.getMin())
print("\n")



## Infix to Postfix conversion 
class Conversion1 : 
    def __init__(self, capacity) :
        self.top=-1 
        self.capacity=capacity 
        self.array=[] 
        self.output=[] 
        self.precedence={"+": 1 , "-": 1, "*": 2, "/": 2, "^": 3} 
    
    def isEmpty(self) :  
        return self.top==-1 
    
    def peek(self) : 
        return self.array[-1] if not self.isEmpty() else None 
    
    def pop(self) : 
        if not self.isEmpty() : 
            self.top-=1 
            return self.array.pop() 
        else : 
            return "None" 
    
    def push(self, op) : 
        self.top+=1 
        self.array.append(op) 
    
    def isOperand(self, ch) : 
        return ch.isalnum() 
    
    def notGreater(self, i) : 
        if self.isEmpty() : 
            return False 
        else : 
            self.precedence.get(i,0) <= self.precedence.get(self.peek(), 0)
    
    def infixToPostfix(self, exp) : 
        for i in exp : 
            if self.isOperand(i) : 
                self.output.append(i) 
            elif i=="(" : 
                self.push(i) 
            elif i==")" : 
                while not self.isEmpty() and self.peek()!="(" :     
                    self.output.append(self.pop()) 
                if not self.isEmpty() and self.peek()=="(" : 
                    self.pop() 
            else : 
                while not self.isEmpty() and self.notGreater(i) : 
                    self.output.append(self.pop()) 
                self.push(i) 
        while not self.isEmpty() : 
            self.output.append(self.pop()) 
        return "".join(self.output) 

print("Infix to Postfix Conversion: ") 
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion1(len(exp))
print(obj.infixToPostfix(exp))

exp = "(a+b)*(c+d)"
obj = Conversion1(len(exp))
print(obj.infixToPostfix(exp))

exp = "a+b*c"
obj = Conversion1(len(exp))
print(obj.infixToPostfix(exp))
print("\n") 


## Evaluation of Postfix 
class Evaluate1 : 
    def __init__(self, capacity) : 
        self.top=-1 
        self.capacity=capacity 
        self.array=[] 
    
    def isEmpty(self) : 
        return self.top==-1
    
    def peek(self) : 
        return self.array[-1] 
    
    def pop(self) : 
        if not self.isEmpty() : 
            self.top-=1 
            return self.array.pop() 
        else : 
            return "None" 
    
    def push(self, op) : 
        self.top+=1 
        self.array.append(op) 
    
    def evaluatePostfix(self, exp) : 
        for i in exp : 
            if i.isdigit() : 
                self.push(i) 
            else : 
                val1=self.pop() 
                val2=self.pop() 
                self.push(str(eval(val2+i+val1))) 
        return int(self.pop()) 

print("Evaluation of Postfix :") 
exp="231*+9-"
obj=Evaluate1(len(exp)) 
print(obj.evaluatePostfix(exp)) 

exp=['10', '2', '*', '3', '+']
obj=Evaluate1(len(exp)) 
print(obj.evaluatePostfix(exp)) 
print("\n") 



## Infix to Prefix (Efficient solution)
print("Infix to Prefix: Efficient solution") 
def isOperator(c):
	return not c.isalnum() 

def getPriority(C):
	if (C == '-' or C == '+'):
		return 1
	elif (C == '*' or C == '/'):
		return 2
	elif (C == '^'):
		return 3
	return 0

def infixToPrefix(infix):
	operators = []
	operands = []
	for i in range(len(infix)):
		if (infix[i] == '('):
			operators.append(infix[i])
		elif (infix[i] == ')'):
			while (len(operators)!=0 and operators[-1] != '('):
				op1 = operands.pop()
				op2 = operands.pop()
				op = operators.pop()				
				tmp = op + op2 + op1
				operands.append(tmp)
			operators.pop()
		elif (not isOperator(infix[i])):
			operands.append(infix[i] + "")
		else:
			while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
				op1 = operands.pop()
				op2 = operands.pop()
				op =  operators.pop()
				tmp = op + op2 + op1
				operands.append(tmp)
			operators.append(infix[i])

	while (len(operators)!=0):
		op1 = operands.pop()		
		op2 = operands.pop()		
		op = operators.pop()		
		tmp = op + op2 + op1
		operands.append(tmp)
	return operands[-1]

s = "(A-B/C)*(A/K-L)"
print( infixToPrefix(s))
  
s = "x+y*z/w+u"
print( infixToPrefix(s))
print("\n")


## Evaluation of Prefix 
def is_operand(c):
	return c.isdigit()

def evaluate(expression):
	stack = []
	for c in expression[::-1]:
		if is_operand(c):
			stack.append(int(c))
		else:
			o1 = stack.pop()
			o2 = stack.pop()
			if c == '+':
				stack.append(o1 + o2)
			elif c == '-':
				stack.append(o1 - o2)
			elif c == '*':
				stack.append(o1 * o2)
			elif c == '/':
				stack.append(o1 / o2)
	return stack.pop()
print("Evaluation of Prefix: ") 
test_expression =["+", "9", "*", "2", "6"] 
print(evaluate(test_expression)) 
