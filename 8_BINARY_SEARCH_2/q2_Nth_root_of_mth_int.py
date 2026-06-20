# Linear Traversal
def nthroot(x,m):
    for i in range(1,m+1):
        if i**x == m:
            return i
        elif i**x>m:
            break 
    return -1
print(nthroot(4,69))

# BINARY SEARCH - OPTIMAL SOLUTION
def nthRootOpt(x,m):
    low = 1
    high = m
    while low<=high:
        mid = (low+high)//2
        if mid**x==m:
            return mid
        elif mid**x < m:
            low = mid+1
        else:
            high = mid-1
    return -1
print(nthRootOpt(3,27))

    