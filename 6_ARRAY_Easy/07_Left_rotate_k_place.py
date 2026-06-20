## LEFT ROTATE K PLACES 

def Left_rotate_k_places(arr,k):
    k = k%len(arr)
    return arr[k:] + arr[:k]
arr = [2,3,4,5,6,7]
print(Left_rotate_k_places(arr,3))





