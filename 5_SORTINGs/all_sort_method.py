## SELECTION SORT
def Selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i                       #Assume the min index is the current position
        for j in range(i+1,n):              #loops run for the rest of the array    
            if arr[j]<arr[min_index]:
                min_index = j               # updates the min_index to the number which actually haves the min index 
        arr[i], arr[min_index] = arr[min_index] ,arr[i] ## SWAPS the values
    return arr

arr = [13,46,24,52,20,9]
print(Selection_sort(arr))

## BUBBLE SORT 
def Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):              # not (i+1, n) bcoz out of arr
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr = [5,1,4,2,8]
print(Bubble_sort(arr)) 

## INSERTION SORT 
def Insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i-1
        while j>0:
            if arr[j-1] >arr[j]:
                arr[j-1],arr[j]= arr[j], arr[j-1]
            j=j-1
    return arr

arr = [1,2,3,2,5]
print(Insertion_sort(arr))

## MERGE SORT 
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right= merge_sort(arr[mid:])

    return merge(left, right)
def merge(left, right):
    result = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result 
arr = [5,1,4,3,2,6]
print(merge_sort(arr))

# RECURSIVE BUBBLE SORT
def Re_Bubble(arr,n):
    if n==1:
        return arr
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return Re_Bubble(arr,n-1)
arr  = [5,1,4,3,2,6]
print(Re_Bubble(arr,6))

# RECURSIVE INSERTION SORT
def Re_Insertion(arr,n):
    if n<=1:
        return arr
    Re_Insertion(arr,n-1)
    last = arr[n-1]
    j = n-2
    while j>=0 and arr[j]>last:
        arr[j+1]= arr[j]
        j-=1

    arr[j+1]=last
    return arr
arr = [5,1,4,3,2,6]
print(Re_Insertion(arr,6))
    
## QUICK SORT
def Quick_sort(arr):
    n = len(arr)
    # base case
    if n<=1:
        return arr
    pivot_index = arr[n-1]     # creating the last element as the pivot element 
    left = []
    right = []
    equal = []
    for i in range(n):                # appending the elements on the list left, right, equal based on the comparison from pivot
        if arr[i]<pivot_index:
            left.append(arr[i])
        elif arr[i]>pivot_index:
            right.append(arr[i])
        else:
            equal.append(arr[i])

    left_sorted = Quick_sort(left)       # sorting of left arr by recursion method 

    right_sorted = Quick_sort(right)     # sorting of right arr by recursion method

    return left_sorted+equal+right_sorted 
arr = [5,2,4,6,7,3]
print(Quick_sort(arr))


            


