## RETURN TRUE IF THE GIVEN STRING IS ANAGRAM OF THE PREVIOUS STRING 
# Brute Force - TC - O(n),SC - o(n)
def valid_anagram_brute(s,t):
    if len(s)!=len(t):
        return False
    freq1 = {}
    freq2 = {}
    for i in range(len(s)):
        freq1[s[i]] = freq1.get(s[i],0)+1
        freq2[t[i]] = freq2.get(t[i],0)+1
    return freq1==freq2
s = "anagram"
t = "ganarma"
print(valid_anagram_brute(s,t))

# BETTER APPROACH -
def valid_anagram_bett(s,t):
    if len(s)!=len(t):
        return False
    freq = {}
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i],0)+1
    for i in range(len(s)):
        if t[i] not in freq:
            return False
        freq[t[i]]-=1
    for value in freq.values():
        if value!=0:
            return False
    return True
s = "akshat"
t = "kshata"
print(valid_anagram_bett(s,t))

## ONE LINER APPROACH 
def valid_anagram(s,t):
    return sorted(s.lower())==sorted(t.lower())
print(valid_anagram(s,t))

