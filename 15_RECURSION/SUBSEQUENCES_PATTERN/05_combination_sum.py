## TO return the elements which sum to the target ... and also every element can be repeated unlimited number of times
def combination_sum(nums,target):
    ans = []
    def recursion(i,target,arr): 
        if i==len(nums):
            if target==0:
                ans.append(arr.copy())    ## Imp as we need are pop out the last element so we append a copy of the array
            return
        if nums[i]<=target:
            arr.append(nums[i])
            recursion(i,target-nums[i],arr)
            arr.pop()                     #Why pop? for backtracking - to undo the last choice made to a mutable list for all possiblities
        recursion(i+1,target,arr)
    recursion(0,target,[])
    return ans 
nums = [2,3,6,7]
print(combination_sum(nums,7))