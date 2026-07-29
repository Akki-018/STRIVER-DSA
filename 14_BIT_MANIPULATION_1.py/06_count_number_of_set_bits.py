## TO COUNT THE NUMBER OF SET BITS IN A BINARY REPRESENTATION OF A NUMBER 
# BRUTE FORCE CODE  - TC - o(log2n),SC-o(1)
def count_number_set_bits(n): 
    cnt = 0 
    while n>0:
        cnt+=(n&1)
        n=n>>1
    return cnt 
print(count_number_set_bits(40))

# Optimal approach - Brian Kernighian Algo 
def count_number_set_bit_opt(n):
    cnt = 0 
    while n>0:
        cnt+=1
        n=n&(n-1)
    return cnt 
print(count_number_set_bit_opt(40))

