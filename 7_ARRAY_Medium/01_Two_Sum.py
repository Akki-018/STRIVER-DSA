## TWO SUM 
# BRUTE FORCE
def Two_sum(arr,k):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]+arr[j] == k and arr[i]!=arr[j]:
                return [i,j]
    return -1
arr = [3,3,1]
print(Two_sum(arr,4))

# BETTER CODE - using HASHMAP
# Returns in True and False
def Two_Sum(arr,k):
    freq = {}
    
    for i in range(len(arr)):
        diff = k-arr[i]
        if diff in freq:
            return True
        freq[arr[i]]=1
    return False
arr = [2,6,5,8,11]
print(Two_Sum(arr,9))

# Returns index of the values
def Two_Sum(arr,k):
    freq = {}
    
    for i in range(len(arr)):
        diff = k - arr[i]
        if diff in freq:
            return [freq[diff],i]
        freq[arr[i]] = i
    
    return -1
arr = [2,6,5,8,11]
print(Two_Sum(arr,14))


## OPTIMAL CODE
def Two_Sum_Optim(arr,k):
    arr.sort()
    i = 0
    j = len(arr)-1
    while i!=j:
        if arr[i]+arr[j] > k:
            j-=1
        elif arr[i]+arr[j] < k:
            i+=1 
        else:
            return True
    return False
arr = [2,6,5,8,11]
print(Two_Sum_Optim(arr,4))




        