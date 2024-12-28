## Bit Magic 
#   Bitwise operators 
#   Binary representation of negative number 
#   Check Kth bit is set or not 
#   Count set bits 
#   Find the only odd 
#   Power of 2
#   One Odd occuring 
#   Two odd occuring
#   Power set using Bitwise 



## Bitwise operators  
print("binary of 18 : ", bin(18)) 
print("binary of 12 : ", bin(12)) 
print("decimal of 0b10010 : ", int("0b10010",2)) 
print("decimal of 0b1100 : ", int("0b1100",2))   

x=3 
y=6 
print("bitwise AND (&) of 3 and 6 : ", x&y)
print("bitwise OR (|) of 3 and 6 : ", 3|6) 
print("bitwise XOR (^) of 3 and 6 : ", 3^6) 
print("\n") 

x=5 
print("Left shift operator ") 
print(x<<1)  # Multiplying with 2^1 
print(x<<2)  # Multiplying with 2^2 
print(x<<3)  # Multiplying with 2^3  
print("\n") 

x=50 
print("Right shift operator ") 
print(x>>1)  # Floor division with 2^1  
print(x>>2)  # Floor division with 2^2  
print(x>>3)  # Floor division with 2^3  
print("\n") 

x=5 
print("Negation of 5 : ", ~x)
print("\n")    



## Check Kth bit is set or not   
# Method - 1 (Left shift)
def isKthBitSetLeft(n,k) : 
    if n & (1<<(k-1)) : 
        return "Yes" 
    else : 
        return "No" 
print("n=5, k=3 : ", isKthBitSetLeft(5,3)) 

# Method - 2 (Right Shift) 
def isKthBitSetRight(n,k) : 
    if (n>>(k-1)) & 1 : 
        return "Yes" 
    else : 
        return "No"
print("n=5, k=1 : ", isKthBitSetRight(5,1)) 
print("n=5, k=2 : ", isKthBitSetRight(5,2)) 
print("\n") 


## Count set bits (3 approaches)
# Naive solution 
print("Count set bits - Naive solution")
def countSetBits01(n) : 
    res=0 
    while n :
        if n%2==1 : 
            res+=1 
        n=n//2 
    return res 
print("Set bits in 5 : ",countSetBits01(5))
print("Set bits in 13 : ",countSetBits01(13))

def countSetBits02(n) : 
    res=0 
    while n :
        res = res + (n&1)
        n=n//2 
    return res 
print("Count Set bits in 5 : ",countSetBits02(5))
print("Count Set bits in 13 : ",countSetBits02(13)) 
print("\n")   


## Approach - 2  Brian Kernigam's Algorithm 
print("Brian Kernigam's Algorithm")
def countSetBits2(n) : 
    res=0 
    while n : 
        n = n & (n-1)
        res+=1 
    return res 
print("Count set bits 40 : ", countSetBits2(40))
print("\n") 

## Approach - 3  Lookup Table 
def countSetBits3(n) : 
    tbl=[0]*256 
    for i in range(256) : 
        tbl[i]=(i&1) + tbl[i//2] 
    return tbl[n&0xff] + tbl[(n>>8)&0xff] + tbl[(n>>16)&0xff] + tbl[(n>>24)&0xff] 

print("Count set bits in 15 : ",countSetBits3(15))
print("Count set bits in 5 : ",countSetBits3(5)) 
print("\n") 