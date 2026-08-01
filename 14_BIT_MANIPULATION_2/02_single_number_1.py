## SINGLE NUMBER - Return the single number in the array 
def single_num_1(num):
    xor = 0
    for i in num:
        xor^=i
    return xor 
num = [2,2,1]
print(single_num_1(num))