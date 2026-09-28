## RETURN THE POWERSET of an array - i.e all the possible subsets
def subsets(nums):
    ans = []
    def generate(i,arr):
        if i==len(nums):
            ans.append(arr.copy())
            return 
        arr.append(nums[i])
        generate(i+1,arr)
        arr.pop()
        generate(i+1,arr)
    generate(0,[])
    return ans 
nums = [1,2,3]
print(subsets(nums))

