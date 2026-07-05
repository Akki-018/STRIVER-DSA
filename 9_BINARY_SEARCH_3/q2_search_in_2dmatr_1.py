## To find the given target element in the matrix and return True or False , m = no. of rows , n = no. of cols
# Brute force -- TC - o(m*n) , SC- o(1)
def search_2dmat_1_brute(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_2dmat_1_brute(matrix,11))

# Optimal code - BINARY SEARCH 
def search_2dmat_2_opt(matrix,target): 
    
    rows = len(matrix)
    cols = len(matrix[0])
    low  = 0
    high = rows*cols - 1
    while low<=high:
        mid = (low+high)//2
        row = mid//cols
        col = mid%cols 
        if matrix[row][col] == target:
            return True
        elif matrix[row][col]<target:
            low = mid+1
        else:
            high = mid-1
    return False
print(search_2dmat_2_opt(matrix,11))

