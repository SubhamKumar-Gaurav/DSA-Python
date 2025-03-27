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
print("\n")



