## Find number that appears once - ( Leetcode q 136 Single number )
def Single_Number(arr):
    n = len(arr)
    xor = 0
    for i in range(n):
        xor = xor^arr[i]
    return xor 
arr = [1,4,2,3,1,4,2]
print(Single_Number(arr))

## Longest subarrays with given sum k (positives) - ( Leetcode q 325(locked))
#Brute force
def Lonest_Subarray_k(arr,k):
    n = len(arr)
    max_size=0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j]
            if sum == k:
                max_size = max(max_size,j-i+1)
    return max_size
arr = [1,2,3,1,1,1]
print(Lonest_Subarray_k(arr,3))

#Optimal code 
''' 
sdfsf
'''

## Subarray Sum equals k - Leetcode 560 - to return the total number of subarrays !!!
