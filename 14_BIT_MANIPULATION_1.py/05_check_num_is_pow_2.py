## TO CHECK IF THE NUMBER IS A POWER OF 2 or not 
# BIT MANIPULTATION APPROACH
def check_power_2(n):
    if n==0:
        return 0
    return n&(n-1)==0
print(check_power_2(18))