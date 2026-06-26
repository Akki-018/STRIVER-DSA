## RETURN TRUE IF THE GIVEN STRING IS ANAGRAM OF THE PREVIOUS STRING 
# Brute Force
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
t = "ganarim"
print(valid_anagram_brute(s,t))

    