## LEFT ROTATE THE ARRAY BY ONE PLACE
# DIRECT CODE
def Left_Rotate(arr):
    return arr[1:len(arr)] + arr[0:1]
arr = [2,3,4,5,6]
print(Left_Rotate(arr))

# LOGICAL CODE
def Left_rotate_logial(arr):
    a = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = a 
    return arr
arr = [2,3,4,5,6]
print(Left_rotate_logial(arr))


