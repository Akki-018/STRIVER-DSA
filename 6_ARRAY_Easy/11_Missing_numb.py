## MISSING NUMBER
# BRUTE FORCE 
def Missing_num_Brute(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i
    return -1
arr = [0,2,1]
print(Missing_num_Brute(arr))

# OPTIMAL CODE( MATHS CODE )
def Missing_num_Optimal(arr):
    n = len(arr)
    total_sum = int(((n)*(n+1))/2)
    actual_arr_sum  = sum(arr)
    return total_sum-actual_arr_sum
arr = [3,1,0,4]
print(Missing_num_Optimal(arr))


# XOR APPROACH(clever Solution) 
def Missing_num_xor(arr):
    xor = 0
    for i in range(len(arr)+1):
        xor = xor^i
        if i<len(arr):
            xor = xor^arr[i]
    return xor 
arr = [1,0,3]
print(Missing_num_xor(arr))
