## To reverse an array by recursion
# simple method - to return arr[::-1] - using slicing technique 

# Iterative Formula
def iterative(arr,n):
    for i in range(n):
        if i>=n//2:
            return arr
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
arr = [1,2,3,4,5]
print(iterative(arr,5))

# Recursive formula-1
def recursive_1(arr,left,right):
    if left>=right:
        return 
    arr[left],arr[right] = arr[right],arr[left]
    recursive_1(arr,left+1,right-1)
arr = [1,2,3,4,5]
recursive_1(arr,0,len(arr)-1)
print(arr)

def recursive_2(arr,i,n):
    if i>=n//2:
        return 
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    recursive_2(arr,i+1,n)
arr = [1,3,4,5,6]
recursive_2(arr,0,5)
print(arr)