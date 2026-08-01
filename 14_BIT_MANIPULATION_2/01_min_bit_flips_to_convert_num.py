## Minimum bits flips to convert a number 

# BRUTE FORCE - Without bit manipulation 
def min_bits_flip_brut(start,goal):
    start_bin = bin(start)[2:]
    goal_bin = bin(goal)[2:]

    leng = max(len(start_bin),len(goal_bin))
    start_bin = start_bin.zfill(leng)
    goal_bin = goal_bin.zfill(leng)
    cnt = 0 
    for i in range(leng):
        if start_bin[i]!=goal_bin[i]:
            cnt+=1
    return cnt 
print(min_bits_flip_brut(10,7))

## OPTIMAL SOLUTION
def min_bits_flip_opt(start,goal):
    xor = start^goal
    cnt = 0 
    while xor>0:
        cnt+=(xor&1)
        xor = xor>>1
    return cnt 
print(min_bits_flip_opt(10,7))
