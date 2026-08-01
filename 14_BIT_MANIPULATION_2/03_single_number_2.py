## Single number-2 but every element is three times 
def single_num_2(nums):
    ans = 0 
    for i in range(32):
        cnt = 0 
        for num in nums:
            if (num&(1<<i)):
                cnt+=1
        if cnt%3!=0:
            ans |= (1<<i)
    return ans 
nums = [2,2,2,1]
print(single_num_2(nums))