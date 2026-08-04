## RETURN ALL the possible Subsets (power set)
def subsets(nums):
    n = len(nums)
    ans = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i&(1<<j):
                subset.append(nums[j])
        ans.append(subset)
    return ans 
nums = [1,2,3]
print(subsets(nums))
