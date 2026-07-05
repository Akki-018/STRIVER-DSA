## RETURN THE LONGEST COMMON PREFIX -- VERTICAL SCANNING
# BRUTE FORCE -- We compare column wise
def longest_comm_prefix(strs):
    a = ""
    min_len = len(strs[0])
    for i in strs:
        min_len = min(min_len,len(i))
    for i in range(min_len):
        for j in range(1,len(strs)):
            if strs[j][i]!=strs[0][i]:
                return a 
        a += strs[0][i]
    return a
print(longest_comm_prefix(["flower","fl","flag"]))

## 