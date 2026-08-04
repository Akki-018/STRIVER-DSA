## SINGLE NUMBER 3 - multiple single number 
def single_num_3(nums):
    xor = 0 
    for i in nums:
        xor^=i
    right_most_set_bit = xor&(-xor)
    num1 = 0 
    num2 = 0 
    for num in nums:
        if num&right_most_set_bit:
            num1^=num
        else:
            num2^=num
    return [num1,num2]
nums = [2,3,1,3,5,2]
print(single_num_3(nums))
