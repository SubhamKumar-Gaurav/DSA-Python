# Greedy 
#   Activity selection 
#   Fractional Knapsack 
#   Job sequencing 
#   Huffman Coding 
#   Huffman Algorithms 


## Minimum coins 
def minCoins(coins, amount) : 
    coins.sort(reverse=True) 
    res=0 
    for x in coins : 
        if x<=amount : 
            c=amount//x 
            res+=c 
            amount-=(c*x) 
        if amount==0 : 
            break 
    return res 
coins=[1,2,5,10]
amount=52
print("Minimum coins : ", minCoins(coins, amount))
print()



## Activity Selection Problem 
def activitySelection(arr) : 
    n=len(arr)
    arr.sort(key= lambda x: x[1])  
    prev=0 
    res=1 
    for curr in range(1,n) : 
        if arr[curr][0]>=arr[prev][1] :  
            res+=1 
            prev=curr 
    return res 
arr=[[1,3], [2,4], [3,8], [10,11]]
print("Activity selection problem : ",activitySelection(arr))
print()



## Fractional Knapsack Problem 
# weight,value
arr=[[50,600], [20,500], [30,400]] 
def fractionalKnapsack(arr, capacity) :  
    for i in range(len(arr)) :
        u=arr[i][0]   # weight
        v=arr[i][1]   # value 
        arr[i].append(v/u) 
    arr.sort(reverse=True, key= lambda x:x[2]) 
    res=0
    for curr in arr : 
        if curr[0]<=capacity :   # curr weight <= knapsack capacity
            res+=curr[1]         # adding value to the answer 
            capacity-=curr[0]    # reducing the knapsack capacity, since we have filled it with curr weight
        else : 
            res+=curr[1]*(capacity/curr[0])  # the remaining quantity: adding only a portion of the weight and not complete 
            return res 
print("Fractional Knapsack : ",fractionalKnapsack(arr, 70))
print()



## Job Scheduling
def jobScheduling(arr,t) : 
    n=len(arr)
    arr.sort(key= lambda x:x[1], reverse=True)
    result=[False]*t 
    res=0 
    for i in range(n) : 
        for j in range(min(t-1, arr[i][0]-1), -1, -1) : 
            if result[j]==False : 
                result[j]=True 
                res+=arr[i][1] 
                break 
    return res 
arr=[[4,70], [1,80], [1,30], [1,100]]
t=4 
print("Job Scheduling : ",jobScheduling(arr,t))
print()



## Huffman Coding 
import heapq

class node:
	def __init__(self, freq, symbol, left=None, right=None):
		self.freq = freq
		self.symbol = symbol
		self.left = left
		self.right = right
		self.huff = ''

	def __lt__(self, nxt):
		return self.freq < nxt.freq		

def printNodes(node, val=''):
	newVal = val + str(node.huff)
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [ 5, 9, 12, 13, 16, 45]
nodes = []

for x in range(len(chars)):
	heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:	
	left = heapq.heappop(nodes)
	right = heapq.heappop(nodes)
	left.huff = 0
	right.huff = 1
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
	heapq.heappush(nodes, newNode)

print("Huffman Coding : ")
printNodes(nodes[0])
print() 
