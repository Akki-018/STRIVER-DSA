## SORT AN ARRAY OF 0s,1s and 2s (LEETCODE 75)
#  Brute Force - Merge Sort

#Better Code 
def sortColors(nums):
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0
    for i in nums:
        if i == 0:
            cnt_0 +=1
        elif i == 1:
            cnt_1 +=1
        elif i == 2:
            cnt_2 +=1
    for j in range(cnt_0):
        nums[j] = 0 
    for k in range(cnt_0,cnt_0+cnt_1):
        nums[k] = 1
    for l in range(cnt_0+cnt_1,len(nums)):
        nums[l] = 2
    return nums

#* OPTIMAL CODE 
# DUCTH NATIONAL FLAG SORTING ALGO
def sort_colors_DNF(nums):
    low = 0
    mid = 0
    high = len(nums)-1
    while mid<=high:
        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low],nums[mid]
            low+=1
            mid+=1

        elif nums[mid] == 1:
            mid+=1
        elif nums[mid] == 2:
            nums[mid] ,nums[high] = nums[high],nums[mid]
            high-=1
            
    return nums

arr = [0,1,2,0,1,2,1,2,0,0,0,1]
print(sort_colors_DNF(arr))

