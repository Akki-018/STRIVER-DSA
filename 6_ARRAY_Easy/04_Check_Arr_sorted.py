## CHECK IF ARRAy IS SORTED 
def Array_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
arr = [1,3,5,0]
print(Array_sorted(arr))