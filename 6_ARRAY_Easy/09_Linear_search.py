## LINEAR SEARCH - search of an element in an array linearly
def Linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1
arr = [7,4,2,1,5,2]
print(Linear_search(arr,5))
