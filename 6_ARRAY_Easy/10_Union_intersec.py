## Union of Two sorted Arrays
# Brute force  TC - O((m+n)log(m+n)) , SC - O(m+n)
def Union(arr1, arr2):
    Set_arr1 = set(arr1)

    Set_arr2 = set(arr2)
    Union_set = Set_arr1.union(Set_arr2)
    return Union_set
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]
print(Union(arr1,arr2))

# Optimal code   TC - O(m+n) , SC - O(m+n)
def Union(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0 
    j = 0
    result = []
    
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i]) 
            i+=1 
        elif arr1[i]>arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j+=1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i+=1
            j+=1
    while i<m: 
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i+=1
    while j<n:
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j+=1
    return result 
        
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]
print(Union(arr1,arr2))


# Intersection of two sorted arrays
def Intersection(arr,n,brr,m):
    i = 0
    j = 0
    result = []
    while i<n and j<m:
        if arr[i]<brr[j]:
            i+=1
        elif arr[i]>brr[j]:
            j+=1
        else:
            if not result or result[-1] != arr[i]:
                result.append(arr[i])
            i+=1
            j+=1
    return result 
arr = [1,1,2,3,4,5]
brr = [2,3,4,4,5,6]
print(Intersection(arr,6,brr,6))

# Intersection of two Unsorted Arrays 
def Intersection_Unsorted(arr,brr):
    freq = {}
    visited = {}
    result = []
    for x in (arr):
        freq[x] = 1
    for i in brr:
        if i in freq and i not in visited:
            result.append(i) 
            visited[i]=1 
    return result
arr = [4,9,5,2]
brr = [9,4,9,8,4]
print(Intersection_Unsorted(arr,brr))