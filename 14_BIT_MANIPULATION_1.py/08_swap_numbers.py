## TO SWAP TO NUMBERS -- like if a = 5, b = 9 so return a = 9 , b = 5 ... using bit manipulation 
# BIT MANIPULATION METHOD 
def swap_num(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b
print(swap_num(5,9))

# ARITHMETIC METHOD 
def swap_num(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b
print(swap_num(5,9))