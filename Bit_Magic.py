## Bit Magic 
#   Bitwise operators 
#   Binary representation of negative number 
#   Check Kth bit is set or not 
#   Count set bits 
#   Find the only odd 
#   Power of 2
#   One Odd occuring 
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
print(x<<10)  # Multiplying with 2^10  