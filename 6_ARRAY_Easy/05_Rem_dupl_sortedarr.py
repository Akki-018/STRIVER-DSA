## REMOVE DUPLICATES FROM SORTED ARRAY
def Remove_duplicate_sortarr(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i] = arr[j]
    return arr[:i+1]
arr = [1,1,2,2,3]
print(Remove_duplicate_sortarr(arr))