## BRUTE Force - traverse through the check matrix and reutnr the index of the peak value 
## brute force - return the index of the max_element

## OPTIMAL CODE - BINARY SEARCH 
def find_peak_ele(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    low = 0
    high = cols - 1
    while low<=high:
        mid = (low+high)//2

        ## find the max_row in a col such that it will be easier, since the element at max_row and mid will be greater than its top and bottom element 
        max_row = 0
        for i in range(rows):
            if matrix[i][mid]>matrix[max_row][mid]:
                max_row=i

        # Now we have the max_element in mid - and that row too now to compare with its left and right we must have the left and right 
        # So initiating left and right as -1
        left = -1
        right = -1
        if mid-1>=0:                         # getting the left value 
            left = matrix[max_row][mid-1] 
        if mid+1<cols:
            right = matrix[max_row][mid+1]
        
        # Now comparing the value 
        if matrix[max_row][mid]>left and matrix[max_row][mid]>right:
            return [max_row,mid]
        elif right>matrix[max_row][mid]:
            low = mid+1
        else:
            high = mid-1
mat = [[10,11,15],[21,9,14],[7,16,32]]
print(find_peak_ele(mat))
        

        