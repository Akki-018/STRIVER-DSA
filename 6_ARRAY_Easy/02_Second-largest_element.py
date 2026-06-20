## SECOND LARGEST ELEMENT IN ARRAY 
def Second_largest(arr):
    if len(arr)<2:
        return -1
    largest = arr[0] 
    second_large = -float('inf')
    
    for i in range(len(arr)):
        if arr[i]>largest:
            second_large = largest 
            largest = arr[i]
        elif arr[i]<largest and arr[i]>second_large:
            second_large = arr[i]
    if second_large == -float('inf'):
        return -1
    return second_large
arr = [5,3,6,4,7,11,12]
print(Second_largest(arr))