## RETURN ALL THE SUBSETS -- UNIQUE elements
def subsets(nums):
    ans = []
    def recurse(i,sub):
        if i==len(nums):
            ans.append(sub.copy())
            return
        sub.append(nums[i])
        recurse(i+1,sub)
        sub.pop()
        recurse(i+1,sub)
    recurse(0,[])
    return ans 
nums = [1,2,3]
print(subsets(nums))
