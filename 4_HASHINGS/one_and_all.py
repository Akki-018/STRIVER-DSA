# BRUTE FORCE APPROACH --- Checks for each iteration 
def Brute_Hashing(arr,n):
    cnt = 0 
    for i  in arr: 
        if i==n:
            cnt+=1
    return cnt
arr = [1,3,2,1,3,1,2]
print(Brute_Hashing(arr,3)) 

## HASHING using HASH ARRAY(Frequency storing in array)
def Hash_array(arr):
    hash_arr = [0]*10              # Hash array created 
    for num in arr:
        hash_arr[num]+=1
    return hash_arr
arr = [1,3,2,1,3,1,2]
print(Hash_array(arr))

## HASHING using HASH MAP(Dictionary using)
def Hash_map(arr):
    hash_map ={}
    for num in arr:
        hash_map[num] =  hash_map.get(num,0)+1
    return hash_map
arr = [1,3,2,1,3,1,2]
print(Hash_map(arr))



