## TO SET/UNSET THE RIGHTMOST UNSET BIT 
# for unset - do n = n&(~(1<<i))
# BRUTE FORCE 
def set_unset_rightmost_bit_bru(n):
    for i in range(32):
        if n&(1<<i)==0:
            n = n|(1<<i)
            break
    return n 
print(set_unset_rightmost_bit_bru(13))

# OPTIMAL SOLUTION 
def set_unset_rightmost_bit_opt(n):
    return n|(n+1)
print(set_unset_rightmost_bit_opt(13))