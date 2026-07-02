## RETURN THE SUM OF BEAUTY OF ALL SUBSTRINGS
# BRUTE FORCE 
def sum_beauty_substr_brute(s):
    summ = 0 
    for i in range(len(s)):
        for j in range(i,len(s)):
            freq = {}
            a = s[i:j+1]
            for m in a:
                freq[m] = freq.get(m,0)+1
            summ+=max(freq.values())-min(freq.values())
    return summ 
s = "aabcbaa"
print(sum_beauty_substr_brute(s))

# OPTIMAL SOLUTION 
def sum_beauty_substr_opt(s):
    summ = 0 
    for i in range(len(s)):
        freq = {}
        for j in range(i,len(s)):
            freq[s[j]] = freq.get(s[j],0)+1
            summ+=max(freq.values())-min(freq.values())
    return summ
s = "aabcbaa"
print(sum_beauty_substr_opt(s))