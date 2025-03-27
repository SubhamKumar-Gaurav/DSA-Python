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



