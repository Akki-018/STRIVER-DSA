## A bit is the smallest unit of data that a computer can store - can have only two possible values - 0 or 1 
# Computers uses binary only because it is built of electronic ckts(transistors) and it has only two stable states i.e Off - 0 or ON -1 
# DECIMAL NUMBER SYSTEM - Base 10 - 0 1 2 3 4 5 6 7 8 9 
# BINARY NUMBER SYSTEM - Base 2 - 0 1 
# BINARY TO DECIMAL 
def binary2decimal(s):
    
    ans = 0
    for i in s:
        ans = ans*2 + int(i)
    return ans
print(binary2decimal("1101"))

# DECIMAL TO BINARY 
def decimal2binary(n):
    ans = ""
    while n!=0 :
        ans+=str(n%2)
        n = n//2
    return ans[::-1]
print(decimal2binary(13))

