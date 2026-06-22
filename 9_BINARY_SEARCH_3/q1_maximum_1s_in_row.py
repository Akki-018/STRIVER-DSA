## Maximum 1s in a row in a matrix -- to return the maximum number in a row and its index

# Brute Force -- TC - o(n), SC - O(n)
def maxi_1_row(matrix):
    store = {}
    maxi_1 = float('-inf')
    for i in range(len(matrix)):
        maxi_1 = max(maxi_1,matrix[i].count(1))
        store[i] = maxi_1
    for key, value in store.items():
        if value == max(store.values()):
            return key,value
matrix = [[0,1],[1,0]]
print(maxi_1_row(matrix))

# Optimal Solution - BINARY SEARCH - only when the rows of this matrix is sorted 
## OPTIMAL FORCE - Binary Search 
def maxi_1_row_optimal(mat):
        rows = len(mat)
        cols = len(mat[0])
        def lowerbound(arr):
            low = 0
            high = len(arr)-1
            ans = cols
            while low<high:
                mid = (low+high)//2
                if arr[mid]>=1:
                    ans = mid
                    high = mid-1
                else:
                    low = mid+1
            return ans 
        
        cnt_max = -1 
        index = 0
        for i in range(rows):
            cnt_ones = cols-lowerbound(mat[i])
            if cnt_ones>cnt_max:
                cnt_max = cnt_ones
                index = i
        return [index, cnt_max]
matrix = [[0,0,1],[0,1,1]]
print(maxi_1_row_optimal(matrix))