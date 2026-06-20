## LARGEST ELEMENT IN ARRAY
def Largest_ele(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i]>=max:
            max = arr[i]
    return max
arr = [5,3,6,7,12,1]
print(Largest_ele(arr))
