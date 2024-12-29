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


## Find the only odd  times occuring number 
# Method - 1 Using count 
print("Find the only odd using count") 
def findOdd1(l) : 
    res=None 
    for x in l : 
        count=l.count(x) 
        if count%2==1 : 
            res=x
            return res  
    return res 
l=[10,20,20,30,10]
print("[10,20,20,30,10] : ", findOdd1(l)) 


# Method - 2 Using XOR 
print("Find only odd using bitwise XOR") 
def findOdd2(l) : 
    res=0 
    for x  in l : 
        res = res^x 
    return res 
l=[10,20,20,30,10,30,10]
print("[10,20,20,30,10,30,10] : ", findOdd2(l)) 
print("\n") 


## Power of 2
# Naive approach  
def isPow2(n) : 
    if n==0 : 
        return False 
    while n!=1 : 
        if n%2!=0 : 
            return False 
        n=n//2 
    return True 
print("Power of 2 check for n=4 : ", isPow2(4))
print("Power of 2 check for n=6 : ", isPow2(6))

# Efficient approach 
def isPower2(n) : 
    if n==0 : 
        return False
    return (n&(n-1))==0 
print("Power of 2 check for n=16 : ", isPower2(16))
print("Power of 2 check for n=18 : ", isPower2(18)) 
print("\n") 


## One odd occuring  (Same as find only odd) 

## Two odd occuring 
# Naive approach 
print("Two odd occuring (Naive)")
def twoOddOccuring1(l) : 
    for i in l : 
        count=0 
        for j in l : 
            if i==j : 
                count+=1 
        if count%2==1 : 
            print(i, end=" ")
l=[3,4,3,4,5,4,4,6,7,7] 
print("[3,4,3,4,5,4,4,6,7,7] : ", end= " ")
twoOddOccuring1(l)   
print("\n")

# Efficient approach 
print("Two odd occuring (Efficient)")
def twoOddOccuring2(l) : 
    xors=0 
    res1=0 
    res2=0 
    for i in l : 
        xors=xors^i 
    sn = xors & ~(xors-1) 
    for i in l : 
        if i & sn != 0 : 
            res1 = res1 ^ i 
        else : 
            res2 = res2 ^ i 
    print(res1, res2)  
l=[3,4,3,4,5,4,4,6,7,7,6,7] 
print("[3,4,3,4,5,4,4,6,7,7,6,7]  : ", end=" ")
twoOddOccuring2(l) 
print("\n") 

## Power set using Bitwise 
def powSet(s) : 
    n=len(s)
    pSize = 1<<n 
    for i in range(pSize) : 
        for j in range(n) : 
            if i&(1<<j)!=0 : 
                print(s[j], end="") 
        print()
s="abc" 
print("Power set of 'abc' : ", end=" ")
powSet(s)