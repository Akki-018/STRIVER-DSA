## Search in a matrix a targeted element -- but the matrix is ascending from left to right , increases from top to bottom 

# BRUTE FORCE - TC - o(m*n), SC- o(1)
def search_2d_2_brute(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(search_2d_2_brute(matrix,5))

## OPTIMAL SOLUTION -- BINARY SEARCH - TC - O(m*log(n)), SC-o(1)
def search_2d_2_opt(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        low = 0
        high = cols-1
        while low<=high:
            mid = (low+high)//2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid]<target:
                low = mid+1
            else:
                high = mid-1
    return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(search_2d_2_opt(matrix,122))
