## ARMSTRONG NUMBER -- a number which is equal to the sum of the elements raised to the cnt of the number of digits
def isArmstrong(n):
    dup = n
    cnt = len(str(n))
    temp = n
    arm_n = 0
    while temp>0:
        digit = temp%10
        arm_n += digit**cnt
        temp  = temp//10
    
    return arm_n == dup
n = 153 
print(isArmstrong(n))