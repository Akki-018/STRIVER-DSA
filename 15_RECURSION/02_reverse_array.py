## To reverse an array by recursion
# simple method - to return arr[::-1] - using slicing technique 

# Recursive formula 
def recursive(arr,n):
    for i in range(n):
        if i>=n//2:
            return arr
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
arr = [1,2,3,4,5]
print(recursive(arr,5))

    