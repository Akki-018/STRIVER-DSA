## PROBLEM - 1 ==> Count the number of substrings of a string
def count_num_substr(s):
    return int((len(s)*(len(s)+1)/2))
print(count_num_substr("abcde"))

## PROBLEM - 2 ==> Count the number of homogeneous substrings in a string (leectcode 1759)
# BRUTE FORCE - TC - O(n^3) 
def count_num_homo_substr_brute(s):
    cnt = 0 
    for i in range(len(s)):
        for j in range(i,len(s)):
            if len(set(s[i:j+1])) == 1:
                cnt+=1
    return cnt 
s = "abbcccaa"
print(count_num_homo_substr_brute(s))

# BETTER CODE -
def count_num_homo_substr_bett(s):
    cnt = 0 
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i]==s[j]:
                cnt+=1
            else:
                break
    return cnt 
s = "abbcccaaa"
print(count_num_homo_substr_bett(s))

# OPTIMAL CODE 
def count_num_homo_substr_opt(s):
    cnt = 0 
    leng = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            leng+=1
        else:
            cnt += leng*(leng+1)//2
            leng = 1 
    cnt= (cnt+leng*(leng+1)//2)%(10**9+7)
    return cnt
s = "abbcccaaa"
print(count_num_homo_substr_opt(s))

## PROBLEM - 3 ==> Count the number of substrings with only 1s 
def count_subst_1s(s):
    cnt = 0 
    leng = 0 
    for i in range(len(s)):
        if s[i]=='1':
            leng += 1
        else:
            cnt+=leng*(leng+1)//2
            leng = 0
    cnt = (cnt+leng*(leng+1)//2)%(10**9+7)
    return cnt 
s = "0110111"
print(count_subst_1s(s))





