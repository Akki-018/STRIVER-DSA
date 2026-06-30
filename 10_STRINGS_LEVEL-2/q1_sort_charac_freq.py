## We have to sort the characters in a string by their frequency
# BRUTE FORCE - TC - O(n+k^2) -- Wrost case - O(n^2), SC - O(1)
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