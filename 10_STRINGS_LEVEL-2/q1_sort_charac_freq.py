## We have to sort the characters in a string by their frequency
## BRUTE FORCE - TC - O(n+k^2) -- Wrost case - O(n^2), SC - O(1)
# Approach - we check for the maximum value in hahmap , append it to the ans and remove that key value from the hashmap, and then update the max_value to the new maximum 
def sort_char_freq_brute(s):
    freq = {}
    ans = ""
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i],0)+1

    while freq:
        max_value = max(freq.values())
        for ch in list(freq.keys()):
            if freq[ch] == max_value:
                ans+=ch*max_value
                freq.pop(ch)
    return ans
print(sort_char_freq_brute("tree"))

## OPTIMAL CODE - TC - O(n+klogk),SC-o(n)
def sort_char_freq_opt(s):
    freq = {}
    ans = ""
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i],0)+1
    sorted_freq = sorted(freq.items(),key = lambda x: x[1],reverse=True)
    for key , value in sorted_freq:
        ans+=key*value
    return ans
print(sort_char_freq_opt("Aabb"))

