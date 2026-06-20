## MOVE ZEROES TO END 

# BRUTE FORCE 
def Move_zeroes_brute(arr):
    new_arr = []
    for num in arr:
        if num != 0:
            new_arr.append(num)
    for num in arr:
        if num == 0:
            new_arr.append(num)
    return new_arr
arr = [1,0,2,3,2,0,0,4,5,1]
print(Move_zeroes_brute(arr))

# Optimal Code
def Move_zeroes_optimal(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    return arr
arr = [1,0,2,3,2,0,0,4,5,1]
print(Move_zeroes_optimal(arr))



