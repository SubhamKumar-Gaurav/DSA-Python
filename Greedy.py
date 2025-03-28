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