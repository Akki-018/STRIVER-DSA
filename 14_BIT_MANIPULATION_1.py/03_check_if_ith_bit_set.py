## TO CHECK IF THE ith bit of a binary number is set or not 
# Set - 1, not set - 0 

def check(n,i):
    if n&(1<<i):
        return True 
    else:
        return False
print(check(13,1))